import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load the model, scaler, and label encoder from the pickle file
with open('car_price_model.pkl', 'rb') as file:
    model, scaler, le = pickle.load(file)

# Streamlit App
st.title("Car Price Prediction")

car_name = st.selectbox("Car Name", le.classes_)
year = st.slider("Year", 2000, 2021, 2018)
present_price = st.number_input("Present Price (in lakhs)", 0.0, 50.0, 9.85)
kms_driven = st.number_input("Kms Driven", 0, 500000, 40000)

# Descriptive options for Owner
owner_options = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth & Above Owner": 3}
owner = st.selectbox("Owner", list(owner_options.keys()))
owner_value = owner_options[owner]

# Descriptive options for Fuel Type
fuel_type_options = {"Petrol": 0, "Diesel": 1, "CNG": 2}
fuel_type = st.selectbox("Fuel Type", list(fuel_type_options.keys()))
fuel_type_value = fuel_type_options[fuel_type]

# Descriptive options for Seller Type
seller_type_options = {"Dealer": 0, "Individual": 1}
seller_type = st.selectbox("Seller Type", list(seller_type_options.keys()))
seller_type_value = seller_type_options[seller_type]

# Descriptive options for Transmission
transmission_options = {"Manual": 0, "Automatic": 1}
transmission = st.selectbox("Transmission", list(transmission_options.keys()))
transmission_value = transmission_options[transmission]


def predict_car_price(Car_Name, Year, Present_Price, Kms_Driven, Owner, Fuel_Type, Seller_Type, Transmission):
    input_data = pd.DataFrame({
        'Car_Name': [le.transform([Car_Name])[0]],
        'Year': [Year],
        'Present_Price': [Present_Price],
        'Kms_Driven': [Kms_Driven],
        'Owner': [Owner],
        'Fuel_Type': [Fuel_Type],
        'Seller_Type': [Seller_Type],
        'Transmission': [Transmission]
    })

    # Standardize numerical features
    input_data = scaler.transform(input_data)

    # Predict the price
    price_prediction = model.predict(input_data)
    return price_prediction[0]


if st.button("Predict"):
    predicted_price = predict_car_price(car_name, year, present_price, kms_driven, owner_value, fuel_type_value,
                                        seller_type_value, transmission_value)
    st.write(f"Predicted Car Price: Rs {round(predicted_price * 1_00_000)}")
