import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

# Define CNN model for load recognition
def create_cnn_model(input_shape):
    """
    Creates a Convolutional Neural Network (CNN) model for load recognition from energy consumption data.
    """
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(10, activation='softmax'))  # 10 is the number of classes (machines)
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Function to train the model
def train_model(model, X_train, y_train, batch_size=32, epochs=10):
    """
    Trains the model on the provided training data.
    """
    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model on the test data.
    """
    return model.evaluate(X_test, y_test)
