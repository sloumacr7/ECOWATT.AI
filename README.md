# EcoWatt: AI-driven Energy Management Solution

*Optimizing Energy Consumption for a Sustainable Future*

![462572902_1353126115656048_4448500756589272563_n](https://github.com/user-attachments/assets/3f675bca-3d46-4c6d-ab17-d55c8bad3065)

## Overview

EcoWatt is an advanced energy management solution designed to optimize energy consumption in industrial buildings. The system leverages Non-Intrusive Load Monitoring (NILM) and artificial intelligence (AI) techniques to analyze and manage energy usage, reducing energy waste, improving efficiency, and supporting sustainability. By monitoring electrical loads and applying predictive analytics, EcoWatt helps industries identify inefficiencies and potential savings.

## Features

- **Energy Consumption Prediction**: Predict energy usage based on historical data and operational factors.
- **Load Disaggregation (NILM)**: Break down total energy consumption into individual machines or equipment to track specific usage.
- **Anomaly Detection**: Identify abnormal patterns in energy consumption that could indicate equipment malfunction or inefficiency.
- **Energy Efficiency Scoring**: Score the energy efficiency of different equipment and overall building performance.
- **Predictive Alerts**: Provide real-time alerts for maintenance needs or abnormal consumption patterns.
- **Sustainability Reporting**: Generate reports to track and optimize energy consumption for sustainability goals.

## Technologies Used

- **Machine Learning**: TensorFlow, Keras, scikit-learn
- **Signal Processing**: PyWavelets for wavelet transformation
- **Data Processing**: Pandas, NumPy
- **Time-Series Analysis**: TSFresh, sktime
- **Visualization**: Matplotlib, Plotly, Seaborn
- **NILM Framework**: NILMTK for non-intrusive load monitoring
- **Anomaly Detection**: PyOD for detecting anomalies in energy usage patterns

![Capture d'écran 2024-11-14 184933](https://github.com/user-attachments/assets/b0dcda10-ea8f-415f-9107-706c88013a5e)

## Getting Started

### Prerequisites

- Python 3.8 or later
- Git installed
- A GitHub account to clone the repository and contribute

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/EcoWatt.git
    ```
    Then, navigate into the project directory:
    ```bash
    cd EcoWatt
    ```

2. Install the dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the sample datasets (e.g., IMDELD, HIPE, HIPE) for training the model.

### Running the Project

1. Launch the main energy monitoring and prediction system:
    ```bash
    python run_model.py
    ```

2. For viewing the dashboard:
    ```bash
    python app.py
    ```


## Contributing

We welcome contributions to improve the EcoWatt project! Whether you’re fixing bugs, adding new features, or improving documentation, we value your contributions.

### Steps to contribute:

1. Fork the repository on GitHub.
2. Clone your fork to your local machine:
    ```bash
    git clone https://github.com/your-username/EcoWatt.git
    ```
3. Create a new branch for your changes:
    ```bash
    git checkout -b new-feature
    ```
4. Make your changes and commit them:
    ```bash
    git commit -am 'Add new feature'
    ```
5. Push to your fork:
    ```bash
    git push origin new-feature
    ```
6. Submit a pull request through GitHub!


## Acknowledgments

- Thanks to the NILMTK and PyOD libraries for their support in non-intrusive load monitoring and anomaly detection, respectively.
- Thanks to the contributors and open-source community for their work on energy efficiency and sustainability research.
