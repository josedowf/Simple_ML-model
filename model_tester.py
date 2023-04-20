import joblib

model = joblib.load('customer_predictor.joblib')
predictions = model.predict([[0, 25, 25000]])
print(predictions)


# Work on predicting and updating general file (Customers.csv) with predictions.
