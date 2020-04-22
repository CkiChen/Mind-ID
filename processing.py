'''
In summary, the experimental runs were:

Baseline, eyes open
Baseline, eyes closed
Task 1 (open and close left or right fist)
Task 2 (imagine opening and closing left or right fist)
Task 3 (open and close both fists or both feet)
Task 4 (imagine opening and closing both fists or both feet)
Task 1
Task 2
Task 3
Task 4
Task 1
Task 2
Task 3
Task 4
The data are provided here in EDF+ format (containing 64 EEG signals, each sampled at 160 samples per second, and an annotation channel). For use with PhysioToolkit software, rdedfann generated a separate PhysioBank-compatible annotation file (with the suffix .event) for each recording. The .event files and the annotation channels in the corresponding .edf files contain identical data.

Each annotation includes one of three codes (T0, T1, or T2):

T0 corresponds to rest
T1 corresponds to onset of motion (real or imagined) of
the left fist (in runs 3, 4, 7, 8, 11, and 12)
both fists (in runs 5, 6, 9, 10, 13, and 14)
T2 corresponds to onset of motion (real or imagined) of
the right fist (in runs 3, 4, 7, 8, 11, and 12)
both feet (in runs 5, 6, 9, 10, 13, and 14)
'''


import mne
import matplotlib.pyplot as plt
%matplotlib qt

fname = 'Data/S001R03.edf'
fevent = 'Data/S001R03.edf.event'

raw = mne.io.read_raw_edf(fname,preload=True)


xRaw = raw.get_data()

raw.plot_psd()


raw.plot()


raw.filter(None, 50., h_trans_bandwidth='auto', filter_length='auto',
           phase='zero')

print(raw.ch_names)
#print(raw.info)
print(raw.info['chs'][0]['loc'])
for x in raw.ch_names:
    str = x.replace(".", "")
    #print(str)
    raw.rename_channels(mapping={x:str})
print (raw.ch_names)
print(raw.info['chs'][0]['loc'])



channels = raw.ch_names

raw.filter(1, 40, n_jobs=2)  # 1Hz high pass is often helpful for fitting ICA


picks_meg = mne.pick_types(raw.info, meg=False, eeg=True, eog=False,
                           stim=False, exclude='bads')


montage =  mne.channels.make_standard_montage('standard_1005')
raw.set_montage(montage,match_case=False)


ica = mne.preprocessing.ICA(n_components=20,random_state=0)


ica.fit(raw.copy().filter(8,40))

ica.plot_components(outlines = 'skirt')

raw.plot()

raw_corrected = raw.copy()

ica.apply(raw_corrected).plot();


#EPOCH EXTRACTION

dictionary = {
            "T2" : 100
        }

eves = mne.events_from_annotations(raw_corrected,dictionary)

events = eves[0] 

events_ids = {"target/stimulus":100}

epochs = mne.Epochs(raw_corrected,events,event_id=events_ids,preload=True)

epochs.plot()


epochs = ica.apply(epochs)



epochs.apply_baseline((None,0))
 

#events = mne.find_events(raw_corrected,channels)


epochs.save("S01E01.fif")

