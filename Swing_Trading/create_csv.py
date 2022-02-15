import os
import csv
from natsort import natsorted
import pandas as pd
import datetime
import numpy as np

data = list
a = pd.DataFrame()
file_path = os.path.join(os.getcwd(), 'csvs/new_csv/')
for file in natsorted(os.listdir(file_path)):
    # with open(os.path.join(os.getcwd(),'csvs', file), 'r') as read_file:
    #     csv_file = csv.reader(read_file)
    #     d = dict(filter(None, csv_file))
    #     print(d)
    df = pd.read_csv(os.path.join(file_path, file))
    #     df = df[df['SERIES'] == 'EQ']

    x = df[df['SERIES'] == 'EQ']
    #     x = df[df['SYMBOL'] == '3PLAND']
    #     print(type(x))
    break
for stocks in x['SYMBOL']:
    print(stocks)
    new_data = pd.DataFrame()
    for file in natsorted(os.listdir('csvs/new_csv/')):
        df = pd.read_csv(os.path.join(os.getcwd(), 'csvs/new_csv/', file))
        #     new_a = pd.DataFrame()
        x = df[df['SYMBOL'] == stocks]
        new_data = new_data.append(x)
    print(new_data)
    new_data.to_csv(os.path.join(os.getcwd(), 'stock_csv/Dec', f'{stocks}.csv'))