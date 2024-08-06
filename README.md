Car Price Prediction Web App
Overview
This project is a web application designed to predict car prices using machine learning. It leverages a Linear Regression model to estimate the value of a car based on various features such as the car's name, manufacturing year, current price, kilometers driven, ownership history, fuel type, seller type, and transmission type.

Features
User-Friendly Interface: Easily input car details through a simple web interface.
Accurate Predictions: Provides car price estimates using a trained Linear Regression model.
Real-Time Results: Instant prediction display based on user inputs.
How It Works
Data Preparation
Data Encoding: Converts categorical data (e.g., car names, fuel types) into numerical format for model processing.
Feature Scaling: Standardizes numerical features to improve model accuracy.
Model Training
Data Splitting: Divides the dataset into training and testing sets.
Model Training: Trains a Linear Regression model on the training data.
Web Application
User Input: Users input car details like name, year, and mileage through the web interface.
Price Prediction: The app uses the trained model to predict and display the car's price.
Getting Started
Prerequisites
Python 3.x
Streamlit
Pandas
Numpy
Scikit-learn
Pickle
Installation
Clone the repository:
sh
Copy code
git clone https://github.com/your-username/car-price-prediction.git
Navigate to the project directory:
sh
Copy code
cd car-price-prediction
Install the required packages:
sh
Copy code
pip install -r requirements.txt
Running the App
Ensure the car_price_model.pkl file is in the project directory.
Run the Streamlit app:
sh
Copy code
streamlit run app.py
Project Structure
app.py: Contains the Streamlit app code.
car_price_model.pkl: Pickle file containing the trained model, scaler, and label encoder.
requirements.txt: Lists the required Python packages.
Usage
Launch the web app using the above command.
Enter the car details in the provided fields.
Click the "Predict" button to get the estimated car price.
