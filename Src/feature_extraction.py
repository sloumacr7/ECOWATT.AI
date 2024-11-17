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
# Cartesian to Polar Transformation
def cartesian_to_polar(x, y):
    """
    Converts Cartesian coordinates to Polar coordinates.

    Parameters:
    x (array-like): X-coordinates
    y (array-like): Y-coordinates

    Returns:
    r (array-like): Radii
    theta (array-like): Angles in radians
    """
    r = np.sqrt(np.square(x) + np.square(y))
    theta = np.arctan2(y, x)
    return r, theta
    # Convert wavelet features to polar coordinates
        approx_r, approx_theta = cartesian_to_polar(approximation, approximation)  # Approximation (using itself for demo)
        detail_r, detail_theta = cartesian_to_polar(details, details)              # Details (using itself for demo)
        harmonic_r, harmonic_theta = cartesian_to_polar(
            np.array([harmonic_ratio]), np.array([harmonic_ratio])
        )  # Harmonic ratio (simplified)

        features[f'machine_{i}'] = {
            'approximation_polar': (approx_r, approx_theta),
            'details_polar': (detail_r, detail_theta),
            'harmonic_ratio_polar': (harmonic_r, harmonic_theta)
        }
    
    return features
#Normalize the Time-Series Data
def normalize_series(series):
    min_val = np.min(series)
    max_val = np.max(series)
    return 2 * (series - min_val) / (max_val - min_val) - 1

approx_norm = normalize_series(approximation)
detail_norm = normalize_series(details)
harmonic_norm = normalize_series(harmonic_ratio)
#Convert Each Sequence to GAF Images
def gaf_transform(series):
    phi = np.arccos(series)  # Convert to polar coordinates
    gaf = np.cos(phi[:, None] + phi[None, :])  # Create GAF matrix
    return gaf

approx_gaf = gaf_transform(approx_norm)
detail_gaf = gaf_transform(detail_norm)
harmonic_gaf = gaf_transform(harmonic_norm)
#Combine GAF Images into an RGB Image
# Stack GAF images into an RGB format
rgb_image = np.stack([approx_gaf, detail_gaf, harmonic_gaf], axis=-1)

# Optionally, convert to a format compatible with OpenCV or image processing libraries
rgb_image = (rgb_image * 255).astype(np.uint8)  # Rescale for image format
