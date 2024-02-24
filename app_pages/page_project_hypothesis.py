import streamlit as st

# This function sets up a page in the Streamlit app that discusses the project's hypotheses and their outcomes.
def page_project_hypothesis_body():

    st.write("## Insights on Property Features and Their Impact on Sale Prices: The Hypoteses and outcome")

    # Insights derived from the correlation study in the "03 - SalesPriceCorrelationStudy" notebook 
    # The markdown method is used to display the insights in a formatted manner. 
    # Each insight is presented as a hypothesis followed by the findings from the data analysis.
    st.markdown(
       """
       **Insight 1: The Influence of Property Size.**  
       _Does size influence property value?_ Our analysis aimed to uncover the relationship between property size and sale price.
       * **Finding:** Indeed, our data analysis confirms this relationship. Property size attributes, such as area measurements, demonstrate a clear positive correlation with sale prices.
       
      **Insight 2: The Influence of Garage Size.**  
       _Does the size of garage influence property value?_ Our analysis aimed to uncover the relationship between garage size and sale price.
       * **Finding:** Indeed, our data analysis confirms this relationship. Property garage size demonstrate a clear positive correlation with sale prices and is one of the important features.


       **Insight 3: The Role of Quality in Valuation.**  
       _How does quality rating affect a property’s market value?_ We looked into the correlation between the house's condition and quality ratings with its market value.
       * **Finding:** Our data supports the idea that better quality and condition ratings are associated with higher sale prices, affirming the significance of quality in property valuation.

       **Insight 4: The Value of Recency and Age.**  
       _Is there a significant connection between a property's age or its recent renovations and its market value?_ We explored this by analyzing the correlation between sale prices and the property's construction year or recent renovations.
       * **Finding:** The data revealed a moderate positive correlation between sale price and newer properties or those with recent remodels, underscoring the importance of property age and upgrades.
       """
    )