#------------------------IMPORT-------------------------------
import os
import pickle
import os.path
import io
import shutil
def clear_screen():
    # Comando para limpiar la pantalla en Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux, macOS, etc.)
    else:
        os.system('clear')

#--------------------------CLASS------------------------------
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
        self.codUsuario = ""
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
afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

#locales
afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
#all = open (afl, "w+b")
regLoc = locales()

#promos
afp = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\PROMOCIONES.DAT"
#alp = open (afp, "w+b")
regProm = promociones()

#uso promos
afup = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USO_PROMOCIONES.DAT"
#alup = open (afup, "w+b")
regUP = uso_promociones()

#novedades
afn = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\NOVEDADES.DAT"
#aln = open (afn, "w+b")
regNov = novedades()

#-------------------------CARGAS---------------------------
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

#------------------------LECTURAS-------------------------
alu = open (afu,"r+b")
tamU= os.path.getsize(afu)

while alu.tell() < tamU:
    regUser = pickle.load(alu)
    print(regUser.cod)
    print(regUser.usuario)
    print(regUser.clave)
    print(regUser.tipo)

alu.close()


#------------------------PANTALLAS-------------------------
def mostrar_menu():
    ancho_ventana = shutil.get_terminal_size().columns

    menu_texto = "Menú"

    espacio_blancos = (ancho_ventana - len(menu_texto) - 2) // 2

    print("-" * ancho_ventana)
    print(f"|{' ' * espacio_blancos}{menu_texto}{' ' * espacio_blancos}|")
    print("-" * ancho_ventana)
    print("\nIngrese una opcion 1-3\n")
    print("1_ Ingresar con usuario registrado\n2_ Registrarse como cliente\n3_ Salir")


#-------------------------MENU'S----------------------------
#Main Menu
def mainMenu():
    clear_screen()
    mostrar_menu()

    opc= input("Ingrese la opcion: ")



def PP():
    mainMenu()

PP()



