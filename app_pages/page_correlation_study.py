import streamlit as st
from src.data_management import load_housing_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
import numpy as np

# Set the style for seaborn plots
sns.set_style("whitegrid")

# Define global variables for repeated use
VARS_TO_STUDY = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'KitchenQual', 'MasVnrArea', 'OpenPorchSF', 'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']
TARGET_VAR = 'SalePrice'

def page_correlation_study_body():
    """
    Display correlated features and options to show various visualizations.
    """
    st.title("Housing Prices Correlation Study")
    
    # Load and display dataset information
    df = load_housing_data()
    display_dataset_info(df)

    # Correlation Study Summary
    display_study_summary()

    # Data Visualization
    if st.checkbox("Data Visualizations"):
        display_data_visualizations(df)

    # Heatmaps
    if st.checkbox("Show Heatmaps"):
        display_heatmaps(df)

def display_dataset_info(df):
    """
    Display basic information about the dataset.
    """
    st.info(
        f"* **Dataset Info** - The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
        "SalePrice is our target variable."
    )
    if st.checkbox("Inspect Housing Data"):
        st.write(df.head(10))

def display_study_summary():
    """
    Display summary of the correlation study.
    """
    st.write(f"* **Study Summary** - The most correlated variables with SalePrice are: {VARS_TO_STUDY}.")
    st.info(
        "Observations from the correlation analysis and heatmaps reveal relationships "
        "between house attributes and SalePrice. Some relationships are less clear at higher values."
    )

def display_data_visualizations(df):
    """
    Display various plots for the data.
    """
    st.write("#### Distribution of SalePrice")
    plot_target_hist(df, TARGET_VAR)

    st.write("#### House Prices per Variable")
    df_eda = df.filter(VARS_TO_STUDY + [TARGET_VAR])
    house_price_per_variable(df_eda)

def display_heatmaps(df):
    """
    Display heatmaps for Pearson, Spearman, and PPS correlations.
    """
    df_corr_pearson, df_corr_spearman, pps_matrix = calculate_corr_and_pps(df)
    display_heatmap(df_corr_pearson, 0.4, "Pearson Correlation")
    display_heatmap(df_corr_spearman, 0.4, "Spearman Correlation")
    display_heatmap(pps_matrix, 0.2, "PPS Matrix")

def plot_target_hist(df, target_var):
    """
    Function to plot a histogram of the target variable
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.histplot(data=df, x=target_var, kde=True)
    plt.title(f"Distribution of {target_var}", fontsize=20)       
    st.pyplot(fig)

def plot_reg(df, col, target_var):
    """
    Generate scatter plot
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.regplot(data=df, x=col, y=target_var, ci=None)
    plt.title(f"Regression plot of {target_var} against {col}", fontsize=20)        
    st.pyplot(fig)

def plot_line(df, col, target_var):
    """
    Generate line plot
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x=col, y=target_var)
    plt.title(f"Line plot of {target_var} against {col}", fontsize=20)        
    st.pyplot(fig)

def plot_box(df, col, target_var):
    """
    Generate box plot
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df, x=col, y=target_var) 
    plt.title(f"Box plot of {target_var} against {col}", fontsize=20)
    st.pyplot(fig)

def calculate_corr_and_pps(df):
    """
    Function to calculate correlations and pps.
    """
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")

    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    return df_corr_pearson, df_corr_spearman, pps_matrix

def display_heatmap(df, threshold, title):
    """
    Function to display a heatmap with given threshold and title.
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(df, annot=True, mask=np.abs(df) < threshold, cmap='viridis', ax=ax)
    plt.title(title)
    st.pyplot(fig)

def house_price_per_variable(df_eda):
    """
    Generate plots for each variable against SalePrice.
    """
    for col in VARS_TO_STUDY:
        if len(df_eda[col].unique()) <= 10:
            plot_box(df_eda, col, TARGET_VAR)
        else:
            if col in ['YearBuilt', 'YearRemodAdd']:
                plot_line(df_eda, col, TARGET_VAR)
            else:
                plot_reg(df_eda, col, TARGET_VAR)

# Main function calls
if __name__ == "__main__":
    page_correlation_study_body()