import streamlit as st
from app_pages.multipages import MultiPage
from app_pages.page_correlation_study import page_correlation_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_price import page_predict_price_body
from app_pages.page_summary import page_summary_body
from app_pages.page_ML_predict_price import page_ml_predict_price_body

app = MultiPage(app_name= "Housing Price Predictor") # Create an instance of the app 


# load pages scripts
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Housing Prices Correlation Study", page_correlation_study_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Predict House Price", page_predict_price_body)
app.add_page("ML: House Price Predictor", page_ml_predict_price_body)


app.run() # Run the  app