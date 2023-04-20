# Simple_ML-model
This repository is a simple machine learning program that downloads a database from Kaggle and preprocesses the data to proceed to split it and model for predictions. The program uses the "load_kaggle" function from the "kaggleDownloader" module to download the database, and then uses the Scikit-learn library to train a Decision Tree Classifier model on the data.

The data is split into training and testing sets using the "train_test_split" function, and the accuracy of the model is evaluated using the "accuracy_score" function. Finally, the trained model is saved using the "joblib" module.

This repository is intended to be a simple example of how to download a database from Kaggle and train a machine learning model on it, and is meant for educational purposes. It uses only a few libraries, making it easy to understand for those new to machine learning.

Note: This repository is intended for educational purposes only.