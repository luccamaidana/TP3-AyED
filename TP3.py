#import
import os
import pickle
import os.path
import io

class user:
    def __init__(self):
        self.cod = 0
        self.usuario = ""
        self.clave = ""
        self.tipo = ""

class locales:
    def __init__(self):
        self.codLocal = 0
        self.nombreLocal = ""
        self.ubicacionLocal = ""
        self.rubroLocal = ""
        self.codUsuario = 0
        self.estado = ""

class promociones:
    def __init__(self):
        self.codPromo = 0
        self.textoPromo = ""
        self.fechaDesdePromo = ""
        self.fechaHastaPromo = ""
        self.diasSemana = ""
        self.estado = ""
        self.codLocal = 0

class uso_promociones: 
    def __init__(self):
        self.codCliente = 0
        self.codPromo = ""
        self.fechaUsoPromo = ""

class novedades:
    def __init__(self):
        self.codNovedad = 0
        self.textoNovedad = ""
        self.fechaDesdeNovedad = ""
        self.fechaHastaNovedad = ""
        self.tipoUsuario = ""
        self.estado = ""

#------------------------PP-----------------------------------
#user
#afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

regUser.usuario = regUser.usuario.ljust(100)
regUser.clave = regUser.clave.ljust(8)
regUser.tipo= regUser.tipo.ljust(14)




#locales
#afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
afl = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\LOCALES.dat"
all = open (afl, "w+b")
regLoc = locales()

pickle.dump(regLoc,all)
all.flush()
all.seek(0,0)
regLoc.codLocal=1
regLoc.nombreLocal="Caquita".ljust(100)
regLoc.ubicacionLocal="narnia".ljust(100)
regLoc.rubroLocal="Indumentaria".ljust(12)
regLoc.codUsuario=0
regLoc.estado="A"
pickle.dump(regLoc,all)
regLoc.codLocal=2
regLoc.nombreLocal="Azombrozo".ljust(100)
regLoc.ubicacionLocal="narnia2".ljust(100)
regLoc.rubroLocal="Perfumeria".ljust(12)
regLoc.codUsuario=0
regLoc.estado="A"
pickle.dump(regLoc,all)
regLoc.codLocal=3
regLoc.nombreLocal="Barbaro".ljust(100)
regLoc.ubicacionLocal="sex".ljust(100)
regLoc.rubroLocal="Perfumeria".ljust(12)
regLoc.codUsuario=0
regLoc.estado="A"
pickle.dump(regLoc,all)
regLoc.nombreLocal = regLoc.nombreLocal.ljust(100)
regLoc.ubicacionLocal = regLoc.ubicacionLocal.ljust(100)
regLoc.rubroLocal = regLoc.rubroLocal.ljust(12)

all.flush()
all.close()

#promos
#afp = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\PROMOCIONES.DAT"
afp = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\PROMOCIONES.DAT"
#alp = open (afp, "w+b")
regProm = promociones()

#uso promos
#afup = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USO_PROMOCIONES.DAT"
afup = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USO_PROMOCIONES.DAT"
#alup = open (afup, "w+b")
regUP = uso_promociones()

#novedades
#afn = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\NOVEDADES.DAT"
afn = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\NOVEDADES.DAT"
#aln = open (afn, "w+b")
regNov = novedades()

#-------------------------EL AJUSTE---------------------------






#-------------------------PRECARGAS/CARGAS---------------------------




def locales_cargados(): #agregar linduras p/
    all = open (afl,"r+b")
    size= os.path.getsize(afl)

    while all.tell() < size:
        regLoc = pickle.load(all)
        print(regLoc.codLocal,regLoc.nombreLocal.rstrip(),regLoc.ubicacionLocal.rstrip(),regLoc.rubroLocal.rstrip(),regLoc.estado)

    all.close()


def orden_rub(matriz):
    for i in range(len(matriz[0])):
        for j in range(i+1, len(matriz[0])):
            if matriz[1][i] < matriz[1][j]:
                # Intercambiar las columnas i y j
                for k in range(len(matriz)):
                    aux = matriz[k][i]
                    matriz[k][i] = matriz[k][j]
                    matriz[k][j] = aux
    print(matriz[0])
    print(matriz[1])

# Resto del código permanece igual...


#----------------------------CONTADURIA RUBROS-----------------------------
def rubros():
    all=open(afl,"r+b")
    all.seek(0,0) 
    size=os.path.getsize(afl)
    rubrolocal = [[0] * 3 for i in range(2)]
    print(rubrolocal)
    rubrolocal[0][0]="Indumentaria"
    rubrolocal[0][1]="Perfumeria"
    rubrolocal[0][2]="Comidas"
    all.seek(0,0)
    while all.tell()<size:

        regLoc=pickle.load(all)
        if regLoc.estado == "A":
            match regLoc.rubroLocal.rstrip():
                case "Indumentaria":
                    rubrolocal[1][0] += 1
                case "Perfumeria":
                    rubrolocal[1][1] += 1
                case "Comidas":
                    rubrolocal[1][2] += 1


    orden_rub(rubrolocal)
    


rubros()
#locales_cargados()