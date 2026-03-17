import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message

import tensorflow as tf 

#create grid using randome
print(tf.__version__)          # should be 2.10 or newer ideally

grid_1 = tf.random.normal(shape=[5,3],mean=10,stddev=2)
print(grid_1)

grid_2 = tf.random.normal(shape=[5],mean=100,stddev=4,dtype=tf.double)
print(grid_2)
