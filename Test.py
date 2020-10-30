# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:56:04 2020

@author: User
"""
from tda.auth import easy_client
from tda.client import Client
#from selenium import webdriver
import os

cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

#driver = webdriver.Chrome(executable_path ="D:\Code\chromedriver\chromedriver.exe" )

'''client = client_from_login_flow(
                    webdriver = driver,
                    api_key = 'ORAGFW4LIDGYCA8CSZAC2MGZGPTBECBG',
                    redirect_url = 'https://localhost',
                    token_path = 'D:\\TDA_steamer\\token.pickle')
'''

                    
client = easy_client(
        api_key='ORAGFW4LIDGYCA8CSZAC2MGZGPTBECBG',
        redirect_uri='https://localhost',
        token_path='D:\\TDA_steamer\\token.pickle')

resp = client.get_price_history('AAPL',
        period_type=Client.PriceHistory.PeriodType.YEAR,
        period=Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=Client.PriceHistory.FrequencyType.DAILY,
        frequency=Client.PriceHistory.Frequency.DAILY)
assert resp.ok
history = resp.json()