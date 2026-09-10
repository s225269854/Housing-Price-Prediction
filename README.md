# Sydney Housing Price Prediction and Decision Support System

This repository contains the supporting files for the SIT720 8.1D Machine Learning Mini Project.

The project develops an end-to-end machine learning workflow for predicting property sale prices across Liverpool, Canterbury and Parramatta. The final Ridge Regression pipeline is deployed through a Streamlit web application.

## Repository Contents

- `SIT720_8.1D_Assignment.ipynb` – complete machine learning workflow and analysis
- `House_Sold_Listings.csv` – manually collected housing dataset
- `app.py` – Streamlit web application
- `ridge_housing_model.pkl` – trained Ridge Regression pipeline
- `requirements.txt` – required Python packages

## Run the Application Locally

Install the required packages:

pip install -r requirements.txt

Then run:

streamlit run app.py
