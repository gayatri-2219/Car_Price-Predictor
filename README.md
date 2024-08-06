# Car Price Prediction Web App

## Overview
This project is a web application designed to predict car prices using machine learning. It leverages a Linear Regression model to estimate the value of a car based on various features such as the car's name, manufacturing year, current price, kilometers driven, ownership history, fuel type, seller type, and transmission type.

## Features
- **User-Friendly Interface**: Easily input car details through a simple web interface.
- **Accurate Predictions**: Provides car price estimates using a trained Linear Regression model.
- **Real-Time Results**: Instant prediction display based on user inputs.

## Workingn

### Data Preparation
1. **Data Encoding**: Converts categorical data (e.g., car names, fuel types) into numerical format for model processing.
2. **Feature Scaling**: Standardizes numerical features to improve model accuracy.

### Model Training
1. **Data Splitting**: Divides the dataset into training and testing sets.
2. **Model Training**: Trains a Linear Regression model on the training data.

### Web Application
1. **User Input**: Users input car details like name, year, and mileage through the web interface.
2. **Price Prediction**: The app uses the trained model to predict and display the car's price.

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Pickle

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/car-price-prediction.git
   ```
2. Navigate to the project directory:
   ```sh
   cd car-price-prediction
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Running the App
1. Ensure the `car_price_model.pkl` file is in the project directory.
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Project Structure
- **app.py**: Contains the Streamlit app code.
- **car_price_model.pkl**: Pickle file containing the trained model, scaler, and label encoder.
- **requirements.txt**: Lists the required Python packages.

## Usage
1. Launch the web app using the above command.
2. Enter the car details in the provided fields.
3. Click the "Predict" button to get the estimated car price.

