import numpy as np

def extract_features(data):
    # Extracting rolling averages as features
    rolling_avg = np.mean(data, axis=1)
    
    # Extracting peak consumption
    peak_consumption = np.max(data, axis=1)
    
    return rolling_avg, peak_consumption
