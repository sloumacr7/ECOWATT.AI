import numpy as np

# Extracting Approximation and Detail Coefficients from the signal (using wavelets)
def extract_wavelet_features(data):
    """
    Extracts wavelet features from the energy consumption signal.
    This method returns approximation and detail coefficients.
    """
    import pywt
    
    wavelet = 'db1'  # Example: Daubechies wavelet
    approximation, details = pywt.dwt(data, wavelet)
    
    return approximation, details

# Extract Harmonic Ratio
def extract_harmonic_ratio(data):
    """
    Extract harmonic ratio for energy consumption data.
    """
    frequency = np.fft.fftfreq(len(data))
    fft_values = np.fft.fft(data)
    harmonic_ratio = np.abs(fft_values[1]) / np.abs(fft_values[0])  # Simplified ratio
    
    return harmonic_ratio

# Function to perform Feature Extraction on the full dataset
def extract_features(data):
    """
    Extract relevant features for each machine.
    """
    features = {}
    for i, machine_data in enumerate(data):
        approximation, details = extract_wavelet_features(machine_data)
        harmonic_ratio = extract_harmonic_ratio(machine_data)
        
        features[f'machine_{i}'] = {
            'approximation': approximation,
            'details': details,
            'harmonic_ratio': harmonic_ratio
        }
    
    return features
