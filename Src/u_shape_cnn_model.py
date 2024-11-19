import pickle

# Load model
MODEL_PATH = "./models/u_shape_cnn_model.pkl"

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Example usage
def predict(input_data):
    # Ensure input_data is preprocessed as needed
    predictions = model.predict(input_data)
    return predictions
