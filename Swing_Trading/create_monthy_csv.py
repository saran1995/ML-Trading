import os
import csv
from datetime import datetime
from natsort import natsorted
import pandas as pd
import numpy as np
from pathlib import Path

data = list
class Monthly_CSV:
    def __init__(self):
        self.current_date = datetime.today()
        self.month = self.current_date.month
        self.year = self.current_date.year
        self.file_path = os.path.join(os.getcwd(),
                                      'bhavcopy',f'{self.year}-{self.month}')
        file = natsorted(os.listdir(self.file_path))[0]
        df = pd.read_csv(os.path.join(self.file_path, file))
        self.stocks_names  = df[df['SERIES'] == 'EQ']
    def create_csv(self):
        new_data = pd.DataFrame()
        for stocks in self.stocks_names['SYMBOL']:
            print(stocks)

            for file in natsorted(os.listdir(self.file_path)):
                df = pd.read_csv(os.path.join(self.file_path, file))
                #     new_a = pd.DataFrame()
                x = df[df['SYMBOL'] == stocks]
                new_data = new_data.append(x)
            # print(new_data)
            file_path = os.path.join(os.getcwd(), 'monthly_csv',f'{self.year}-{self.month}', f'{stocks}.csv')
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            new_data.to_csv(file_path)
            new_data = pd.DataFrame()
if __name__ == '__main__':
    monthly = Monthly_CSV()
    monthly.create_csv()