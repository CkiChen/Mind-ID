

#DIMS = 15x113

#USER_LIST = 'Res/Users.npy'
#DB_PATH = 'Res/dataset.npy'

import numpy as np
import processing as proc
import pickle as pkl
import os


def SetPathsVars():
    global USER_LIST
    global DB_PATH
    global USER_PLOT_PATH 
    dirname = os.path.dirname(__file__)                  ### This defines dirctory path
    USER_LIST = os.path.join(dirname, 'Res/Users.npy')   ### this puts absolute path in filename
    DB_PATH = os.path.join(dirname, 'Res/dataset.npy')    
    USER_PLOT_PATH = os.path.join(dirname,'Res/Plots')
    





def getPath(s):
    dirname = os.path.dirname(__file__)                  ### This defines dirctory path
    path = os.path.join(dirname,s)                       ### this puts absolute path in filename
    return path


def UpdateModel():
    try :  
        SetPathsVars() 
        database = np.load(DB_PATH,allow_pickle='TRUE')
        print(database)
        database = database[1:]
        rows,cols = len(database),len(database[0])
        print(rows,cols)
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
        pkl.dump(clf,open(getPath('Res/model.pkl'),'wb'))
        print('Successfully updated model')
        return True        
    except Exception as e:
        print(e)
        print("Update Model haga")
        return False
    
    

def MakePrediction(username,fname):
    SetPathsVars()
    userlist = np.load(USER_LIST,allow_pickle='TRUE').item()
    real_label = userlist[username]
    raw = proc.PredInput(fname)
    proc.PredSetMontage(raw)
    pca_epochs,avg_epoch = proc.PredApplyPCA(raw,15)
    clf = pkl.load(open(getPath('Res/model.pkl'),'rb'))
    predicted_label = clf.predict([avg_epoch])

    if predicted_label == real_label:
        return True
    else :
        return False



                   
