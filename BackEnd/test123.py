#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:14:45 2020

@author: jatin
"""
USER_LIST = 'Res/Users.npy'
DB_PATH = 'Res/dataset.npy'
import numpy as np


database = np.load(DB_PATH,allow_pickle='TRUE')
userlist = np.load(USER_LIST,allow_pickle='TRUE').item()
    


X = [[]]

database = database[1:]

#yooy = database[14][7232]


rows,cols = len(database),len(database[0])


database[16][-1]



#arrr = database[0][:cols-1]
#arrr = np.reshape(arrr,(64,113))

   

X = []
y = []

for r in database:
    y.append(r[-1])
    arrr = r[:cols-1]
    arrr = np.reshape(arrr,(64,113))
    X.append(arrr)
    

from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.ensemble import RandomForestClassifier


from mne.decoding import Vectorizer

clf = make_pipeline(Vectorizer(),StandardScaler(),RandomForestClassifier())




clf.fit(X,y)


import processing as proc

fname = 'Test/Data/S001R12.edf' #>>> from sklearn.ensemble import RandomForestClassifier


raw = proc.Input(fname)
proc.SetMontage(raw)
new_raw,ica = proc.ApplyICA(raw)
epochs = proc.GetEpochs(new_raw,ica)

'''
from scipy.stats import trim_mean  
trim = lambda x: trim_mean(x, 0.1, axis=0)  
epoch_avg = epochs.average(method=trim) 
epoch_av_data = epoch_avg.data
Xtest = epoch_av_data
'''

Xtest = epochs.get_data()

pred = clf.predict(Xtest)

                   
