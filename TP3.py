#import
import os
import pickle
import os.path
import io

#class
class USUARIOS:
    def __init__(self):
        self.cod = 0
        self.user = ""
        self.clave = ""
        self.tipo = ""

#PP
os.makedirs("users")
afu = "C:\Users\lucca\Desktop\UTN\AyED\TP\TP3-AyED\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = USUARIOS()
