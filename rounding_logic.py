# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 01:30:58 2020

@author: User
"""



def myround(x, prec=2, base=10):
 
  round_up = round(base * round(float(x)/base),prec)
  #round_down = 
  return round_up

print(myround(3258))


#%%