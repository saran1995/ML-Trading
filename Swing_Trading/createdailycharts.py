import os
import create_images_new
import create_monthy_csv
import bhavcopy



class Trigger_data_aquistion:
    def __init__(self):
        self.download_bhavcopy = bhavcopy.GetBhavCopy()
        print('getting Data')
        self.download_bhavcopy.download_prices()
        self.image_creation = create_images_new.CreateImages()
        self.monthly_csv = create_monthy_csv.Monthly_CSV()


    def get_data(self):
        # print('getting Data')
        # self.download_bhavcopy.download_prices()
        print('creating monthly csv')
        self.monthly_csv.create_csv()
        print('create images')
        self.image_creation.plot_images()

if __name__ == '__main__':
    trigger = Trigger_data_aquistion()
    trigger.get_data()


