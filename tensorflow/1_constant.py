import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message


import tensorflow as tf
numbers = [10,5,12,18,11,7,90]
#create tensor 
tensor = tf.constant(numbers)
print(tensor)
grid = [
            [1,2,3],
            [4,5,6]
    ]

tensor2 = tf.constant(grid)
print(tensor2)