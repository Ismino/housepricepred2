import streamlit as st
import pandas as pd
import numpy as np
import joblib

# code taken from https://github.com/Amareteklay/heritage-housing-issues/tree/main
@st.cache(allow_output_mutation=True, ttl=3600)
def load_housing_data():
    df = pd.read_csv("outputs/datasets/collection/HousePrices.csv")
    return df


@st.cache(allow_output_mutation=True, ttl=3600)
def load_heritage_data():
    df_h = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df_h


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)