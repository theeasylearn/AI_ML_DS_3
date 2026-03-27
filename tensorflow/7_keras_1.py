import tensorflow as  tf 
from tensorflow.keras.layers import Dense 

#create model 
my_model = tf.keras.Sequential([
    Dense(4,activation='relu',input_shape=(3,)),
    Dense(2,activation='relu'),
    Dense(1,),
])

my_model.compile(optimizer='adam',loss='mse')
my_model.summary()