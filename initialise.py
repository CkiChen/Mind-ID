import numpy as np

def init():
    Users={
            
        };
    
    np.save('Res/Users.npy', Users) 

    temp = np.zeros(7233)
    dataset=[temp]

    np.save('Res/dataset.npy',dataset)    
    
    
    
init()
