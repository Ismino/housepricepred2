import streamlit as st
import pandas as pd
from datetime import date
from src.data_management import load_housing_data, load_heritage_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_price, predict_inherited_house_price

# Function to load pipelines
def load_pipeline(pkl_filename):
    return load_pkl_file(pkl_filename)

# Define the function to draw input widgets and collect user input
def DrawInputsWidgets():
    try:
        df = load_housing_data()
        
        percentageMin, percentageMax = 0.4, 2.0
        X_live = pd.DataFrame([], index=[0])

        col1, col2, col3, col4, col5, col6 = st.beta_columns(6)

        with col1:
            feature = "TotalBsmtSF"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        with col2:
            feature = "GarageArea"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        with col3:
            feature = "YearBuilt"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()),
                max_value=int(df[feature].max()),
                value=int(df[feature].median()),
                step=1
            )

        with col4:
            feature = "2ndFlrSF"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        with col5:
            feature = "KitchenQual"
            X_live[feature] = st.selectbox(
                label=feature,
                options=["Ex", "Gd", "TA", "Fa", "Po"],
                index=2  # Default to 'TA'
            )

        with col6:
            feature = "YearRemodAdd"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()),
                max_value=int(df[feature].max()),
                value=int(df[feature].median()),
                step=1
            )

        return X_live

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Update the predict_price function to use both pipelines
def predict_price(X_live, preprocessing_pipeline, model_pipeline):
    # Apply preprocessing
    X_preprocessed = preprocessing_pipeline.transform(X_live)
    
    # Make predictions with the model pipeline
    price_prediction = model_pipeline.predict(X_preprocessed)
    
    return price_prediction

# Streamlit interface function
def page_predict_price_body():
    # Load both pipelines
    preprocessing_pipeline = load_pipeline("path/to/preprocessing_pipeline.pkl")
    model_pipeline = load_pipeline("path/to/model_pipeline.pkl")

    st.write("### Predicting sales price of inherited houses (BR2)")
    st.info(
       "* **BR2** - The client is interested in predicting the house sale prices from her 4 inherited houses,"
       " and any other house in Ames, Iowa."
    )

    try:
        st.write("###### Predicted sales price of 4 inherited houses")
        st.write("* See PredictedSalePrice column in the table below.")

        X_inherited = load_heritage_data()
        # Implement logic for predicting inherited houses here

    except Exception as e:
        st.error(f"An error occurred: {e}")

    st.write("### House Price Predictor Interface (BR2)")
    st.write("#### Do you want to predict the sale price of another house?")
    st.write("Provide the correct values of the following attributes and click on the 'Predict Sale Price' button.")
    
    X_live = DrawInputsWidgets()

    if X_live is not None:
        if st.button("Predict Sale Price"):
            try:
                # Pass both pipelines to the prediction function
                price_prediction = predict_price(X_live, preprocessing_pipeline, model_pipeline)
                st.success(f"Predicted Sale Price: ${price_prediction[0]:,.2f}")
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    page_predict_price_body()
