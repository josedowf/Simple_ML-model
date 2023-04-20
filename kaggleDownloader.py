from authpy import auth_kaggle
from zipfile import ZipFile
import pandas as pd


# loads db from kaggle and creates dataframe with the wanted columns from db
def load_kaggle():
    kaggle_api = auth_kaggle()
    # retrieve database from Kaggle
    kaggle_api.dataset_download_file('datascientistanna/customers-dataset',
                                     file_name='Customers.csv')

    # unzip kaggle database and save in this directory.
    # use this when files come in ZIP format after download
    # zf = ZipFile('Customers.csv.zip')
    # zf.extractall()
    # zf.close()

    # load selected columns from db
    df = pd.read_csv('Customers.csv', index_col=None)
    return df

