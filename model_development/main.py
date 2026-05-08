# ========================================================
# TEST VERSION - SMALL DATASET + FAST START
# ========================================================

import tensorflow as tf
from tensorflow.keras import layers, Model, callbacks, optimizers
import os
from glob import glob
import argparse
import time

# GPU Setup
print("🔍 GPU Setup...")
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    print(f"✅ GPU: {tf.config.experimental.get_device_details(gpus[0])['device_name']}")

tf.keras.mixed_precision.set_global_policy('mixed_float16')

# ===================== CONFIG =====================
parser = argparse.ArgumentParser()
parser.add_argument('--data_root', type=str, required=True)
parser.add_argument('--batch_size', type=int, default=4)
parser.add_argument('--epochs', type=int, default=5)
parser.add_argument('--max_images', type=int, default=5000, help="Use only this many images for testing")
args = parser.parse_args()

BATCH_SIZE = args.batch_size
EPOCHS = args.epochs
MAX_IMAGES = args.max_images

# ===================== PATHS =====================
DATA_ROOT = args.data_root
TRAIN_WM_DIR = os.path.join(DATA_ROOT, "train", "watermarked_image")
TRAIN_CLEAN_DIR = os.path.join(DATA_ROOT, "train", "Watermark_free_image")

wm_files = sorted(glob(os.path.join(TRAIN_WM_DIR, "*.*")))[:MAX_IMAGES]
clean_files = sorted(glob(os.path.join(TRAIN_CLEAN_DIR, "*.*")))[:MAX_IMAGES]

print(f"✅ Using {len(wm_files):,} images for testing")

val_size = max(1, int(len(wm_files) * 0.1))

# ===================== FAST DATA =====================
def load_pair(wm_path, clean_path):
    wm = tf.image.decode_jpeg(tf.io.read_file(wm_path), 3)
    clean = tf.image.decode_jpeg(tf.io.read_file(clean_path), 3)
    wm = tf.image.resize(wm, [256, 256])
    clean = tf.image.resize(clean, [256, 256])
    wm = tf.cast(wm, tf.float32) / 255.0
    clean = tf.cast(clean, tf.float32) / 255.0
    return wm, clean

train_ds = tf.data.Dataset.from_tensor_slices((wm_files[val_size:], clean_files[val_size:]))
train_ds = train_ds.shuffle(1000).map(load_pair, num_parallel_calls=1).batch(BATCH_SIZE).prefetch(1)

val_ds = tf.data.Dataset.from_tensor_slices((wm_files[:val_size], clean_files[:val_size]))
val_ds = val_ds.map(load_pair, num_parallel_calls=1).batch(BATCH_SIZE).prefetch(1)

# ===================== LOSS =====================
def combined_loss(y_true, y_pred):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))
    ssim = 1.0 - tf.reduce_mean(tf.image.ssim(y_true, y_pred, max_val=1.0))
    return 0.85 * mse + 0.15 * ssim

# ===================== U-NET (Smaller for speed) =====================
def build_unet():
    inputs = layers.Input((256, 256, 3))
    c1 = layers.Conv2D(48, 3, activation='relu', padding='same')(inputs)
    c1 = layers.MaxPooling2D(2)(c1)
    c2 = layers.Conv2D(96, 3, activation='relu', padding='same')(c1)
    c2 = layers.MaxPooling2D(2)(c2)
    c3 = layers.Conv2D(192, 3, activation='relu', padding='same')(c2)
    
    u2 = layers.Conv2DTranspose(96, 2, strides=2, padding='same')(c3)
    u1 = layers.Conv2DTranspose(48, 2, strides=2, padding='same')(u2)
    outputs = layers.Conv2D(3, 1, activation='sigmoid')(u1)
    return Model(inputs, outputs)

model = build_unet()
model.summary()

model.compile(optimizer=optimizers.Adam(3e-4), loss=combined_loss, metrics=['mae'])

# ===================== PROGRESS =====================
class SimpleProgress(callbacks.Callback):
    def on_epoch_begin(self, epoch, logs=None):
        print(f"\n=== Epoch {epoch+1}/{EPOCHS} started ===")
        self.start = time.time()

    def on_batch_end(self, batch, logs=None):
        if batch % 10 == 0:
            print(f"   Batch {batch+1:4d} done", end="\r")

    def on_epoch_end(self, epoch, logs=None):
        print(f"✅ Epoch {epoch+1} done | Loss: {logs.get('loss'):.4f}")

print("\n🚀 Starting Training (Small Test Version)...\n")

model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=[SimpleProgress()], verbose=0)
print("🎉 Test Training Finished!")
model.save("watermark_test_model.keras")