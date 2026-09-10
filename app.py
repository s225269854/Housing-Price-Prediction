import streamlit as st
import pandas as pd
import joblib

# loading the trained model
model = joblib.load("ridge_housing_model.pkl")

# Setup page
st.set_page_config( page_title="Sydney House Price Predictor",
                   page_icon=":material/house:",
                   layout="centered")

st.title("Sydney Housing Price Predictor")

st.write("Enter the property details below and Estimate its sale price ")
st.write("(Using the trained Ridge Regression model.)")

# Mapping tables
property_type_mapping = {
    "Apartment / Unit": "Apartment_Unit",
    "House": "House",
    "Other": "Other",
}

month_mapping = {
    "January": 1, "February": 2, "March": 3, "April": 4,"May": 5, "June": 6,
    "July": 7,"August": 8,"September": 9, "October": 10, "November": 11, "December": 12,
}

# Input Form
st.subheader("Property Details")

with st.form("property_input_form"):
    # Location and Property type
    col1, col2 = st.columns(2)
    with col1:
        suburb = st.selectbox("Suburb", ["Liverpool", "Canterbury", "Parramatta"],
                              index=None, 
                              placeholder="Select a Suburb")
    with col2:
        property_type = st.selectbox("Property Type", ["Apartment / Unit", "House", "Other"],
                              index=None, 
                              placeholder="Select a Property Type")

    # Bedrooms, Bathrooms and Parking
    col3, col4, col5 = st.columns(3)
    with col3:
        bedrooms = st.number_input("Bedrooms", min_value=1, max_value=12, value=None, 
            step=1, 
            placeholder="Enter no. of Bedrooms")
    with col4:
        bathrooms = st.number_input("Bathrooms", min_value=1, max_value=6, value=None, 
            step=1, 
            placeholder="Enter no. of Bathrooms")
    with col5:
        parking = st.number_input("Parking Spaces", min_value=0, max_value=6, value=None, 
            step=1, 
            placeholder="Enter Parking Space")

    # Floor size and Sale Month
    col6, col7 = st.columns(2)
    with col6:
        floor_area = st.number_input("Floor Area (m²)", min_value=1.0, value=None, 
            step=5.0, 
            placeholder="Enter Floor Areas size")
    with col7:
        sale_month_name = st.selectbox("Sale Month", list(month_mapping.keys()),index=None, 
            placeholder="Select Sale Month")

    submit_button = st.form_submit_button("Estimate Price", type="primary")

# Prediction
if submit_button:
    model_data = pd.DataFrame({
        "Suburb": [suburb],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Parking": [parking],
        "Floor_Area_m2": [floor_area],
        "Property_Type_Grouped": [property_type_mapping[property_type]],
        "Sale_Month": [month_mapping[sale_month_name]]
    })

    price_prediction = model.predict(model_data)[0]

    st.subheader("The Estimated Sale Price:")
    st.success(f"${price_prediction:,.0f}")

    st.caption("This estimate is to only help with the decision"
               "and should not be considered as an accurate representation")
