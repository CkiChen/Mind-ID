
import processing as proc
import numpy as np
import pickle as pkl

#args 1 -> username , args2 -> array file adresses,args3 -> email
def registerUser(username,filesArray,mail): 
    userlist = np.load(proc.USER_LIST,allow_pickle='TRUE').item()
    label = -1
    if username in userlist:
        print("Username already taken!")
        return
    else:
        cnt = len(userlist)
        label = cnt+1
        userlist.update({username:(cnt+1)})
        np.save(proc.USER_LIST,userlist) 

    for fname in filesArray:
        raw = proc.Input(fname)
        proc.SetMontage(raw)
        epochs,avg_epoch = proc.ApplyPCA(raw,15)
        if label == -1:
            pass
        else:
            proc.ModifyDatabase(avg_epoch,label)
    
    
    
    
    
    
    
'''
files = ['Data/S1/S001R03.edf','Data/S1/S001R04.edf','Data/S1/S001R07.edf','Data/S1/S001R08.edf',
         'Data/S1/S001R11.edf','Data/S1/S001R12.edf']    


registerUser('John',files,'john@gmail.com')


files = ['Data/S2/S002R03.edf','Data/S2/S002R04.edf','Data/S2/S002R07.edf','Data/S2/S002R08.edf',
         'Data/S2/S002R11.edf','Data/S2/S002R12.edf']    


registerUser('Amy',files,'amy@gmail.com')




files = ['Data/S3/S003R03.edf','Data/S3/S003R04.edf','Data/S3/S003R07.edf','Data/S3/S003R08.edf',
         'Data/S3/S003R11.edf','Data/S3/S003R12.edf']    



registerUser('Chris',files,'amit@ymail.com')



files = ['Data/S4/S004R03.edf','Data/S4/S004R04.edf','Data/S4/S004R07.edf','Data/S4/S004R08.edf',
         'Data/S4/S004R11.edf','Data/S4/S004R12.edf']    


registerUser('Monica',files,'monica@ymail.com')



files = ['Data/S5/S005R03.edf','Data/S5/S005R04.edf','Data/S5/S005R07.edf','Data/S5/S005R08.edf',
         'Data/S5/S005R11.edf','Data/S5/S005R12.edf']    


registerUser('Adam',files,'adam@ymail.com')

'''