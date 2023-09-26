global cont,contowner
cont=2
contowner=0
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
all = open (afl, "w+b")
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

#-------------------------PRECARGAS/CARGAS---------------------------

regUser.cod=1
regUser.usuario="5"
regUser.clave="6"
regUser.tipo="Administrador"
pickle.dump(regUser,alu)



regUser.cod=cont
regUser.usuario= input("\nUsuario:")
regUser.clave= input("\nClave:")
pickle.dump(regUser, alu)

alu.flush()
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
def pantalla_locales():
    
    print("\n        Gestión de locales")
    print("Ingrese una opción a-d\n")
    print("a- Crear locales")
    print("b- Modificar local")
    print("c- Eliminar local")
    print("d- Mapa de locales")
    print("e- Volver")




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
def valid_opc_loc():
    global opcloc
    opcloc = input("\nOPCION: ")
    opcloc = opcloc.lower()
    while opcloc != "a" and opcloc != "b" and opcloc != "c" and opcloc != "d" and opcloc != "e":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")
        opcloc = opcloc.lower()
    clear_screen()
#----------------------------CASE-----------------------------
def select_menu(m):
    match m:
        case "Administrador":
            menu_admin()
        case "Dueño de local":
            menu_owner()
        case "Cliente":
            menu_client()
def ingreso_main_menu(k):
    match k:
        case "1":
            login()
        case "2":
            signin("Cliente")
            mainMenu()
        case "3":
            print("\nSaliendo...")
def ingreso_datos():
    global k
    match k:
        case 0:
            print("\nIngrese el NOMBRE del local:")
        case 1:
            print("\nIngrese la UBICACIÓN del local:")
        case 2:
            print("\nIngrese el RUBRO del local:")
            valid_selec_rubro(shopping_loc[i][2])
        case 3:
            print("\nIngrese el CÓDIGO DEL USUARIO")
            valid_cod_user()

#----------------------------BUSQUEDA DICOATOMICA-----------------------------
def buscadicotomica(elem): 
        global bandera, med
        bandera=0 
        #all = open (afu,"r+b")
        regLoc=pickle.load(all)   
        tamreg=all.tell()
        tamarch=os.path.getsize(afl)
        cant=tamarch//tamreg
        inf = 0
        sup = cant-1

        while (inf<=sup) and bandera==0:
            med = (inf+sup)//2
            all.seek(med*tamreg,0)
            regLoc=pickle.load(all)
            if(regLoc.nombreLocal==elem):
                bandera=1
            else:
                if(regLoc.nombreLocal<elem):
                    inf=med+1
                else:
                    sup=med-1
        return bandera
#----------------------------CARGA LOCALES-----------------------------
def crear_locales():
    global k,i, shopping_loc,cod,bandera, med,rubroLocal,rub1,rub2,rub3
    k = 0
    alu = open (afu,"r+b")
    regUser=pickle.load(alu)
    all = open (afl,"r+b")
    regLoc=pickle.load(all)
    exit = "S" 
    while exit.upper() == "S" and k<=6:

        ingreso_datos()

        valor = input(f"Ingrese el Nombre del Local: ")
        bandera=1

        while bandera==1:
            bandera=buscadicotomica(valor)
            while (bandera == 1 or valor==""):
                if(valor==""):
                    valor = input(f"No se permiten espacios vacios. Pruebe nuevamente: ")
                    bandera=1
                else:
                    valor = input(f"Este nombre ya existe. Pruebe nuevamente: ")
                    bandera=buscadicotomica(valor)
        regLoc=all.seek(0,2)
        regLoc.nombreLocal=valor

        

        ubi = input("\nIngrese la UBICACIÓN: ")
        while ubi== "":
            ubi = input("No se permiten espacios vacios: ")
        regLoc.ubicacionLocal=ubi


        rubro = input("\nIngrese el RUBRO 1_Indumentaria 2_Perfumeria 3_Comidas ")
        while rubro!= "1" and rubro != "2" and rubro != "3":
            rubro = input("Mal ingresado. Repetir opción. OPCION: ")
        match rubro:
            case "1":
                regLoc.rubroLocal="Indumentaria"
            case "2":
                regLoc.rubroLocal="Perfumeria"
            case "3":
                regLoc.rubroLocal="Comidas"    
            

        

        size= os.path.getsize(afu)
        bandera=0
        cod = input("\nIngrese el CÓDIGO de dueño de local: ")
        while bandera==0:
            alu.seek(0,0)
            while alu.tell() < size and regUser.tipo!="Dueño de local" and regUser.cod!=cod:
                regUser = pickle.load(alu)
            if(regUser.tipo=="Dueño de local" and regUser.cod==cod):
                bandera=1
            else:
                cod = input("El codigo no pertenece a un dueño o no existe. Repetir código. CÓDIGO: ")
        regLoc.codUsuario=cod


        if k==4:
            shopping_loc[i][4]="A"
            k = k+1
        if k == 5:
                cod=cod+1
                shopping_loc[i][5]= cod
                k = 0
                i = i + 1
                orden(shopping_loc)
                if i == 49:
                        print("Se alcanzó el límite de filas (50).")
                else:
                        exit = input("\n ¿Desea seguir cargando? (S/N): ")
                        while exit.upper() != "S" and exit.upper() != "N":
                                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ")
                                #gestion_locales()

    pickle.dump(regLoc, all)
    all.flush()
                orden(shopping_loc)
        loc_cargados(shopping_loc)
    
    rubros(shopping_loc)
    exit = input("\n Toque Enter para volver: ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER: ")
    if exit=="": 
        clear_screen()
        gestion_locales()
#standby recordar close ambos alu afu 




#------------------------GESTIONES-------------------------
def gestion_locales(): 
    
    global shopping_loc, i
    all = open (afl,"r+b")
    regLoc=pickle.load(all)
    size=os.path.getsize(afl)
    pantalla_locales()
    valid_opc_loc()
    match opcloc:
        case "a":
            clear_screen()
            print("---Crear locales---")
            exit = input("\n ¿Desea ver los locales cargados? (S/N): ").upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            if exit=="S" and size=0:
                print("\n       No hay locales cargados hasta el momento.")
            else:
                if exit=="S":
                    all.seek(0,0)
                    while all.tell() < size:
                        regLoc = pickle.load(all)
                        print(regLoc.codLocal)
                        print(regLoc.nombreLocal)
                        print(regLoc.ubicacionLocal)
                        print(regLoc.rubroLocal)
                        print(regLoc.codUsuario)
                        print(regLoc.estado)
            if(contowner==0):
                print("No hay duenos regristrados.")
            else:
                crear_locales()
            gestion_locales()
        case "b":
            clear_screen()
            print("---Modificar locales---")
            exit = input("\n ¿Desea ver los locales cargados? (S/N): ").upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            if exit=="S" and i==0:
                print("\n       No hay locales cargados hasta el momento.")
            else:
                if exit=="S":
                    all.seek(0,0)
                    while all.tell() < size:
                        regLoc = pickle.load(all)
                        print(regLoc.codLocal)
                        print(regLoc.nombreLocal)
                        print(regLoc.ubicacionLocal)
                        print(regLoc.rubroLocal)
                        print(regLoc.codUsuario)
                        print(regLoc.estado)

            modificar_local(shopping_loc)
            gestion_locales()
        case "c":
            clear_screen()
            print("---Eliminar locales---")
            exit = input("\n ¿Desea ver los locales cargados? (S/N): ").upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            if exit=="S" and i==0:
                print("\n       No hay locales cargados hasta el momento.")
            else:
                if exit=="S":
                    all.seek(0,0)
                    while all.tell() < size:
                        regLoc = pickle.load(all)
                        print(regLoc.codLocal)
                        print(regLoc.nombreLocal)
                        print(regLoc.ubicacionLocal)
                        print(regLoc.rubroLocal)
                        print(regLoc.codUsuario)
                        print(regLoc.estado)

            eliminar_loc(shopping_loc)
            gestion_locales()

        case "d":
            clear_screen()
            mapa(shopping_loc)
            exit = input("\n Toque Enter para volver: ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER: ")
            if exit=="": 
                gestion_locales()
        case "e":
            menu_adm()
    all.close()     




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

def signin(user):
    global cont
    alu = open (afu, "r+b")
    size=os.path.getsize(afu)
    regUser=pickle.load(alu)
    flag=0
    regUser.usuario = regUser.usuario.ljust(100)
    regUser.clave = regUser.clave.ljust(8)
    regUser.tipo= regUser.tipo.ljust(14)

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
    regUser.tipo = user

    pickle.dump(regUser, alu)
    alu.flush()
    alu.close()
    print("\nPerfil creado exitosamente!")
    print("Volviendo...")
#-------------------------MENU'S----------------------------
def menu_admin():
   global contowner
   pantalla_adm()
   valid_adm()
   match opcadm:
      case "1":
        #clear_screen()
        print("\nGestión de locales")
        gestion_locales()
        #orden_rub(shopping_loc)
      case "2":
        clear_screen()
        print("\nCrear cuentas de dueños de locales")
        signin("Dueño de local")
        contowner=contowner+1
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
    ingreso_main_menu(valid_opc())

def PP():
    mainMenu()

PP()








