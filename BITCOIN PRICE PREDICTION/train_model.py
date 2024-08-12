import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense # type: ignore
from preprocess_data import preprocess_data

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model():
    X_train, X_test, y_train, y_test, scaler = preprocess_data('E://download//elevate//BITCOIN PRICE PREDICTION//bitcoin_data.csv')
    model = build_model((X_train.shape[1], 1))
    
    X_train = np.expand_dims(X_train, axis=-1)
    X_test = np.expand_dims(X_test, axis=-1)
    
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    model.save('bitcoin_price_model.h5')
    
    return model, scaler

if __name__ == "__main__":
    train_model()
