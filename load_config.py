# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:37:34 2020

@author: User
"""

import json

def loadConfig(filePath):
        with open(filePath,'r') as fp:
            data = json.load(fp)
        return data