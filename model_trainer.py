from kaggleDownloader import load_kaggle
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# import dataset from kaggle and store dataframe in variable 'Customers_data'
Customers_data = load_kaggle()

# Make the gender column alternate numbers (0 and 1) to make it easier to manipulate
Customers_data['Gender'].replace('Female', 0, inplace=True)
Customers_data['Gender'].replace('Male', 1, inplace=True)

# takes all rows that have a null value and stores them
sample_data = Customers_data[Customers_data.isnull().any(axis=1)]

# now we drop all rows with a null value, so we can just have a
# table with full elements for the model to train on
Customers_data.dropna(inplace=True)


# structure both sets of data.'X' contains the info the model uses to LEARN
# while 'y' refers to what we are trying to predict.
# the columns left to train on are: 'Gender', 'Age' and 'Annual Income ($)'
X = Customers_data.drop(columns=['CustomerID', 'Spending Score (1-100)',
                                 'Work Experience', 'Family Size', 'Profession'])
y = Customers_data['Profession']


# function that runs the model 100 times and throws a mean and stdv of how accurate the model is
def accuracy_tester(input_set, output_set):
    # Create an empty list to store the accuracy scores
    accuracy_scores = []

    # Loop over the range of 10 to get 10 different accuracy scores
    for i in range(100):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)

        # Fit the model on the training data
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        # Make predictions on the testing data
        predictions = model.predict(X_test)

        # Calculate the accuracy score for the predictions and append it to the list
        accuracy_scores.append(accuracy_score(y_test, predictions))

        # when the loop reaches 100 tests, the loop breaks and begins calculating results
        if i == 99:
            # Round the numbers to 2 decimal places
            rounded_acc_scores = [round(num, 2) for num in accuracy_scores]
            # Print the list of accuracy scores
            print(rounded_acc_scores)

            # Calculate and print the mean and standard deviation of the accuracy scores
            print(f"Mean accuracy score: {np.mean(accuracy_scores).round(2)}")
            print(f"Standard deviation of accuracy scores: {np.std(accuracy_scores).round(2)}")


# accuracy_tester(X, y)

model = DecisionTreeClassifier()
model.fit(X, y)

# store model when modified in order to reuse it later in the model_tester.py file
joblib.dump(model, 'customer_predictor.joblib')





