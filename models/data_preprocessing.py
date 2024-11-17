from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def preprocess_data(data):
    # Normalize the data
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    # Split into train and test datasets
    train_size = int(len(data) * 0.8)
    train_data, test_data = data_scaled[:train_size], data_scaled[train_size:]
    
    return train_data, test_data, scaler
