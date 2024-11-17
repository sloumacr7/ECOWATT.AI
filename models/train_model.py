from model import create_model
from data_preprocessing import preprocess_data
from feature_extraction import extract_features
import numpy as np

def train_model(data):
    # Preprocess data
    train_data, test_data, scaler = preprocess_data(data)
    
    # Extract features
    train_features, test_features = extract_features(train_data)
    
    # Create model
    model = create_model(input_shape=(train_features.shape[1], 1))
    
    # Train the model
    model.fit(train_features, train_data, epochs=10, batch_size=32, validation_data=(test_features, test_data))
    
    return model, scaler
