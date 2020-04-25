
import mne
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os





#%matplotlib qt


USER_LIST = 'Res/Users.npy'
DB_PATH = 'Res/dataset.npy'


def createDir(s):
    global USER_PLOT_PATH 
    USER_PLOT_PATH = 'Res/Plots'    
    USER_PLOT_PATH = os.path.join(USER_PLOT_PATH,s)
    os.mkdir(USER_PLOT_PATH)


def Input(fname):
    raw = mne.io.read_raw_edf(fname,preload=True)
    fig = raw.plot()
    fig.savefig(USER_PLOT_PATH+'/'+'raw-data.png')
    fig = raw.plot_psd()
    #print(USER_PLOT_PATH)
    #print(USER_PLOT_PATH+'/'+'power_spectral_density.png')
    fig.savefig(USER_PLOT_PATH+'/'+'power_spectral_density.png')
    return raw
    
         

def SetMontage(raw):
    raw.filter(None, 50., h_trans_bandwidth='auto', filter_length='auto',
           phase='zero')
    for x in raw.ch_names:
        str = x.replace(".", "")
        raw.rename_channels(mapping={x:str})
    raw.filter(1, 40, n_jobs=2) 
    montage =  mne.channels.make_standard_montage('standard_1005')
    fig = montage.plot()
    fig.savefig(USER_PLOT_PATH+'/'+'Montage.png')
    raw.set_montage(montage,match_case=False)

    

def ApplyPCA(raw,n): 
    dictionary = {"T2" : 100}
    eves = mne.events_from_annotations(raw,dictionary)
    events = eves[0] 
    events_ids = {"target/stimulus":100}
    epochs = mne.Epochs(raw,events,event_id=events_ids,preload=True)
    fig = epochs.plot()
    fig.savefig(USER_PLOT_PATH+'/'+'raw_epochs.png')
    fig = epochs.plot_psd()
    fig.savefig(USER_PLOT_PATH+'/'+'epochs_psd.png')    
    from mne.decoding import UnsupervisedSpatialFilter
    from sklearn.decomposition import PCA
    X = epochs.get_data()
    pca = UnsupervisedSpatialFilter(PCA(n), average=False)
    pca_data = pca.fit_transform(X)
    tmin, tmax = -0.1, 0.3
    ev = mne.EvokedArray(np.mean(pca_data, axis=0),
        mne.create_info(n,epochs.info['sfreq'],ch_types='eeg'),tmin=tmin)
    fig = ev.plot(show=False, window_title="PCA", time_unit='s')
    fig.savefig(USER_PLOT_PATH+'/'+'PCA_15_Channels.png')
    fig = ev.plot_image()
    fig.savefig(USER_PLOT_PATH+'/'+'EvokedData_As_Image.png')
    
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
    
    

    

#For Model
def PredInput(fname):
    raw = mne.io.read_raw_edf(fname,preload=True)
    return raw
    
         

def PredSetMontage(raw):
    raw.filter(None, 50., h_trans_bandwidth='auto', filter_length='auto',
           phase='zero')
    for x in raw.ch_names:
        str = x.replace(".", "")
        raw.rename_channels(mapping={x:str})
    raw.filter(1, 40, n_jobs=2) 
    montage =  mne.channels.make_standard_montage('standard_1005')
    raw.set_montage(montage,match_case=False)

    

def PredApplyPCA(raw,n): 
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















