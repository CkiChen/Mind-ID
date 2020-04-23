
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
    picks_meg = mne.pick_types(raw.info, meg=False, eeg=True, eog=False,
                               stim=False, exclude='bads')
    montage =  mne.channels.make_standard_montage('standard_1005')
    raw.set_montage(montage,match_case=False)

    

def ApplyICA(raw):
    ica = mne.preprocessing.ICA(n_components=20,random_state=0)
    ica.fit(raw.copy().filter(8,40))    
    #ica.plot_components(outlines = 'skirt')    
    #raw.plot()    
    raw_corrected = raw.copy()    
    ica.apply(raw_corrected)
    #ica.apply(raw_corrected).plot();
    return raw_corrected,ica
    

def GetEpochs(raw,ica):
    dictionary = {"T2" : 100}
    eves = mne.events_from_annotations(raw,dictionary)
    events = eves[0] 
    events_ids = {"target/stimulus":100}
    epochs = mne.Epochs(raw,events,event_id=events_ids,preload=True)
    #epochs.plot()
    epochs = ica.apply(epochs)
    epochs.apply_baseline((None,0))
    #epochs.save("S01E01.fif")
    return epochs


def ModifyDatabase(epochs,label):
    from scipy.stats import trim_mean  
    trim = lambda x: trim_mean(x, 0.1, axis=0)  
    epoch_avg = epochs.average(method=trim) 
    #epoch_avg.plot()
    #epochs.plot_psd()
    #epochs.plot()
    epoch_av_data = epoch_avg.data
    X = epoch_av_data
    y = label
    db = np.load(DB_PATH,allow_pickle='TRUE')
    flatX = X.flatten()
    flatX = np.append(flatX,y)
    db = np.append(db,[flatX],axis=0)
    np.save(DB_PATH,db) 
    #db.close()
    
    

    
















