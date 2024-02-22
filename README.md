# Housing Price Predictor

* This project is made with ML-based tool designed to forecast the sale prices of residential properties. It operates by analyzing various attributes of houses, such as size, location, age, and other relevant features, to generate accurate price predictions. This solution offers a valuable resource for potential homebuyers, sellers, and real estate professionals, providing them with data-driven insights to inform their decisions in the housing market.

![Screenshot](/assets/images/summary.png)

You find the dashboard [on Heroku](https://pricepred2-1de5ea4de904.herokuapp.com/).

1. [Dataset Content](#1-dataset-content)
2. [Business Requirements](#2-business-requirements)
    - [Epics](#epics)
    - [User Stories](#user-stories)
3. [Hypotheses and validation](#3-hypotheses-and-validation)
4. [Rationale to map the business requirements to the Data Visualizations and ML tasks](#4-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
5. [ML Business Case](#5-ml-business-case)
6. [Dashboard Design](#6-dashboard-design)
   - [Page 1: Quick project summary](#page-1-quick-project-summary)
   - [Page 2: House prices Correlation Study](#page-2-house-prices-correlation-study)
   - [Page 3: Project hypotheses and validation](#3-hypotheses-and-validation)
   - [Page 4: Predict House price](#page-4-predict-house-price)
   - [Page 5: ML: House Price Predictor](#page-5-ml-house-price-predictor)
7. [Unfixed Bugs](#7-unfixed-bugs)
8. [Deployment](#8-deployment)
9. [Main Data Analysis and Machine Learning Libraries](#9-main-data-analysis-and-machine-learning-libraries)
10. [Credits](#10-credits)


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


## Business Requirements

As a trusted friend, I've been approached by a close friend who recently inherited properties from her great-grandfather in Ames, Iowa. She has tasked me with maximizing the sales value of these properties.

My friend is quite knowledgeable about property values in her own state and area, but she's concerned that this knowledge might not accurately apply to Ames. Aware of the regional differences in what makes a property desirable, she wisely decided to use a more data-driven approach. She's provided me with a public dataset containing property prices in Ames, which I'll use for this analysis.

There are two main objectives for this project:

* BR1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* BR2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

### Epics

* Information gathering and data collection.

* Data visualization, cleaning, and preparation.

* Model training, optimization and validation.

* Dashboard planning, designing, and development.

* Dashboard deployment and release.

### User Stories

* **US1:** As a customer I seek to identify the characteristics of a house that have the strongest relationship with its selling price. so that I can focus my forecasts on the most appropriate set of characteristics

* **US2:** As a costumer I can accurately forecast the sale prices of the houses I've acquired through bequest so that I can sell them for the maximum total price achievable.

* **US3:** As a costumer I can access a dashboard so that I can showcase the outcomes of the prediction within an application

* **US4:** As a technical user I can gain knowledge about the machine learning processes utilized for predicting sale prices so that I can comprehend the methodology of the model.

* **US5:** As a technical user, I can comprehend the efficacy of the model so that **I can verify the dependability of its predictions. 

* **US6:** As a user I can **use dynamic input tools that allow me to input up-to-date house information ** so that I can forecast the selling price

* **US7:** As a user I can access plots charts so that I can understand the correlations between the selling price and various house attributes.

* **US8:** As a user I can utilize established methods for data cleaning and preparation so that I can quickly estimate sale prices without starting from scratch.

* **US9:** As a user I can familiarize myself with the source and composition of the data that was used to train the model so that to understand the quality

* **US10:** As a role I can get insights into the initial assumptions of the project and the methods used for their verification so that I can gain a more comprehensive understanding of the factors influencing sale price


## Hypothesis and how to validate?
* Property Size Impact: My theory posits that the bigger a property is, the more it should fetch in the market. To test this, I'll analyze the relationship between house size metrics and their sale prices.

* Importance of Quality and Condition: I believe that the quality and condition of a house greatly affect its market value. Higher quality ratings, like those for the kitchen or the overall construction, should correlate with higher prices. I'll verify this by examining how these quality indicators relate to the sale price.

* Age and Renovation Influence: My assumption is that a property's age and any recent renovations play a crucial role in determining its value. I intend to investigate this by looking at the construction year, any recent remodels, and how these factors influence the property’s market value.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* For Business Requirement 1 (BR1): Focusing on Data Visualization and Correlation Analysis
   
   * I plan to delve into the sale prices in our dataset by creating histograms to visualize their distribution. This will provide a clearer understanding of the price range and spread.

   *  I'll conduct a detailed correlation analysis between various house attributes and their sale prices. This involves computing both Pearson and Spearman correlations to grasp both linear and rank correlations.

   * To further clarify these relationships, I'll graphically represent the key variables in relation to the sale prices of the houses, demonstrating how they are interconnected.

   * A dedicated notebook for correlation study will cover all aspects of this business requirement.

* For Business Requirement 2 (BR2): Implementing Regression Analysis
   
   * Given that our goal is to predict a continuous variable - the sale price, regression analysis will be my primary tool. Should the regression model underperform, I may consider reframing this as a classification challenge.

   * Understanding that not all house attributes equally impact sale price, my objective is to pinpoint those factors that have the most significant influence. Techniques like Principal Component Analysis (PCA) might be employed to identify these key variables.

   * A specialized notebook for modeling and evaluation, titled "Predict House Prices," will be used to fulfill this business requirement.


## ML Business Case

  ### Predict House Sales Price 
   
   #### Regression Model

   * To fulfill our second business requirement (BR2), our plan is to develop a Machine Learning (ML) model.

   * This model's purpose is to assist our client in estimating the sale prices of four specific inherited properties, as well as for any other comparable properties.

   * We've chosen to employ a regression model for this task, as our primary variable of interest – the sale price – is a numeric value

   * This task will be handled as a supervised learning problem focusing on a single dimension.
    
      * Our objective is to provide the client with valuable insights into the characteristics of houses that can potentially enhance their sale value. We've set specific performance targets for the model: achieving a minimum R2 score of 0.75 in both training and testing phases.

      * A prediction accuracy drop below 70% for any individual property will be considered a failure of the model. 

   * The model's output will be the projected sale price in U.S. dollars, based on the relevant house attributes.

   * The client has provided data on four inherited properties, and our model will predict both individual and cumulative sale prices for these.

   * Additionally, the model will support real-time predictions for other properties, allowing users to input key features for immediate price estimates. This dual functionality caters to the client’s current and future property valuation needs.

   * To avoid the potential inaccuracies of heuristic valuations, we are adopting a data-driven approach. The client’s local real estate knowledge may not accurately reflect the property values in Ames, Iowa, hence the reliance on a more analytical approach.
   * Our model, named 'HousePriceIssue' (House Price Issues), will utilize a public dataset from Ames, Iowa. This dataset comprises around 1,500 property listings with 22 features. During the data preparation phase, we'll exclude variables with significant missing data. Our focus will be on the 'SalePrice' as the target variable, with all other relevant features included in the analysis.    


## Dashboard Design

* 1. Quick project summary
* Key Terminology Explained:

* Sales Price: This term refers to the current market value of a house, determined by its specific features.
* Inherited House: A property acquired through inheritance, in this case, from the client's grandparents.
* Summed Price: The total value calculated by adding the sales prices of the four inherited properties.
* Project Data Source:

* The data for this project originates from a comprehensive real estate database in Ames, Iowa. This dataset is publicly accessible through Kaggle, courtesy of the Code Institute. It encompasses various house characteristics, including the sales price (our target variable), age indicators (like the year built and renovation year), spatial dimensions (areas of different house floors and garage), and evaluations of the house’s quality.
Business Objectives:

* The project is guided by two primary business objectives:
* Attribute Correlation Analysis (BR1): The client seeks insights into how different house characteristics influence their market value. This involves creating visual representations that highlight the relationships between house features and their sales prices.
* Price Prediction (BR2): The client aims to estimate the market value of four houses they have inherited, as well as other properties in Ames, Iowa. This entails using machine learning techniques to predict the potential sale prices based on house attributes.
![Screenshot](/assets/images/summary.png)

* 2. House prices Correlation Study (BR1)

* This section provides an interactive exploration into the key aspects of the correlation study, focusing on the relationship between house attributes and their sale prices:

* Business Objective Addressed:

* The primary focus of this section is to investigate the correlation between various house features and their sale prices. This analysis is fundamental to understanding which attributes significantly impact the value of a house.
Dataset Exploration Tools:

*An option to inspect the dataset is provided through a checkbox. This feature allows users to delve into the dataset details, offering a deeper understanding of the data used in the study.
* Correlation Findings Summary:

* A detailed list of findings is presented, highlighting the features that exhibit the strongest correlation with house sale prices. This summary provides a clear insight into which characteristics are most influential in determining a house's market value.
* Visual Correlation Analysis:

* Users can choose to view various plots illustrating the relationship between sale price and key features via a checkbox. This interactive section showcases:
The distribution of the target variable, sale price, through a histogram.
Regression plots linking sale price with each continuous numerical attribute.
Box plots depicting the relationship between sale price and categorical features.
Line graphs for analyzing sale price trends over time-related variables.
Comprehensive heatmaps, including Pearson and Spearman Correlation Heatmaps, along with Predictive Power Score (PPS) Heatmaps.
* Target Variable Examination:

* The target variable, SalePrice, is examined in detail using a histogram to understand its distribution. This analysis is crucial for grasping the range and common values of house prices in the dataset.
* Feature Relationship Analysis:

* Upon identifying the features most correlated with SalePrice, their relationships are analyzed using different types of plots:
* Box plots for categorical features.
* Scatter plots for continuous variables.
* Line plots for time-related attributes.
![Screenshot](/assets/images/pricecorr.png)

* 3. Hypotheses and validation

* The Significance of Size in Determining Property Value:

* Premise: A direct correlation exists between the size of a property and its market price, with larger properties commanding higher prices.
* Outcome: This theory holds true. Our data analysis revealed a consistent and moderate positive correlation between property size indicators and their sale prices.
Correlation Between Property Quality and Market Price:

* Theory: The hypothesis posits that the quality and condition of a property are critical determinants of its value, suggesting that properties with higher quality ratings should have higher sale prices.
* Conclusion: The hypothesis is validated. By analyzing the relationship between sale prices and quality metrics like kitchen and overall house conditions, we found a direct correlation, supporting the notion that higher quality equates to higher market value.
Influence of Age and Renovation on Property Value:

* Hypothesis: The age of a property and the recency of renovations are believed to significantly impact its market value, with newer or recently renovated properties expected to fetch higher prices.
* Verification: The hypothesis is corroborated. Examination of sale prices in relation to the year of construction and renovation history showed a moderate positive correlation, confirming that newer or updated properties tend to be valued higher in the market.
![Screenshot](/assets/images/hypothes.png)

* 4. Predict House price

* The client's objective is to accurately forecast the sale prices for four specific inherited properties, as well as for any additional houses located within Ames, Iowa. This section of the project is dedicated to achieving this goal:

* Display of Inherited Properties:

* This section showcases detailed information about the four inherited houses, including their key features. Alongside each property’s attributes, their anticipated sale prices, as predicted by our model, are displayed.
Cumulative Price Estimation:

* An informative section is included that presents the aggregate predicted value of all four inherited houses. This provides a comprehensive view of the total potential market value of the inherited properties.
User-Driven Price Prediction Tool:

* We have integrated a set of dynamic input widgets. These widgets enable users to input specific details about any house in Ames, Iowa, facilitating the prediction of its sale price in real-time.
Sale Price Prediction Activation:

* A prominently placed “Predict Sale Price” button is included. When clicked, this button feeds the user-provided house data into our Machine Learning pipeline. The system then processes this information to estimate the house's sale price, showcasing the power and versatility of our predictive model.
![Screenshot](/assets/images/predictpage1.png)
![Screenshot](/assets/images/predictpage2.png)

* 5. House Price Predictor, The ML machine

* This section offers a comprehensive view of the outcomes and insights following the training of our Machine Learning pipeline:

* Post-Training Insights:

* An in-depth analysis and summary of key takeaways derived after the pipeline's training phase. This encompasses the evaluation of the model's learning, adaptability, and overall effectiveness in price prediction.
* Pipeline Composition:

* A detailed breakdown of the various stages involved in the Machine Learning pipeline. 
* This includes data preprocessing steps, feature selection techniques, model training algorithms, and any optimization processes applied.
* Significance of Features:

* A dual-perspective presentation on feature importance:
* A descriptive list highlighting which features most significantly impact the model's predictions.
* A visual representation, such as a graph or chart, that illustrates the relative importance of each feature in the predictive model.
* Model Performance Metrics:

* A thorough presentation of the regression model's performance metrics. This section delves into the effectiveness of the model, discussing various measures such as accuracy, precision, recall, and any other relevant statistics that indicate the model’s predictive power and reliability.
![Screenshot](/assets/images/MLpredictlast.png)

## Unfixed Bugs
* There is no unfixed bugs that i know about

## Deployment
### Heroku

* The App live link is: https://pricepred2-1de5ea4de904.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Numpy: Integral for creating arrays, including those used in visualizing data correlations, such as masks for heatmaps.
* Pandas: Essential for transforming CSV files into DataFrames, enabling efficient data handling and manipulation.
* Scikit-learn: A cornerstone for building and fine-tuning the Machine Learning model. It provided tools for cross-validation and hyperparameter optimization, crucial for enhancing model accuracy.
* Matplotlib: Utilized for crafting various types of visualizations to analyze and present data insights.
* Seaborn: Complemented Matplotlib by offering advanced statistical graphing capabilities, like creating intricate heatmaps.
* Jupyter: Served as an interactive platform for executing the entire data science workflow — from data collection and preprocessing to model training and evaluation.
* Streamlit: Used to construct an interactive web dashboard, offering users a user-friendly interface for predicting house prices and displaying key information across multiple pages.
* ydata-profiling: Played a key role in initial data exploration, providing detailed insights into each dataset variable, which helped identify data cleaning requirements.
* PPScore: Offered a unique approach to assessing relationships between variable pairs in the dataset, regardless of their data types.
* Feature-engine: Vital for preparing the dataset for Machine Learning. It offered sophisticated tools for tasks like encoding and transforming variables as part of feature engineering.

## Credits 

* I give big credit to https://github.com/Code-Institute-Solutions/churnometer/tree/main and https://github.com/Amareteklay/heritage-housing-issues who i followed as an ex. Also some parts of the code are totally taken from them. 

### Content 

* The content was prod´vided from the kaggle dataset. 

### 

* I did this project in another repo at first but when i redid after getting it back from the assesment team it to fix my errors i didnt create a new kanban, I used my already created kanban. 