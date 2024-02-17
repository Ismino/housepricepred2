import streamlit as st

def predict_price(X_live, house_features, price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_price = X_live.filter(house_features)

	# predict
	price_prediction = price_pipeline.predict(X_live_price)
	# st.write(tenure_prediction_proba)

	# create a logic to display the results
	
	statement = (
			f"* The value of your house is: **${round(price_prediction[0])}**.\n\n"
			)
	
	st.write(statement)


def predict_inherited_house_price(X_inherited, house_features, price_pipeline):

	# From inherited houses data, subset features related to this pipeline
	X_inherited_price = X_inherited.filter(house_features)

	# predict

	price_prediction_inherited = price_pipeline.predict(X_inherited_price)
	# st.write(tenure_prediction_proba)
	
	this_price = price_prediction_inherited[0]
	# create a logic to display the results
	
	return this_price