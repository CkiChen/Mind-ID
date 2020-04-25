import numpy as np
import os

def init():
    dirname = os.path.dirname(__file__)     ### This defines dirctory path
    try:
        filename = os.path.join(dirname, 'Res/Users.npy')   ### this puts absolute path in filename
        f = open(filename)
        print("Already exists!")
        f.close()
    except:
        print("creating...")
        Users={}
        filename = os.path.join(dirname, 'Res/Users.npy')
        np.save(filename, Users) 
        ch = 15
        temp = np.zeros(ch*113+1)
        dataset=[temp]
        filename = os.path.join(dirname, 'Res/dataset.npy')
        np.save(filename,dataset)                

       
# init()
