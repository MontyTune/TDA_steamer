# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:46:41 2020

@author: Monty
"""


from tda.auth import easy_client
from tda.streaming import StreamClient
import pprint
import os
import asyncio
from load_config import loadConfig





class MySteamConsumer:    
    def __init__(self, api_key, account_id, token_path, config, queue_size = 1):
        self.api_key = api_key
        self.account_id = account_id
        self.token_path = token_path
        self.tda_client = None
        self.stream_client = None
        self.config = config
        self.symbols = [
            "/ES"
            ]
        self.queue = asyncio.Queue(queue_size)
            
    def initialize(self):    
        self.tda_client = easy_client(
            api_key=     self.config['Stream']['api_key'],
            redirect_uri=self.config['Stream']['redirect_url'],
            token_path=  self.config['Stream']['token_path'])
        
        self.stream_client = StreamClient(self.tda_client,account_id = self.account_id)
        
        
        # The streaming client wants you to add a handler for every service type
        self.stream_client.add_level_one_futures_handler(self.handle_futures_quotes)   
        
                
    async def stream(self):
        await self.stream_client.login() # Log into the streaming service
        await self.stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)        
        await self.stream_client.level_one_futures_subs(self.symbols)                
        
        asyncio.ensure_future(self.handle_queue())
        
        while True:
            await self.stream_client.handle_message()
                        
    async def handle_futures_quotes(self, msg):
        """
        This is where we take msgs from the streaming client and put them on a
        queue for later consumption. We use a queue to prevent us from wasting
        resources processing old data, and falling behind.
        """
        
        # if the queue is full, make room
        if self.queue.full():
            await self.queue.get()
        await self.queue.put(msg)

    async def handle_queue(self):
        """
        Here we pull messages off the queue and process them.
        """
        while True:
            msg = await self.queue.get()
            pprint.pprint(msg)
            
async def main():
    """
    Create and instantiate the consumer, and start the stream
    """    
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_file_path = os.path.join(script_dir, "config.json")
    token_path = os.path.join(script_dir, "token.pickle")             
    config_json = loadConfig(abs_file_path)
    
    consumer = MySteamConsumer(config_json['Stream']['api_key'], config_json['Stream']['account_id'], token_path, config_json)
    consumer.initialize()
    await consumer.stream()

if __name__ == '__main__':    
    asyncio.run(main())
    
    
    
    
    
    