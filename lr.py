import tensorflow as tf
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import datetime

start = datetime.datetime.now()

print("train start=", start)


df = pd.read_csv('/home/ubuntu/Documents/canonical/drives.csv', usecols=['failure', 'smart_5_raw','smart_187_raw', 'smart_188_raw'])
df.dropna()

train, test = train_test_split(df, test_size=0.2)

labels = train['failure']
features = train[['smart_5_raw','smart_187_raw', 'smart_188_raw']]

model = Sequential()

model.add(Dense(3, input_shape=(1,)))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(labels, features,
          batch_size=12,
          epochs=10,
          verbose=1,
          validation_data=(labels, features))
          
model.evaluate(labels, features, verbose=0)

model.summary()


end = datetime.datetime.now()

print("train end=", end)

print("train elapsed=", end - start)
