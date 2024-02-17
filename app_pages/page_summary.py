import streamlit as st

def page_summary_body():
    """
    Showcases an overview of the project with key insights and dataset details.
    """
    st.title("Housing Insights")

    st.markdown("""
        #### Key Terminology
        - **Sales Price**: The market valuation of a house in USD, considering its various features.
        - **Inherited Houses**: Properties passed down from the client's grandparents.
        - **Summed Price**: Aggregate of the projected sales values for the four inherited properties.
    """)

    st.markdown("""
        #### Data Exploration
        * We leverage a detailed dataset from Ames, Iowa's housing market, provided by [Kaggle's Code Institute](https://www.kaggle.com/codeinstitute/housing-prices-data).
        * It encompasses a wide array of house characteristics including age, size, and quality ratings, alongside their respective sales prices.
    """)

    st.markdown("""
        *Interested in a deeper exploration? Delve into our comprehensive [Project Documentation]().*
    """)

    st.markdown("""
        #### Project Goals
        Our analysis revolves around two primary objectives:
        1. **Correlation Analysis (BR1)**: Unraveling the relationship between house features and their sales prices, aimed at visualizing how various attributes influence market value.
        2. **Price Prediction (BR2)**: Estimating the value of four specific inherited properties and providing a predictive model for Ames' real estate market.
    """)

    st.markdown("""
        ##### Discoveries & Predictions
        Dive into our findings on the correlation between property attributes and their market value, and explore our predictive model's insights on property valuation in Ames.
    """)

    # Optionally, you can add more sections or interactive elements here

# Main function to run the app
if __name__ == "__main__":
    page_summary_body()