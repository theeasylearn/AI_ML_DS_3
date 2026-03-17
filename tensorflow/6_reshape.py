import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message

import tensorflow as tf 

grid_1 = [[1,2,3],[4,5,6]] #2 x 3 
grid = tf.Variable(grid_1)

#reshape into 3 rows and 2 column 
grid_2 = tf.reshape(grid,[3,2])
print(grid_2)

vector = tf.Variable([1,2,3,4,5,6,7,8])
#reshape into row and column
grid_3 = tf.reshape(vector,[2,4])
print(grid_3)

#reshape grid to vector 
vector_2 = tf.reshape(grid_1,[-1])
print(vector_2)

#calculate 2nd dimension of grid automatically
grid_4 = tf.reshape(vector,[4,-1])
print(grid_4)
