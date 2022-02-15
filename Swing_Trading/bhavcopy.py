from datetime import date, datetime
from jugaad_data.nse import bhavcopy_save
import pandas as pd
import calendar
from jugaad_data.holidays import holidays
from random import randint
import time, os

class GetBhavCopy():
    def __init__(self):
        self.current_date = datetime.today()

        self.month = self.current_date.month
        self.year = self.current_date.year
        self.month_date_range = calendar.monthrange(self.year,self.month )
        self.date_range = pd.bdate_range(start=f'{self.month}/{self.month_date_range[0]}/{self.year}',
                                         end=f'{self.month}/{self.month_date_range[1]}/{self.year}',
                                    freq='C', holidays=holidays(self.year, self.month))

        self.savepath = os.path.join(os.getcwd(), 'bhavcopy', f'{self.year}-{self.month}')
        if not os.path.exists(self.savepath):
            os.mkdir(self.savepath)
    def download_prices(self):
        dates_list = [x.date() for x in self.date_range]

        for dates in dates_list:
            print(dates)
            if dates.day > self.current_date.day:
                print('Upcoming event')
                continue
            try:
                bhavcopy_save(dates, self.savepath)
                time.sleep(randint(1, 4))  # adding random delay of 1-4 seconds
            except Exception as e:
                time.sleep(10)  # stop program for 10 seconds and try again.
                try:
                    bhavcopy_save(dates, self.savepath)
                    time.sleep(randint(1, 4))
                except Exception as e:
                    print(f'{dates}: File not Found')

if __name__ == '__main__':
    getbhav = GetBhavCopy()
    getbhav.download_prices()