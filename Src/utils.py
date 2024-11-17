import joblib
import tensorflow as tf

# Save a model to disk
def save_model(model, filename):
    """
    Save the trained model to a file.
    """
    model.save(filename)

# Load a model from disk
def load_model(filename):
    """
    Load a model from a saved file.
    """
    return tf.keras.models.load_model(filename)

# Save a scaler for data normalization
def save_scaler(scaler, filename):
    """
    Save the scaler to file for future use (e.g., StandardScaler).
    """
    joblib.dump(scaler, filename)

# Load the saved scaler
def load_scaler(filename):
    """
    Load the scaler from file.
    """
    return joblib.load(filename)
