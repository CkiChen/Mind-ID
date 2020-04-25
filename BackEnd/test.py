#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:28:40 2020

@author: jatin
"""

import numpy as np

db = np.load('Res/dataset.npy',allow_pickle='TRUE')

print(db)

x = np.load('Res/Users.npy',allow_pickle='TRUE').item()

print(x)


   
 