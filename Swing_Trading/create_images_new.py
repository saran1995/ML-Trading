import traceback
from datetime import datetime
import matplotlib.pyplot as plt
import mplfinance as mpf
import os
from pathlib import Path
from dateutil import relativedelta
import pandas as pd
window = 20
no_of_std = 2
class CreateImages:
    def __init__(self):
        self.current_date = datetime.today()
        self.month = self.current_date.month
        self.year = self.current_date.year
        self.last_month = (self.current_date -  relativedelta.relativedelta(months=1))
        self.second_last_month = (self.current_date - relativedelta.relativedelta(months=2))
    def plot_images(self):

        stocks_path = os.path.join(os.getcwd(), 'monthly_csv',f'{self.year}-{self.month}')
        for csv in os.listdir(stocks_path):
            try:
                print(csv)
                current = pd.read_csv(os.path.join(os.getcwd(), 'monthly_csv',f'{self.year}-{self.month}', csv))
                last = pd.read_csv(os.path.join(os.getcwd(), 'monthly_csv',
                                                f'{self.last_month.year}-{self.last_month.month}',csv))
                second_last = pd.read_csv(os.path.join(os.getcwd(), 'monthly_csv',
                                                f'{self.second_last_month.year}-{self.second_last_month.month}',csv))
                frames = [current, last, second_last]
                new_data = pd.concat(frames)
                x = new_data[['TIMESTAMP', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'PREVCLOSE', 'TOTTRDVAL']]
                x['TIMESTAMP'] = pd.to_datetime(x['TIMESTAMP'])
                x.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
                x = x.sort_values(by='Date')
                x = x.set_index('Date')
                rolling_mean = x['Close'].rolling(window=20).mean()
                rolling_std = x['Close'].rolling(window=20).std()
                rolling_vol = x['Volume'].rolling(window=20).mean()
                x['Rolling Mean'] = rolling_mean
                x['Bollinger High'] = rolling_mean + (rolling_std * no_of_std)
                x['Bollinger Low'] = rolling_mean + (rolling_std * no_of_std)
                x['Rolling Vol'] = rolling_vol
                price_latest = x.iloc[-1]
                if price_latest['Adj Close'] > price_latest['Close']:
                    filename = os.path.join(os.getcwd(), 'stock_image',
                                            f"{self.year}-{self.month}", f"{self.current_date.day}", 'Low')

                    # filename = os.path.join(os.getcwd(), 'stock_image/Feb/Low', csv.split('.')[0] + '.png')
                elif price_latest['Adj Close'] < price_latest['Close']:
                    filename = os.path.join(os.getcwd(), 'stock_image',
                                            f"{self.year}-{self.month}", f"{self.current_date.day}", 'High')

                filename_ = Path(filename)
                filename_.mkdir(parents=True, exist_ok=True)
                filename =os.path.join(filename, csv.split('.')[0] + '.png')
                new_plot = mpf.plot(x, type='candle', style='charles',volume=True, savefig=filename,mav=(20))

            except Exception:
                print(traceback.print_exc())

if __name__ == '__main__':
    create_image = CreateImages()
    create_image.plot_images()