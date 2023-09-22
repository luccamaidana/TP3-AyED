#import
import os
import pickle
import os.path
import io

#class
class user:
    def __init__(self):
        self.cod = 0
        self.usuario = ""
        self.clave = ""
        self.tipo = ""

#PP
afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

regUser.cod=1
regUser.usuario="admin@shopping.com"
regUser.clave="12345"
regUser.tipo="administrador"
pickle.dump(regUser,alu)

regUser.usuario = regUser.usuario.ljust(100)
regUser.clave = regUser.clave.ljust(8)
regUser.tipo = "usuario"

regUser.cod=2
regUser.usuario= input("\nUsuario:")
regUser.clave= input("\nClave:")
pickle.dump(regUser, alu)

alu.flush()
alu.close()

#lectura
alu = open (afu,"r+b")
tamU= os.path.getsize(afu)

while alu.tell() < tamU:
    regUser = pickle.load(alu)
    print(regUser.cod)
    print(regUser.usuario)
    print(regUser.clave)
    print(regUser.tipo)

alu.close()