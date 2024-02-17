import streamlit as st
import pandas as pd
from datetime import date
from src.data_management import load_housing_data, load_heritage_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_price, predict_inherited_house_price

def DrawInputsWidgets():
    try:
        df = load_housing_data()
        df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF']
        
        percentageMin, percentageMax = 0.4, 2.0
        X_live = pd.DataFrame([], index=[0]) 

        col1, col2, col3, col4 = st.columns(4)
        col5, col6, col7, col8 = st.columns(4)

        with col1:
            feature = "GarageArea"
            st_widget = st.number_input(
                label= feature,
                min_value= int(df[feature].min()*percentageMin), 
                max_value= int(df[feature].max()*percentageMax),
                value= int(df[feature].median()), 
                step= 50
            )
            X_live[feature] = st_widget

        # Add similar blocks for other features here
        # ...

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