import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message

import tensorflow as tf 

#create grid using randome
print(tf.__version__)          # should be 2.10 or newer ideally

grid_1 = tf.random.uniform(shape=[5,3])
print(grid_1)

vector = tf.random.uniform(shape=[5],minval=10,maxval=100)
print(vector)
