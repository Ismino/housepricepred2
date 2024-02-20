import streamlit as st
import pandas as pd
from datetime import date
from src.data_management import load_housing_data, load_heritage_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_price, predict_inherited_house_price

def DrawInputsWidgets():
    try:
        df = load_housing_data()
        
        # Define the percentage range for the inputs
        percentageMin, percentageMax = 0.4, 2.0
        X_live = pd.DataFrame([], index=[0])

        # Define columns for Streamlit layout
        col1, col2, col3, col4, col5 = st.beta_columns(5)

        # Input for '2ndFlrSF'
        with col1:
            feature = "2ndFlrSF"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        # Input for 'GarageArea'
        with col2:
            feature = "GarageArea"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        # Input for 'LotArea'
        with col3:
            feature = "LotArea"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=100
            )

        # Input for 'TotalBsmtSF'
        with col4:
            feature = "TotalBsmtSF"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min()*percentageMin),
                max_value=int(df[feature].max()*percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        # Input for 'YearBuilt'
        with col5:
            feature = "YearBuilt"
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

def page_predict_price_body():
    version = 'v4'
    regression_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_price/{version}/regression_pipeline.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
                      .columns
                      .to_list())

    st.write("### Predicting sales price of inherited houses (BR2)")
    st.info(
       "* **BR2** - The client is interested in predicting the house sale prices from her 4 inherited houses,"
       " and any other house in Ames, Iowa."
    )

    try:
        st.write("###### Predicted sales price of 4 inherited houses")
        st.write("* See PredictedSalePrice column in the table below.")

        X_inherited = load_heritage_data()
        # Similar logic for predicting inherited houses
        # ...

    except Exception as e:
        st.error(f"An error occurred: {e}")

    st.write("### House Price Predictor Interface (BR2)")
    st.write("#### Do you want to predict sale price of another house?")
    st.write("Provide the correct values of the following attributes and click on the 'Predict Sale Price' button.")
    
    X_live = DrawInputsWidgets()

    if X_live is not None:
        if st.button("Predict Sale Price"):
            try:
                price_prediction = predict_price(X_live, house_features, regression_pipe)
                # Display the prediction result
                # ...
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    page_predict_price_body()