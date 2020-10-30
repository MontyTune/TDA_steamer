# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:46:41 2020

@author: User
"""


from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient
import math


import asyncio
import json


def loadConfig(filePath):
    with open(filePath,'r') as fp:
        data = json.load(fp)
    return data

"""
def handle_messages(msg):
    print(json.dumps(msg, indent=4))
    last_price = msg["content"]['LAST_PRICE']
    
"""

config = loadConfig("D:\\TDA_steamer\\config.json")
print(config['Stream']['redirect_url'],config['Stream']['token_path'])
client = easy_client(
        api_key=     config['Stream']['api_key'],
        redirect_uri=config['Stream']['redirect_url'],
        token_path=  config['Stream']['token_path'])
stream_client = StreamClient(client, account_id=config['Stream']['account_id'])

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)

    # Always add handlers before subscribing because many streams start sending
    # data immediately after success, and messages with no handlers are dropped.
    stream_client.add_level_one_futures_handler(
                            lambda msg: print(json.dumps(msg, indent=4)))
    
    await stream_client.level_one_futures_subs(['/ES'])

    while True:
        await stream_client.handle_message()

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = None


if loop and loop.is_running():
    print("Async event loop already running")
    tsk = loop.create_task(read_stream())
    tsk.add_done_callback(        
    lambda t: print(f'Task done: '                              # optional
                   f'{t.result()=} << return val of main()'))
          
else:
    print("Starting new event loop")          
    asyncio.run(read_stream())