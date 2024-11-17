from tensorflow.keras.models import load_model

def save_model(model, filepath):
    model.save(filepath)

def load_model_from_file(filepath):
    return load_model(filepath)
