import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message
import tensorflow as tf
age = tf.Variable(42)
print(age)

age.assign(43)
print(age)

#create vector using list 
numbers = [10,5,12,18,11,7,90]
marks = tf.Variable(numbers)
print(marks)

#create grid 
grid = [
            [1,2,3],
            [4,5,6]
    ]

result = tf.Variable(grid)
print(result)