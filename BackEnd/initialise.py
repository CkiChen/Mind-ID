import numpy as np

def init():
    
    try:
        f = open('Res/Users.npy')
        print("Already exists!")
        f.close()
    except IOError:
        print("creating...")
        Users={};
        np.save('Res/Users.npy', Users) 
        ch = 15
        temp = np.zeros(ch*113+1)
        dataset=[temp]
        np.save('Res/dataset.npy',dataset)                

       
init()
