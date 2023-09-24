global cont
cont=2
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
#afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

#locales
#afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
afl = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\LOCALES.dat"
#all = open (afl, "w+b")
regLoc = locales()

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

#-------------------------CARGAS---------------------------

regUser.cod=1
regUser.usuario="5"
regUser.clave="6"
regUser.tipo="administrador"
pickle.dump(regUser,alu)



regUser.cod=cont
regUser.usuario= input("\nUsuario:")
regUser.clave= input("\nClave:")
pickle.dump(regUser, alu)

alu.flush()
alu.close()
#------------------------ATAJOS-------------------------

       

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
def pantalla_adm():
    clear_screen()
    print("\n        Menú ADMIN")
    print("Ingrese una opcion 0-5\n")
    print("1_ Gestión de locales")
    print("2_ Crear cuentas de dueños de locales")
    print("3_ Aprobar / Denegar solicitud de descuento")
    print("4_ Gestión de novedades")
    print("5_ Reporte de utilización de descuentos")
    print("0_ Fin de programa")


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
def valid_adm():
    global opcadm
    opcadm = input("\nOPCION: ")
    while opcadm != "1" and opcadm != "2" and opcadm != "3" and opcadm != "4" and opcadm != "5" and opcadm != "0":
        opcadm = input("Mal ingresado. Repetir opción. OPCION: ")
    clear_screen()

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
            signin()
            mainMenu()
        case "3":
            print("\nSaliendo...")

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
            regUser=pickle.load(alu)
            #si no funca agregar reguser/ty

        if(regUser.usuario==nombre and regUser.clave==password):  
            correcto=1
        else:
            nombre=input("\nIngrese el nombre: ")
            password = maskpass.askpass(prompt="\nIngresar contraseña: ", mask="*")
            cont=cont+1
            alu.seek(0,0)
    if (regUser.usuario==nombre and regUser.clave==password):  
            correcto=1    
    if(correcto==1):
        select_menu(regUser.tipo)
    else:
        print("Cantidad de maxima de intentos permitidos")

    alu.close()
#-------------------------SIGN IN----------------------------

def signin():
    global cont
    alu = open (afu, "r+b")
    size=os.path.getsize(afu)
    regUser=pickle.load(alu)
    flag=0
    regUser.usuario = regUser.usuario.ljust(100)
    regUser.clave = regUser.clave.ljust(8)
    regUser.tipo= regUser.tipo.ljust(13)

    nombre=input("\nIngrese el nombre: ")

    while flag!=1:
        alu.seek(0,0)

        while(alu.tell() < size) and (regUser.usuario!=nombre):
            regUser=pickle.load(alu)
        if(regUser.usuario==nombre):  
            nombre=input("\nEse nombre ya existe. Ingrese el nombre: ")  
        else:
            flag=1
            alu.seek(0,0)

    password = maskpass.askpass(prompt="\nIngrese una contraseña con 8 caracteres: ", mask="*")
    while len(password)!=8:
        password = maskpass.askpass(prompt="\nLa contraseña debe contener 8 caracteres: ", mask="*")

    cont=cont+1
    regUser.cod=cont
    regUser.usuario = nombre
    regUser.clave = password
    regUser.tipo = "cliente"

    pickle.dump(regUser, alu)
    alu.flush()
    alu.close()
    print("\nPerfil creado exitosamente!")
    print("Volviendo...")
#-------------------------MENU'S----------------------------
def menu_admin():
   
   pantalla_adm()
   valid_adm()
   match opcadm:
      case "1":
        #clear_screen()
        print("\nGestión de locales")
        gestion_locales()
        orden_rub(shopping_loc)
      case "2":
       clear_screen()
       print("\nCrear cuentas de dueños de locales")
       menu_admin()
      case "3":
        clear_screen()
        print("\nAprobar / Denegar solicitud de descuento")
        menu_admin()
      case "4":
        clear_screen()
        print("\nGestión de novedades")
        gestion_novedades()
      case "5":
        clear_screen()
        print("\nEn construcción…")
        menu_admin()
      case "0":
        clear_screen()
        chau_franchu=f"""{Fore.RED}
        ▒╔═╦═╦═╦╦╦═╦══╗▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒║╬║║║╔╣╔╣╦╩╗╔╝▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒
        ▒║╗╣║║╚╣╚╣╩╗║║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄██▒▒
        ▒╚╩╩═╩═╩╩╩═╝╚╝▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀██▀█▀█▀███
        ▒╔══╦═╦══╦═╦═╗▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀▀▀████▀▀▀▒
        ▒╚╗╔╣╦╣╔╗║║║║║▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▀██▒▒▒▒
        ▒▒║║║╩╣╠╣║║║║║▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒╚╝╚═╩╝╚╩╩═╩╝▒▒▒▒▒▒▄▒▒▒─███▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐█▌▒▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▐█▒▒▒▒▒▒▒▒▄▄▄▒▒▒█▒▒▒▒▄▒▒▒▒▒▒▒
        ▒▒▒▒█████████▒▒▒▒▒▒▒▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄
        ▒▒▒████████████▒▒▒▒▒░█▀█▀█░█▀██░█▀█░█▄█▄█
        ▒▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▒▒▒░█▀█▀█░█▀████▀█░█▄█▄█
        ▐████████████████▒▒▒████████▀████████████
"""
        print(chau_franchu)
        
        exit = input("\n Toque Enter para salir: ")
        while exit != "":
                exit = input("Respuesta inválida. Presione ENTER: ")
        print("\nSaliendo...")
#Main Menu
def mainMenu():
    #clear_screen()
    mostrar_menu()
    ingreso_datos(valid_opc())

def PP():
    mainMenu()

PP()








