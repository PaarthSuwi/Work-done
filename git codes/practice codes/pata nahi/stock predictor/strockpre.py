import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow import _keras_module
from keras import models
from keras import layers
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt

stock_symbol = 'AAPL'
start_date = '2010-01-01'
end_date = '2022-01-01'

file_path = 'C:\\Users\\paart\\OneDrive\\Desktop\\Edit\\work\\faaltu bakwaas\\pata nahi\\stock predictor\\AAPL.csv'
data = pd.read_csv(file_path)  
stock_data = data['AdjClose']
# Step 2: Data Preprocessing
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(stock_data.values.reshape(-1, 1))

training_data_len = int(np.ceil(len(scaled_data) * 0.8))
train_data = scaled_data[0:training_data_len, :]

# Create training data sequences
sequence_length = 60
x_train = []
y_train = []
for i in range(sequence_length, len(train_data)):
    x_train.append(train_data[i - sequence_length:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# Reshape the data for LSTM input
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Step 3: Model Creation
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)

# Call model on a test input
x = tf.ones((3, 3))
y = model(x)

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# Step 4: Predictions
test_data = scaled_data[training_data_len - sequence_length:, :]
x_test = []

for i in range(sequence_length, len(test_data)):
    x_test.append(test_data[i - sequence_length:i, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Plot the predictions
train = stock_data[:training_data_len]
valid = stock_data[training_data_len:]
valid['Predictions'] = predictions

plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Date')
plt.ylabel('AdjClose Price USD ($)')
plt.plot(train)
plt.plot(valid[['AdjClose', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()