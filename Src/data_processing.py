import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
def load_data(file_path):
    """
    Load the energy consumption dataset from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

# Preprocessing data (Handling missing values, normalization)
def preprocess_data(data):
    """
    Clean and preprocess the energy consumption data.
    """
    # Fill missing values with mean
    data = data.fillna(data.mean())
    
    # Normalize the data (e.g., using StandardScaler)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    return pd.DataFrame(scaled_data, columns=data.columns)

# Split the data into training and testing sets
def split_data(data, test_size=0.2):
    """
    Split the dataset into training and test sets.
    """
    X = data.drop('target', axis=1)  # Assuming 'target' is the output column
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test
