# Mind-ID
As the risks and concerns for cyber-security are ever-increasing and have become mainstream,conventional methods for authentication like alphanumeric passwords may soon susceptible to
higher security threats. Hence, technology is moving towards biometric based methods which are hard to crack,replicate and reproduce.
In this project , we attempt to develop a biometric (Electroencephalogram (EEG) signal) based user authentication system that can potentially be used by clients as a
log-in interface for their users.

## Methodology

Phase 1:

Physionet’s EEG Motor Movement/Imagery
Dataset was used as source of the EEG data.
Under this experiment , each of the 109 subjects
performed 14 experimental runs: two one-minute
baseline runs (one with eyes open, one with eyes
closed), and three two-minute runs of each of four
tasks.Epochs were extracted using events of one
of the four tasks. (Annotated as T2 in data files).

Phase 2:

To read , process and visualise EEG data in python , the following
following modules were utilised - MNE-python , NumPy , Matplotlib. In
the processing steps , raw data was filter based on frequency range
and 'bad channels' .Next , montage was set for the data to emulate
electrodes and headshape sensor positions. Eye blinking and other
artifacts were removed using Independent Component Analysis (ICA).
Now , to reduce the number of channels and hence , the feature space
, Principal Componenet Analysis (PCA) was applied .
Next comes epoch extraction , epochs corresponding to our chosen
experimental stimuli were chosen , averaged and stored as a sample.
Data to make predictions is now obtained.

Phase 3:

For the next phase , a classification model is need to be
implemented which will make predictions on input data during log
in attempts. This model needs to updated as well , after a new user
registered to the system and new data is attained. We are looking
for a multi-class classifying algorithm.Support Vector Machine(SVM)
model was chosen as they are used widely for classification of EEG
signals as they shows good generalization performance for high
dimensional data due to its convex optimization problem.
UI development is undergoing in parallel. Python's PyQt5 module
was used along with PyQt5-tools which is a designing tool for the
same. PyQt5 lets you use the Qt GUI framework from Python. Qt itself
is written in C++. By using it from Python, you can build applications
much more quickly while not sacrificing much of the speed of C++.

## Citations
Original dataset resource -[
Schalk, G., McFarland, D.J., Hinterberger, T., Birbaumer, N.,
Wolpaw, J.R. BCI2000: A General-Purpose Brain-Computer
Interface (BCI) System. IEEE Transactions on Biomedical
Engineering 51(6):1034-1043, 2004.](https://pubmed.ncbi.nlm.nih.gov/15188875/)

Citation for PhysioNet -
Goldberger AL, Amaral LAN, Glass L, Hausdorff JM, Ivanov
PCh, Mark RG, Mietus JE, Moody GB, Peng C-K, Stanley HE.
PhysioBank, PhysioToolkit, and PhysioNet: Components of a
New Research Resource for Complex Physiologic Signals
(2003). Circulation. 101(23):e215-e220.
