# TDA_steamer

I made this to simply stream futures quotes. What you do from here is up to you.

pip install tda-api

First, go to TDA dev/api website and create an app. Copy the callback url in the config for the TDA app callback url if you intend to run this off your your own computer

Take the API key and your actual TDA account number and put then in the correct place in the config file. 
(I had to login to the actual TDA website to get my account number. Not the dev/api website.

Once you have the API Key,Acct #, and token created you should be able to run the TDA_streamer_class. Edit as you see fit.



Stream is as fast as this API allows via the express setting so should be under 500ms from the time the actual trade/quote happened.
