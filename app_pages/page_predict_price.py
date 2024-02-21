import streamlit as st
import pandas as pd
from src.data_management import load_housing_data, load_heritage_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_price, predict_inherited_house_price

# Function to create input widgets for user to enter house features
def DrawInputsWidgets():
    try:
        df = load_housing_data() # Load the housing data
        
        # Define the percentage range for the inputs
        percentageMin, percentageMax = 0.4, 2.0
        X_live = pd.DataFrame([], index=[0])  #Initialize an empty DataFrame for user inputs

        # Define columns for Streamlit layout using a 3:1 ratio for column width
        col1, col2 = st.beta_columns([3, 1])
        col3, col4 = st.beta_columns([3, 1])
        col5, _ = st.beta_columns([3, 1])

        # Creating input widgets for each feature with predefined steps and range
        # Input for '2ndFlrSF'
        with col1:
            feature = "2ndFlrSF"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min() * percentageMin),
                max_value=int(df[feature].max() * percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        # Input for 'GarageArea'
        with col2:
            feature = "GarageArea"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min() * percentageMin),
                max_value=int(df[feature].max() * percentageMax),
                value=int(df[feature].median()),
                step=50
            )

        # Input for 'LotArea'
        with col3:
            feature = "LotArea"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min() * percentageMin),
                max_value=int(df[feature].max() * percentageMax),
                value=int(df[feature].median()),
                step=100
            )

        # Input for 'TotalBsmtSF'
        with col4:
            feature = "TotalBsmtSF"
            X_live[feature] = st.number_input(
                label=feature,
                min_value=int(df[feature].min() * percentageMin),
                max_value=int(df[feature].max() * percentageMax),
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

        return X_live # Return the DataFrame with user inputs


    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Main function to display the prediction interface and show predictions
def page_predict_price_body():
    version = 'v4'
    regression_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_price/{version}/regression_pipeline.pkl")
    house_features = pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/X_train.csv").columns.to_list()
    
     # Displaying the purpose of the page
    st.write("### Predicting sales price of inherited houses (BR2)")
    st.info(
        "* **BR2** - The client is interested in predicting the house sale prices from her 4 inherited houses,"
        " and any other house in Ames, Iowa."
    )

    # Predict sales prices of inherited houses
    st.write("###### Predicted sales price of 4 inherited houses")
    st.write("* See PredictedSalePrice column in the table below.")

    X_inherited = load_heritage_data()
    X_inherited = X_inherited[['2ndFlrSF', 'GarageArea', 'LotArea', 'TotalBsmtSF', 'YearBuilt']]
    
     # Calculate and display predicted prices
    summed_price = 0
    predicted_sale_price = []
    for i in range(X_inherited.shape[0]):
        # Assuming predict_inherited_house_price returns a scalar value
        pprice = predict_inherited_house_price(X_inherited.iloc[[i,]], house_features, regression_pipe)
        predicted_sale_price.append(round(pprice, 2))  # Use pprice directly without indexing
        summed_price += pprice
    
    # Add the predicted prices to the DataFrame and display it
    X_inherited['PredictedSalePrice'] = predicted_sale_price
    st.write(X_inherited.head())
    st.write(f"* Summed price of the 4 inherited houses: **${summed_price:,}**")
    st.write(f"* Features used for prediction: **{', '.join(X_inherited.columns.to_list()[:-1])}**.")
    st.write("The Machine Learning model successfully predicted the sale prices of the 4 inherited houses, and we were able to find the summed value of the properties in question.") 
    
    # Section for users to input features and predict prices for other houses
    st.write("### House Price Predictor Interface (BR2)")
    st.write("#### Do you want to predict sale price of another house?")
    st.write("Provide the correct values of the following attributes and click on the 'Predict Sale Price' button.")
    
    X_live = DrawInputsWidgets() # Create input widgets for user to enter features
    
    # Button to trigger prediction
    if X_live is not None:
        if st.button("Predict Sale Price"):
            try:
                price_prediction = predict_price(X_live, house_features, regression_pipe)
                # Display the prediction result
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    page_predict_price_body()
