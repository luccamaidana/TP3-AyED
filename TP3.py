#------------------------IMPORT-------------------------------
import os
import pickle
import os.path
import io
import shutil
import maskpass
def clear_screen():
    # Comando para limpiar la pantalla en Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux, macOS, etc.)
    else:
        os.system('clear')

import colorama
from colorama import Fore, Style

# Inicializar colorama
colorama.init(autoreset=True)


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
#afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

#locales
afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
#afl = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\LOCALES.dat"
#all = open (afl, "w+b")
regLoc = locales()

#promos
afp = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\PROMOCIONES.DAT"
#afp = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\PROMOCIONES.DAT"
#alp = open (afp, "w+b")
regProm = promociones()

#uso promos
afup = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USO_PROMOCIONES.DAT"
#afup = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USO_PROMOCIONES.DAT"
#alup = open (afup, "w+b")
regUP = uso_promociones()

#novedades
afn = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\NOVEDADES.DAT"
#afn = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\NOVEDADES.DAT"
#aln = open (afn, "w+b")
regNov = novedades()

#-------------------------CARGAS---------------------------

regUser.cod=1
regUser.usuario="5"
regUser.clave="6"
regUser.tipo="administrador"
pickle.dump(regUser,alu)



regUser.cod=2
regUser.usuario= input("\nUsuario:")
regUser.clave= input("\nClave:")
pickle.dump(regUser, alu)

alu.flush()
alu.close()

#------------------------LECTURAS-------------------------
#----Usuarios----
alu = open (afu,"r+b")
size= os.path.getsize(afu)

while alu.tell() < size:
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


#-------------------------LOGIN----------------------------

def login():
    alu = open (afu, "r+b")
    size=os.path.getsize(afu)
    correcto=0
    cont=1
    nombre=input("\nIngrese el nombre: ")
    password = maskpass.askpass(prompt="\nIngresar contraseña: ", mask="*")
    regUser=pickle.load(alu)
    #1
    while correcto!=1 and cont<3:
        alu.seek(0,0)

        while(alu.tell() < size) and (regUser.usuario!=nombre) and (regUser.clave!=password):
            pickle.load(alu)

        if(regUser.usuario==nombre and regUser.clave==password):  
            correcto=1
        else:
            nombre=input("\nIngrese el nombre: ")
            password = maskpass.askpass(prompt="\nIngresar contraseña: ", mask="*")
            cont=cont+1
            alu.seek(0,0)
            print(cont)
    if (regUser.usuario==nombre and regUser.clave==password):  
            correcto=1    
    if(correcto==1):
        god=regUser.tipo
        #selec_menu(regUser.tipo)
    else:
        print("Cantidad de maxima de intentos permitidos")

    alu.close()
#-------------------------SIGN IN----------------------------

def signin():
    alu = open (afu, "r+b")
    size=os.path.getsize(afu)
    regUser=pickle.load(alu)

    flag=0

    regUser.usuario = regUser.usuario.ljust(100)
    regUser.clave = regUser.clave.ljust(8)
    regUser.tipo = "cliente"

    nombre=input("\nIngrese el nombre: ")
    password = maskpass.askpass(prompt="\nIngrese una contraseña de 8 caracteres: ", mask="*")

    while flag!=1:
        alu.seek(0,0)

        while(alu.tell() < size) and (regUser.usuario!=nombre):
            pickle.load(alu)

        if(regUser.usuario==nombre):  
            flag=1

        else:
            nombre=input("\nEse nombre ya existe. Ingrese el nombre: ")
            password = maskpass.askpass(prompt="\nIngrese una contraseña de 8 caracteres: ", mask="*")
            alu.seek(0,0)
    
    #hacer cod y verificar 8 caract contra

    regUser.usuario = nombre
    regUser.clave = password
    pickle.dump(regUser, alu)
    alu.flush()

    alu.close()

    print("\nPerfil creado exitosamente!")
    print("Volviendo...")


#------------------------VALIDADORES-------------------------

def valid_opc():
    global opc
    opc = input("\nOPCION: ")
    #clear_screen()
    while opc != "1" and opc != "2" and opc != "3":
        mostrar_menu()
        opc = input("\nMal ingresado. Repetir opción. OPCION: ")
        #clear_screen()
    #clear_screen()
    return opc

#----------------------------CASE-----------------------------
def select_menu(m):
    match m:
        case "administrador":
            menu_admin()
        case "owner":
            menu_owner()
        case "cliente":
            menu_client()

def ingreso_datos(k):
    match k:
        case "1":
            login()
        case "2":
            print("\nSaliendo...")
            #signin()
        case "3":
            print("\nSaliendo...")


#-------------------------MENU'S----------------------------


#Main Menu
def mainMenu():
    #clear_screen()
    mostrar_menu()
    ingreso_datos(valid_opc())


def PP():
    mainMenu()

PP()






