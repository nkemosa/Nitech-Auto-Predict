
import streamlit as st
import pandas as pd
import pickle

# Page Configuration
st.set_page_config(
    page_title="NITECH AutoPredict",
    page_icon="🚗",
    layout="wide"
)

# Load Model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🚗 NITECH AutoPredict App")
st.write("Enter the car details below to predict its estimated price.")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🚗 About This App")

st.sidebar.write("""
This application uses Machine Learning to predict
the estimated price of a car based on its features.
""")

st.sidebar.subheader("How It Works")

st.sidebar.write("""
1. Enter the car details.
2. Click the Predict Price button.
3. View the estimated car price.
""")

st.sidebar.divider()

st.sidebar.write("Developed by Nkemosa using Python & Streamlit")


# =========================
# MAIN PAGE INPUTS
# =========================

st.subheader("Enter Car Details")

# Create Columns
col1, col2, col3 = st.columns(3)

with col1:
    brand = st.selectbox(
        "Brand",
        [
            "Toyota", "Honda", "Ford", "Hyundai",
            "Nissan", "Kia", "BMW",
            "Mercedes", "Audi", "Lexus"
        ]
    )

    year = st.number_input(
        "Year",
        min_value=2010,
        max_value=2025,
        value=2020
    )

    mileage = st.number_input(
        "Mileage",
        min_value=0,
        max_value=500000,
        value=50000
    )


with col2:
    model_name = st.number_input(
        "Model Encoded Value",
        min_value=0,
        max_value=100,
        value=1
    )

    engine_size = st.number_input(
        "Engine Size",
        min_value=1.0,
        max_value=10.0,
        value=2.0
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "Hybrid", "Electric"]
    )


with col3:
    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic"]
    )

    owner_count = st.selectbox(
        "Owner Count",
        [1, 2, 3, 4]
    )


# =========================
# ENCODING
# =========================

brand_map = {
    "Toyota": 0,
    "Honda": 1,
    "Ford": 2,
    "Hyundai": 3,
    "Nissan": 4,
    "Kia": 5,
    "BMW": 6,
    "Mercedes": 7,
    "Audi": 8,
    "Lexus": 9
}

fuel_map = {
    "Petrol": 0,
    "Diesel": 1,
    "Hybrid": 2,
    "Electric": 3
}

transmission_map = {
    "Manual": 0,
    "Automatic": 1
}


# =========================
# CREATE INPUT DATA
# =========================

input_data = pd.DataFrame({
    "Brand": [brand_map[brand]],
    "Model": [model_name],
    "Year": [year],
    "Engine_Size": [engine_size],
    "Mileage": [mileage],
    "Fuel_Type": [fuel_map[fuel_type]],
    "Transmission": [transmission_map[transmission]],
    "Owner_Count": [owner_count]
})


# =========================
# PREDICTION
# =========================

st.divider()

if st.button("🚗 Predict Car Price", use_container_width=True):

    prediction = model.predict(input_data)[0]

    st.success(
        f"💰 Estimated Car Price: ₦{prediction:,.2f}"
    )


# =========================
# FOOTER
# =========================

st.divider()

st.caption("Car Price Prediction System | Nitech Academy")

