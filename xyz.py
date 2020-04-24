import mne
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib qt





fname = 'Data/S1/S001R03.edf'

raw = mne.io.read_raw_edf(fname,preload=True)
raw.plot()


#xRaw = raw.get_data()
#raw.plot_psd()
#raw.plot()

good_chs = ['Fc5', 'Fc3', 'Fc1', 'Fcz', 'Fc2', 'Fc4', 'Fc6', 'C5', 'C3', 'C1', 'Cz', 'C2',
 'C4', 'C6','Fp1', 'Fpz', 'Fp2','Af7', 'Af3', 'Afz', 'Af4', 'Af8', 'F7', 
 'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6','F8', 'Ft7', 'Ft8', 'T7', 'T8', 'T9', 'T10', 'Tp7', 'Tp8']




print(raw.ch_names)
#print(raw.info)
print(raw.info['chs'][0]['loc'])
for x in raw.ch_names:
    str = x.replace(".", "")
    #print(str)
    raw.rename_channels(mapping={x:str})
print (raw.ch_names)




good_chs = ['Fc5', 'Fc3', 'Fc1', 'Fcz', 'Fc2', 'Fc4', 'Fc6', 'C5', 'C3', 'C1', 'Cz', 'C2',
 'C4', 'C6','Fp1', 'Fpz', 'Fp2','Af7', 'Af3', 'Afz', 'Af4', 'Af8', 'F7', 
 'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6','F8', 'Ft7', 'Ft8', 'T7', 'T8', 'T9', 'T10', 'Tp7', 'Tp8']


raw =raw.filter(None, 50., h_trans_bandwidth='auto', filter_length='auto',
           phase='zero',picks = good_chs)

raw['Tp7']



print(raw.info['chs'][0]['loc'])



channels = raw.ch_names
channels


raw['Iz']


raw.filter(1, 40, n_jobs=2)  # 1Hz high pass is often helpful for fitting ICA


picks_meg = mne.pick_types(raw.info, meg=False, eeg=True, eog=False,
                           stim=False, exclude='bads')


montage =  mne.channels.make_standard_montage('standard_1005')
raw.set_montage(montage,match_case=False)


ica = mne.preprocessing.ICA(n_components=20,random_state=0)


ica.fit(raw.copy().filter(8,40))

#ica.plot_components(outlines = 'skirt')

#raw.plot()

raw_corrected = raw.copy()

ica.apply(raw_corrected).plot();


#EPOCH EXTRACTION

dictionary = {
            "T2" : 100
        }

eves = mne.events_from_annotations(raw,dictionary)

events = eves[0] 

events_ids = {"target/stimulus":100}


epochs = mne.Epochs(raw,events,event_id=events_ids,preload=True)

epochs = mne.Epochs(raw_corrected,events,event_id=events_ids,preload=True)


#epochs.plot()


epochs = ica.apply(epochs)



epochs.apply_baseline((None,0))
 

#events = mne.find_events(raw_corrected,channels)


#epochs.save("S01E01.fif") 

#





from scipy.stats import trim_mean  
trim = lambda x: trim_mean(x, 0.1, axis=0)  

epoch_avg = epochs.average(method=trim) 

#epoch_avg.plot()

epoch_av_data = epoch_avg.data



'''


'''

epochs.plot_psd()

epochs.plot()




from mne.decoding import UnsupervisedSpatialFilter

from sklearn.decomposition import PCA, FastICA


X = epochs.get_data()




pca = UnsupervisedSpatialFilter(PCA(12), average=False)
pca_data = pca.fit_transform(X)

tmin, tmax = -0.1, 0.3
ev = mne.EvokedArray(np.mean(pca_data, axis=0),
                     mne.create_info(12, epochs.info['sfreq'],
                                     ch_types='eeg'), tmin=tmin)



ev.plot(show=False, window_title="PCA", time_unit='s')


from scipy.stats import trim_mean  
trim = lambda x: trim_mean(x, 0.1, axis=0)  

epoch_avg = np.mean(pca_data, axis=0)



#epoch_avg.plot()

epoch_av_data = epoch_avg.data







X = epoch_av_data
y = Users[username]

'''