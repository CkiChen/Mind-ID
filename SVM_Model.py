

#DIMS = 15x113

USER_LIST = 'Res/Users.npy'
DB_PATH = 'Res/dataset.npy'
import numpy as np
import processing as proc
import pickle as pkl


def UpdateModel():
    database = np.load(DB_PATH,allow_pickle='TRUE')
    database = database[1:]
    rows,cols = len(database),len(database[0])
    
    X = []
    y = []
    
    for r in database:
        y.append(r[-1])
        arrr = r[:cols-1]
        arrr = np.reshape(arrr,(15,113))
        X.append(arrr)
        
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import LinearSVC
    from mne.decoding import Vectorizer
    clf = make_pipeline(Vectorizer(),StandardScaler(),LinearSVC())
    clf.fit(X,y)
    pkl.dump(clf,open('model.pkl','wb'))



def MakePrediction(username,fname):
    userlist = np.load(USER_LIST,allow_pickle='TRUE').item()
    real_label = userlist[username]
    raw = proc.Input(fname)
    proc.SetMontage(raw)
    pca_epochs,avg_epoch = proc.ApplyPCA(raw,15)
    clf = pkl.load(open('model.pkl', 'rb'))
    predicted_label = clf.predict([avg_epoch])

    if predicted_label == real_label:
        return True
    else :
        return False
    #pred = clf.predict(pca_epochs)
    #print(pred)





                   
