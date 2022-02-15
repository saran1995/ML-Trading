import traceback

import matplotlib.pyplot as plt
import mplfinance as mpf
import os
import pandas as pd
window = 20
no_of_std = 2
for csv in os.listdir('stock_csv/Jan/'):
    try:
        print(csv)
        a = pd.read_csv(os.path.join(os.getcwd(), 'stock_csv/Jan/', csv))
        b = pd.read_csv(os.path.join(os.getcwd(), 'stock_csv/Feb/', csv))
        frames = [a, b]
        a = pd.concat(frames)
        x = a[['TIMESTAMP', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'PREVCLOSE', 'TOTTRDVAL']]
        x['TIMESTAMP'] = pd.to_datetime(x['TIMESTAMP'])
        x.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        x = x.set_index('Date')
        rolling_mean = x['Close'].rolling(window=20).mean()
        rolling_std = x['Close'].rolling(window=20).std()
        rolling_vol = x['Volume'].rolling(window=20).mean()
        # x['MA20'] = x['Close'].rolling(window=20).mean()
        # x['20dSTD'] = x['Close'].rolling(window=20).std()
        #
        # x['Upper'] = x['MA20'] + (x['20dSTD'] * 2)
        # x['Lower'] = x['MA20'] - (x['20dSTD'] * 2)
        x['Rolling Mean'] = rolling_mean
        x['Bollinger High'] = rolling_mean + (rolling_std * no_of_std)
        x['Bollinger Low'] = rolling_mean + (rolling_std * no_of_std)
        x['Rolling Vol'] = rolling_vol
        filename = os.path.join(os.getcwd(), 'stock_image/Feb/', csv.split('.')[0] + '.png')
        filename_new = os.path.join(os.getcwd(), 'stock_image/new/', csv.split('.')[0] + '.png')
        fig, ax = plt.subplots()
        date = x.index
        plt.plot(x.index, rolling_mean, 'k-')
        plt.fill_between(date,x['Bollinger Low'],x['Bollinger High'],color = '#eeeee4')
        plt.title('b')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.savefig(filename_new)
        new_plot = mpf.plot(x, type='candle', volume=True, savefig=filename,mav=(10, 20))
        # new_plot.fill_between(date, x['Bollinger Low'], x['Bollinger High'], color='#eeeee4')

    except Exception:
        print(traceback.print_exc())