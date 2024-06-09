import os
import pandas as pd

from HAEstates import app

DATASET_PATH = os.path.join(app.root_path, 'dataset', 'real_estate_data_chicago.csv')

df = pd.read_csv(DATASET_PATH, sep=',')
df = df.fillna('')