from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def evaluate_model(model, test_data, test_features):
    # Predict values
    predictions = model.predict(test_features)
    
    # Calculate error
    mse = mean_squared_error(test_data, predictions)
    
    # Plot results
    plt.plot(test_data, label="True Data")
    plt.plot(predictions, label="Predictions")
    plt.legend()
    plt.show()
    
    return mse
