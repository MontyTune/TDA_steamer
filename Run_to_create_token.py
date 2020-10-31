# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:56:04 2020

@author: Monty
"""
from tda.auth import easy_client
from tda.client import Client
from tda.auth import client_from_login_flow
import os
from load_config import loadConfig


'''Make sure you have install Chrome Driver or firefox driver and pip install selenium

'''



def make_webdriver():
    #Import selenium here because its slow to import
    from selenium import webdriver   
    
    driver = webdriver.Chrome(executable_path ="D:\Code\chromedriver\chromedriver.exe" )  #<---- Change this. Can call function without executable path if chromedriver
    return driver                                                                         #                   is in path



 
#Get all the relavent path's for your current config.son and future token.pickle
script_dir = os.path.dirname(os.path.abspath(__file__))
abs_file_path = os.path.join(script_dir, "config.json")          
token_path_ = os.path.join(script_dir, "token.pickle")  
config = loadConfig(abs_file_path)


#Create a new client. This will create your pickle 
client = client_from_login_flow(
                    webdriver = make_webdriver(),
                    api_key=     config['Stream']['api_key'],
                    redirect_uri=config['Stream']['redirect_url'],
                    token_path=  token_path_)



'''
This is to check your login/token is good and you can pull historical data


                    
client = easy_client(
        api_key=config['Stream']['api_key'],
        redirect_uri=config['Stream']['redirect_url'],
        token_path=  token_path_ )

resp = client.get_price_history('AAPL',
        period_type=Client.PriceHistory.PeriodType.YEAR,
        period=Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=Client.PriceHistory.FrequencyType.DAILY,
        frequency=Client.PriceHistory.Frequency.DAILY)
assert resp.ok
history = resp.json()
print(history)
'''


