
#64 x 113
import mne
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#%matplotlib qt


USER_LIST = 'Res/Users.npy'
DB_PATH = 'Res/dataset.npy'


def Input(fname):
    raw = mne.io.read_raw_edf(fname,preload=True)
    return raw
    
    

def SetMontage(raw):
    raw.filter(None, 50., h_trans_bandwidth='auto', filter_length='auto',
           phase='zero')
    for x in raw.ch_names:
        str = x.replace(".", "")
        raw.rename_channels(mapping={x:str})
    raw.filter(1, 40, n_jobs=2) 
    montage =  mne.channels.make_standard_montage('standard_1005')
    raw.set_montage(montage,match_case=False)

    

def ApplyPCA(raw,n): 
    dictionary = {"T2" : 100}
    eves = mne.events_from_annotations(raw,dictionary)
    events = eves[0] 
    events_ids = {"target/stimulus":100}
    epochs = mne.Epochs(raw,events,event_id=events_ids,preload=True)
    from mne.decoding import UnsupervisedSpatialFilter
    from sklearn.decomposition import PCA
    X = epochs.get_data()
    pca = UnsupervisedSpatialFilter(PCA(n), average=False)
    pca_data = pca.fit_transform(X)
    epoch_avg = np.mean(pca_data, axis=0)    
    return pca_data,epoch_avg


def ModifyDatabase(epochs,label):
    X = epochs
    y = label
    db = np.load(DB_PATH,allow_pickle='TRUE')
    flatX = X.flatten()
    flatX = np.append(flatX,y)
    db = np.append(db,[flatX],axis=0)
    np.save(DB_PATH,db) 
    #db.close()
    
    

    
















