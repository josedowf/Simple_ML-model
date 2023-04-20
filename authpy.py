import json
from kaggle.api.kaggle_api_extended import KaggleApi


# auth function for Kaggle
def auth_kaggle():
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()
    return kaggle_api


# read credentials from creds.json file
def read_creds(filename):
    # Read JSON file to load credentials.
    # Store API credentials in a safe place.
    # If you use Git, make sure to add the file to .gitignore
    with open(filename) as f:
        creds = json.load(f)
    return creds


# test if Kaggle api is working
if __name__ == '__main__':
    api_kaggle = auth_kaggle()

    # Try auth access
    try:
        api_kaggle.authenticate()
        print('Successful Kaggle Authentication')
    except Exception as error:
        print('Failed Kaggle authentication')
        print(error)
