#import
import os
import pickle
import os.path
import io

def orden():  #ordena por campo codigo 
    all = open(afl, "r+b")
    all.seek (0, 0)
    aux = pickle.load(all)
    auxi = pickle.load(all)
    auxj = pickle.load(all)
    tamReg = all.tell() 
    tamArch = os.path.getsize(afl)
    cantReg = tamArch // tamReg
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            all.seek (i*tamReg, 0)
            auxi = pickle.load(all)
            all.seek (j*tamReg, 0)
            auxj = pickle.load(all)
            if (auxi.nombreLocal > auxj.nombreLocal):
                auxreg = auxi
                auxi = auxj
                auxj = auxreg
                all.seek (i*tamReg, 0)
                pickle.dump(auxj, all)
                all.seek (j*tamReg, 0)
                pickle.dump(auxi, all)
                all.flush()
