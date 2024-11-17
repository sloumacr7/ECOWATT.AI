import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Plot the loss curve during model training
def plot_loss_curve(history):
    """
    Plot the loss curve to show the model training progress.
    """
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss Curve')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

# Plot a confusion matrix for classification results
def plot_confusion_matrix(y_true, y_pred, labels):
    """
    Plot a confusion matrix to evaluate classification performance.
    """
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

# Plot a comparison of predicted vs actual values
def plot_predictions_comparison(y_true, y_pred):
    """
    Plot a comparison between predicted and actual values.
    """
    plt.plot(y_true, label='Actual Consumption')
    plt.plot(y_pred, label='Predicted Consumption')
    plt.title('Predicted vs Actual Energy Consumption')
    plt.xlabel('Time')
    plt.ylabel('Energy Consumption')
    plt.legend()
    plt.show()
