global cont,contowner,codloc,regLoc
cont=2
contowner=0
codloc=0
#------------------------IMPORT-------------------------------
import sys
import os
import pickle
import os.path
import io
import shutil
import maskpass
import datetime
import time
def clear_screen():
    # Comando para limpiar la pantalla en Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para limpiar la pantalla en sistemas basados en Unix (Linux, macOS, etc.)
    else:
        os.system('clear')

import colorama
from colorama import Fore, Style, Back

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
global all
#------------------------PP-----------------------------------
#user
""" afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
#afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
#afu = "E:\\Users\\Lenovo\\Documents\\GitHub\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()
size=os.path.getsize(afu) """

afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
#afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
#afu = "D:\\Descargas\\Facultad\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()



regUser.usuario = regUser.usuario.ljust(100)
regUser.clave = regUser.clave.ljust(8)
regUser.tipo= regUser.tipo.ljust(14)




#locales
afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
#afl = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\LOCALES.dat"
#afl="E:\\Users\\Lenovo\\Documents\\GitHub\\TP3-AyED\\LOCALES.dat"
all = open (afl, "w+b")

#allaux = open (afl, "w+b")
regLoc = locales()
regLocAux = regLoc
#pickle.dump(regLocAux,all)
#pickle.dump(regLoc,all)
all.flush()
#allaux.flush()
size= os.path.getsize(afl)
print(size)
regLoc.nombreLocal = regLoc.nombreLocal.ljust(100)
regLoc.ubicacionLocal = regLoc.ubicacionLocal.ljust(100)
regLoc.rubroLocal = regLoc.rubroLocal.ljust(12)
regLoc.estado = regLoc.estado.ljust(1)
size= os.path.getsize(afl)
print(size)
regLoc.codLocal= 0
regLoc.nombreLocal=""
regLoc.ubicacionLocal=""
regLoc.rubroLocal=""
regLoc.codUsuario= 0
regLoc.estado= "A"
size= os.path.getsize(afl)
print(size)

all.flush()



#-------------------------EL AJUSTE---------------------------






#-------------------------PRECARGAS/CARGAS---------------------------
pickle.dump(regLoc,all)
all.flush()
all.seek(0,0)
regLoc.codLocal=1
regLoc.nombreLocal="Nombre1".ljust(100)
regLoc.ubicacionLocal="narnia".ljust(100)
regLoc.rubroLocal="Indumentaria".ljust(12)
regLoc.codUsuario=2
regLoc.estado="A"
pickle.dump(regLoc,all)
regLoc.codLocal=2
regLoc.nombreLocal="Nombre2".ljust(100)
regLoc.ubicacionLocal="narniaconenanos".ljust(100)
regLoc.rubroLocal="Perfumeria".ljust(12)
regLoc.codUsuario=2
regLoc.estado="A"
pickle.dump(regLoc,all)
regLoc.codLocal=3
regLoc.nombreLocal="Nombre3".ljust(100)
regLoc.ubicacionLocal="sex".ljust(100)
regLoc.rubroLocal="Comidas".ljust(12)
regLoc.codUsuario=2
regLoc.estado="A"
pickle.dump(regLoc,all)


all.flush()
all.close()

regUser.cod=00
regUser.usuario="5"
regUser.clave="6"
regUser.tipo="Administrador"
pickle.dump(regUser,alu)
alu.flush()

#------------------------PANTALLAS-------------------------
def barracarga():
    clear_screen()
    print(Style.NORMAL + Fore.MAGENTA +Back.BLACK+ "         CARGANDO...       ")
    bar_len = 25
    elements = ['-','\\', '|', '/']
    for i in range(bar_len+1):
        frame =i%len(elements)
        print(Fore.GREEN+Style.BRIGHT +Back.BLACK+ f'\r[{elements[frame]*i:=^{bar_len}}]', end='')
        time.sleep(0.08) 


def centrar_input(prompt):
    ancho_consola, _ = shutil.get_terminal_size()
    espacio_adicional = max(0, (ancho_consola - len(prompt) -10) // 2)
    texto_centrado = " " * espacio_adicional + prompt
    return input(texto_centrado)
def centrar_texto_var(texto, var):
    anchoconsola,  = shutil.get_terminal_size()
    ancho_t = len(texto)
    ancho_v = len(var)
    espacio_disponible = anchoconsola - ancho_t - ancho_v
    espacio_adicional_izquierda = (espacio_disponible // 2) -5 
    espacio_adicional_derecha = espacio_disponible - espacio_adicional_izquierda
    texto_centrado = " " * espacio_adicional_izquierda + texto + var + " " * espacio_adicional_derecha 
    print(texto_centrado)
def centrar_texto(texto):
    ancho_consola, _ = shutil.get_terminal_size()
    espacio_adicional = max(0, (ancho_consola - len(texto)) // 2)
    texto_centrado = " " * espacio_adicional + texto
    print(texto_centrado)
def mostrar_menu():
    ancho_ventana = shutil.get_terminal_size().columns

    menu_texto = "Menú"

    espacio_blancos = (ancho_ventana - len(menu_texto) - 2) // 2

    print("-" * ancho_ventana)
    print(f"|{' ' * espacio_blancos}{menu_texto}{' ' * espacio_blancos}|")
    print("-" * ancho_ventana)
    print(Style.BRIGHT + '\nIngrese una opción' + Fore.YELLOW  + ' 1-3\n')
    print(Fore.YELLOW + '1_ ' + Fore.RESET + 'Ingresar con usuario registrado\n' + Fore.YELLOW + '2_' + Fore.RESET + ' Registrarse como cliente\n' + Fore.YELLOW + '3_' + Fore.RESET + ' Salir')
def pantalla_adm():
    clear_screen()
    centrar_texto(Style.BRIGHT  + Fore.WHITE +'Menú ADMIN')
    print(Style.BRIGHT +'Ingrese una opción ' +  Fore.LIGHTYELLOW_EX + '0-5\n')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '1_' + Fore.RESET + ' Gestión de locales')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '2_' + Fore.RESET +' Crear cuentas de dueños de locales')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '3_' + Fore.RESET +' Aprobar / Denegar solicitud de descuento')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '4_' + Fore.RESET +' Gestión de novedades')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '5_' + Fore.RESET +' Reporte de utilización de descuentos')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '0_' + Fore.RESET +' Volver al Menú Principal')
def pantalla_locales():
    clear_screen()
    centrar_texto(Fore.WHITE + Style.BRIGHT + "Gestión de locales")
    print(Style.BRIGHT +'Ingrese una opción ' +  Fore.LIGHTYELLOW_EX + 'a-d\n')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'a_' + Fore.RESET + ' Crear locales')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'b_' + Fore.RESET + ' Modificar local')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'c_' + Fore.RESET + ' Eliminar local')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'd_' + Fore.RESET + ' Mapa de locales')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'e_' + Fore.RESET + ' Volver')
def enter(menu):
    #COPIAR ESTA LINEA DE ABAJO PARA CADA EXIT
    #exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER: ")
    if exit=="":
        clear_screen()
        menu




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


#----Locales----
def locales_cargados():
    all = open(afl, "r+b")
    size = os.path.getsize(afl)
    all.seek(0, 0)

    # Definir ancho de cada columna de la tabla
    col_codLocal = 20
    col_nombreLocal = 40
    col_ubicacionLocal = 40
    col_rubroLocal = 20
    col_codUsuario = 16
    col_estado = 10

    # Encabezados de la tabla
    print(
        Back.BLACK + Fore.BLUE + Style.BRIGHT + Back.BLACK +
        f'{"Código del Local".center(col_codLocal)} | ' +
        f'{"Nombre".center(col_nombreLocal)} | ' +
        f'{"Ubicación".center(col_ubicacionLocal)} | ' +
        f'{"Rubro".center(col_rubroLocal)} | ' +
        f'{"Código del Dueño".center(col_codUsuario)} | ' +
        f'{"Estado".center(col_estado)}'
    )

    while all.tell() < size:
        regLoc = pickle.load(all)

        # Formatear y centrar cada columna en la tabla
        formatted_row = (
            Fore.WHITE + Style.BRIGHT + 
            f'{str(regLoc.codLocal).center(col_codLocal)} | ' +
            f'{regLoc.nombreLocal.strip().center(col_nombreLocal)} | ' +
            f'{regLoc.ubicacionLocal.strip().center(col_ubicacionLocal)} | ' +
            f'{regLoc.rubroLocal.strip().center(col_rubroLocal)} | ' +
            f'{str(regLoc.codUsuario).center(col_codUsuario)} | ' +
            f'{regLoc.estado.center(col_estado)}'
        )
        
        print(formatted_row)

    all.close()

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

def valid_campo(opc):
    while opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 0:
        opc = int(input("Mal ingresado. Repetir opción. OPCION: "))
    clear_screen()
    return opc

def valid_opc_loc():
    global opcloc
    opcloc = input("\nOPCION: ")
    opcloc = opcloc.lower()
    while opcloc != "a" and opcloc != "b" and opcloc != "c" and opcloc != "d" and opcloc != "e":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")
        opcloc = opcloc.lower()
    clear_screen()

def valid_codLoc(codLoc): #te dice si existe el codloc
    all=open(afl,"r+b")
    regLoc=locales()
    all.seek(0,0)
    size=os.path.getsize(afl)
    bandera=1
    while all.tell()<size and codLoc!=regLoc.codLocal and bandera==1:
        regLoc=pickle.load(all)
    if(codLoc!=regLoc.codLocal):
        bandera=1
        all.seek(0,0)
    else:
        bandera=0
    return bandera

def valid_codUser(): #te dice si esxiste el coduser
    global coduser
    all=open(all,"r+b")
    regLoc=locales()
    all.seek(0,0)
    size=os.path.getsize(afl)
    bandera=1
    while all.tell()<size and codLoc!=regLoc.codLocal and bandera==1:
        regLoc=pickle.load(all)
    if(codLoc!=regLoc.codLocal):
        bandera=1
        all.seek(0,0)
        codLoc=int(input("Codigo inexistente, pruebe nuevamente: "))
    else:
        bandera=0
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

#----------------------------BUSQUEDA DICOATOMICA-----------------------------
def buscadicotomica(elem): 
        global bandera, med
        print("bonjour")
        all = open (afl,"r+b")
        regLoc=locales()
        bandera=0 
        all.seek(0,0)
        regLoc=pickle.load(all)
        tamreg=all.tell()
        tamarch=os.path.getsize(afl)
        cant=tamarch//tamreg
        inf = 0
        sup = cant-1
        while (inf<=sup) and bandera==0: 
            med = int((inf+sup)//2)
            all.seek(med*tamreg,0)
            regLoc=pickle.load(all)
            if(regLoc.nombreLocal==elem):
                bandera=1
            else:
                if(regLoc.nombreLocal<elem):
                    inf=med+1
                    
                else:
                    sup=med-1
        all.close()
        return bandera

#----------------------------BUSQUEDAS-----------------------------
def buscadorLoc(cod): #NO TOCAR, JUSTIN TE MATA SI LO HACES
    all=open(afl,"r+b")
    all.seek(0,0)
    point=all.tell()
    regLoc=locales()
    regLoc=pickle.load(all)
    all.seek(0,0)
    point=all.tell()
    while regLoc.codLocal!=cod:
        point=all.tell()
        regLoc=pickle.load(all)
    return point


#----------------------------ORDEN EN LA SALA-----------------------------
def orden():  #ordena por campo codigo 
    all = open(afl, "r+b")
    all.seek (0, 0)
    aux = pickle.load(all)
    tamReg = all.tell() 
    tamArch = os.path.getsize(afl)
    cantReg = int(tamArch / tamReg)
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            all.seek (i*tamReg, 0)
            auxi = pickle.load(all)
            all.seek (j*tamReg, 0)
            auxj = pickle.load(all)
            if (auxi.nombreLocal > auxj.nombreLocal):
                all.seek (j*tamReg, 0)
                pickle.dump(auxi, all)
                all.seek (i*tamReg, 0)
                pickle.dump(auxj, all)
                all.flush()
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
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()
    #print(matriz[0])
    #print(matriz[1])

#----------------------------CONTADURIA RUBROS-----------------------------
def rubros():
    global rubrolocal
    all=open(afl,"r+b")
    all.seek(0,0) 
    regLoc=locales()
    size=os.path.getsize(afl)
    rubrolocal = [[0] * 3 for i in range(2)]
    rubrolocal[0][0]="Indumentaria"
    rubrolocal[0][1]="Perfumeria"
    rubrolocal[0][2]="Comidas"
    #regLoc=pickle.load(all)
    while all.tell()<size:
        regLoc=pickle.load(all)
        if (regLoc.estado == "A"):
            match regLoc.rubroLocal.rstrip():
                case "Indumentaria":
                    rubrolocal[1][0] += 1
                case "Perfumeria":
                    rubrolocal[1][1] += 1
                case "Comidas":
                    rubrolocal[1][2] += 1


    orden_rub(rubrolocal)

#----------------------------CARGA LOCALES-----------------------------
def crear_locales():
    global k,i, shopping_loc,codloc,bandera, med,rubroLocal,rub1,rub2,rub3,all,afl,regLoc#dejar codloc
    k = 0
    
    alu = open (afu,"r+b")
    regUser=pickle.load(alu)
    size=os.path.getsize(afl)
    all = open (afl,"r+b")
    regLoc=locales()

    exit = "S" 
    while exit.upper() == "S":

        if(size==0):
            bandera=0
        else:
            bandera=1
            

        valor = input("Ingrese el Nombre del Local: ").ljust(100)
        while valor=="":
            valor = input("No se permiten espacios vacios. Pruebe nuevamente: ").ljust(100)
        

        while bandera==1:
            bandera=buscadicotomica(valor)
            while (bandera == 1 or valor==""):
                if(valor==""):
                    valor = input("No se permiten espacios vacios. Pruebe nuevamente: ").ljust(100)
                    bandera=1
                else:
                    valor = input("Este nombre ya existe. Pruebe nuevamente: ").ljust(100)
                    bandera=buscadicotomica(valor) 

        all.seek(0,2)
        regLoc.nombreLocal = valor
        

        ubi = input("\nIngrese la UBICACIÓN: ").ljust(100)
        while ubi== "":
            ubi = input("No se permiten espacios vacios: ").ljust(100)
        regLoc.ubicacionLocal=ubi.ljust(100)


        rubro = input('\nIngrese el' + Fore.WHITE + Style.BRIGHT + ' RUBRO' + Style.RESET_ALL + Fore.YELLOW + '\n1_ ' + Fore.RESET +'Indumentaria' + Fore.YELLOW + '\n2_ '+ Fore.RESET +'Perfumeria'+ Fore.YELLOW +  '\n3_ '+ Fore.RESET + 'Comidas\n\nOPCION: ')
        #campo = int(input('\nIngrese el campo que desea' + Fore.WHITE + Style.BRIGHT + ' Modificar' + Style.RESET_ALL + Fore.YELLOW + '\n1_ ' + Fore.RESET + 'Nombre' + Fore.YELLOW + '\n2_ ' + Fore.RESET + 'Ubicación' + Fore.YELLOW + '\n3_ ' + Fore.RESET + 'Rubro' + Fore.YELLOW + '\n4_ ' + Fore.RESET + 'Código de usuario' + Fore.YELLOW + '\n0_ ' + Fore.RESET + 'Volver\n\nOPCION: '))

        while rubro!= "1" and rubro != "2" and rubro != "3":
            rubro = input("Mal ingresado. Repetir opción. OPCION: ")
        match rubro:
            case "1":
                regLoc.rubroLocal="Indumentaria".ljust(12)
            case "2":
                regLoc.rubroLocal="Perfumeria".ljust(12)
            case "3":
                regLoc.rubroLocal="Comidas".ljust(12)    
            

        size= os.path.getsize(afu)
        bandera=0
        print(regUser.cod)
        cod = int(input("\nIngrese el CÓDIGO de dueño de local: "))
        while bandera==0:
            alu.seek(0,0)
            while alu.tell() < size and regUser.tipo!="Dueño de local" and regUser.cod!=cod:
                regUser = pickle.load(alu)
            if(regUser.tipo=="Dueño de local" and regUser.cod==cod):
                bandera=1
            else:
                cod = int(input("El codigo no pertenece a un dueño o no existe. Repetir código. CÓDIGO: "))
        regLoc.codUsuario=cod
        regLoc.estado="A"
        codloc=codloc+1
        regLoc.codLocal=codloc

        pickle.dump(regLoc, all)
        all.flush()
        size=os.path.getsize(afl)
        orden()

        exit = input("\n ¿Desea seguir cargando? (S/N): ")
        while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ")
                #gestion_locales()


    all.flush()
    if (size!=0):
        orden()
    locales_cargados()
    
    #rubros()
    exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    enter(gestion_locales())
    
    alu.close()
    all.close()

#----------------------------MODIFICATIO LOCALATIO-----------------------------
def modificar_local():
    global bandera, med,campo,codloc,coduser,rubrolocal,codLoc
 #ver que pasa si no hay locales cargados
    
    all=open(afl,"r+b")
    regLoc=locales()
    all.seek(0,0)
    size=os.path.getsize(afl)
    orden()
    bandera=1
    while bandera==1:
        codLoc=int(input('\nIngrese el código del local a' + Fore.WHITE + Style.BRIGHT + ' Modificar' + Fore.RESET + Style.RESET_ALL + ': '))
        bandera=valid_codLoc(codLoc)
    
    point=buscadorLoc(codLoc)
    all.seek(point,0)

    if (regLoc.estado =="B"):
        alta = input("\nEste local esta dado de baja. ¿Desea activarlo? (S/N): ").upper()
        while alta.upper() != "S" and alta.upper() != "N":
            alta = input("\nRespuesta inválida. ¿Desea activarlo? (S/N): ")
        if (alta=="S"):
            regLoc.estado="A" 

    campo = int(input('\nIngrese el campo que desea' + Fore.WHITE + Style.BRIGHT + ' Modificar' + Style.RESET_ALL + Fore.YELLOW + '\n1_ ' + Fore.RESET + 'Nombre' + Fore.YELLOW + '\n2_ ' + Fore.RESET + 'Ubicación' + Fore.YELLOW + '\n3_ ' + Fore.RESET + 'Rubro' + Fore.YELLOW + '\n4_ ' + Fore.RESET + 'Código de usuario' + Fore.YELLOW + '\n0_ ' + Fore.RESET + 'Volver\n\nOPCION: '))
    campo=valid_campo(campo)
    
  
    all.seek(point,0)
    regLoc=pickle.load(all)
    codLoc=regLoc.codLocal
    valor=regLoc.nombreLocal.ljust(100)
    ubi=regLoc.ubicacionLocal.ljust(100)
    rubro=regLoc.rubroLocal.ljust(12)
    coduser=regLoc.codLocal
    estado=regLoc.estado

    while campo!= 0:
        match campo:
            case 1: #NOMBRE
                bandera=0
                valor = input("Ingrese el Nombre del Local: ").ljust(100)
                while valor=="":
                    valor = input("No se permiten espacios vacios. Pruebe nuevamente: ").ljust(100)
                while bandera==1:
                    bandera=buscadicotomica(valor)
                    while (bandera == 1 or valor==""):
                        if(valor==""):
                            valor = input("No se permiten espacios vacios. Pruebe nuevamente: ").ljust(100)
                            bandera=1
                        else:
                            valor = input("Este nombre ya existe. Pruebe nuevamente: ").ljust(100)
                            bandera=buscadicotomica(valor)

            case 2:  #UBICACION
                ubi = input("\nIngrese la UBICACIÓN: ").ljust(100)
                while ubi== "":
                    ubi = input("No se permiten espacios vacios: ").ljust(100)

            case 3: #RUBRO
                rubro = input('\nIngrese el' + Fore.WHITE + Style.BRIGHT + ' RUBRO' + Style.RESET_ALL + Fore.YELLOW + '\n1_ ' + Fore.RESET +'Indumentaria' + Fore.YELLOW + '\n2_ '+ Fore.RESET +'Perfumeria'+ Fore.YELLOW +  '\n3_ '+ Fore.RESET + 'Comidas\n\nOPCION: ')
                while rubro!= "1" and rubro != "2" and rubro != "3":
                    rubro = input("Mal ingresado. Repetir opción. OPCION: ")
                all.seek(point,0)
                match rubro:
                    case "1":
                        rubro="Indumentaria".ljust(12)
                    case "2":
                        rubro="Perfumeria".ljust(12)
                    case "3":
                        rubro="Comidas".ljust(12)   

            case 4: #CODIGO
                bandera=0
                alu=open(afl,"r+b")
                alu.seek(0,0)
                regUser=user()
                size=os.path.getsize(afu)
                coduser = int(input("\nIngrese el CÓDIGO de usuario: "))
                while alu.tell()<size and regUser.tipo!="Dueño de Local" and regUser.cod!=coduser and bandera==1:#recorre user p/ver si existe el codigo con dueño de local
                    regUser=pickle.load(alu)
                if(regUser.tipo=="Dueño de Local" and regUser.cod!=coduser):
                    bandera=0
                else:
                    coduser = int(input("\nNo existe el codigo, Ingrese nuevamente: "))
                    bandera=1
                    alu.seek(0,0)
        campo = int(input('\nIngrese el campo que desea' + Fore.WHITE + Style.BRIGHT + ' Modificar' + Style.RESET_ALL + Fore.YELLOW + '\n1_ ' + Fore.RESET + 'Nombre' + Fore.YELLOW + '\n2_ ' + Fore.RESET + 'Ubicación' + Fore.YELLOW + '\n3_ ' + Fore.RESET + 'Rubro' + Fore.YELLOW + '\n4_ ' + Fore.RESET + 'Código de usuario' + Fore.YELLOW + '\n0_ ' + Fore.RESET + 'Volver\n\nOPCION: '))
        campo=valid_campo(campo)
    
    
    
    
    all.seek(point,0)
    regLoc.codLocal=codLoc
    regLoc.nombreLocal=valor.ljust(100)
    regLoc.ubicacionLocal=ubi.ljust(100)
    regLoc.rubroLocal=rubro.ljust(12)
    regLoc.codLocal=coduser
    regLoc.estado=estado
 
    pickle.dump(regLoc,all)
    all.flush()
    all.seek(point,0)
    orden()
    locales_cargados()
    print()
    centrar_texto(Fore.GREEN + Style.BRIGHT + Back.BLACK + 'La modificación fue EXITOSA.')
    print()
    rubros()
    exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    enter(gestion_locales())


#----------------------------ELIMINATION LOCALATIO-----------------------------
def eliminar_loc():
    all=open(afl,"r+b")
    regLoc=locales()

    bandera=1
    while bandera==1:
        codLoc=int(input(f"Ingrese el código del local a {Fore.RED + 'Eliminar:' }{Style.RESET_ALL}"))
        bandera=valid_codLoc(codLoc)

    point=buscadorLoc(codLoc)
    all.seek(point,0)
    regLoc=pickle.load(all)
    codLoc=regLoc.codLocal
    valor=regLoc.nombreLocal.ljust(100)
    ubi=regLoc.ubicacionLocal.ljust(100)
    rubro=regLoc.rubroLocal.ljust(12)
    coduser=regLoc.codLocal
    estado=regLoc.estado

    if (regLoc.estado == "A"):
        baja = input("Este local esta activo. ¿Desea darlo de baja? (S/N): ").upper()
        while baja.upper() != "S" and baja.upper() != "N":
            baja = input("Respuesta inválida. ¿Desea darlo de baja? (S/N): ")
        if (baja=="S"):
            estado="B" 

    all.seek(point,0)
    regLoc.codLocal=codLoc
    regLoc.nombreLocal=valor.ljust(100)
    regLoc.ubicacionLocal=ubi.ljust(100)
    regLoc.rubroLocal=rubro.ljust(12)
    regLoc.codLocal=coduser
    regLoc.estado=estado
    pickle.dump(regLoc,all)
    all.flush()
    all.seek(point,0)
    
    #print("El local", regLoc.codLocal, "fue dado de baja.")
    codStr=str(regLoc.codLocal)
    print(f"El local {Fore.RED + codStr}{Style.RESET_ALL} fue dado de baja.")
    
    orden()
    rubros()
    orden_rub(rubrolocal)

    exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    enter(gestion_locales())

#------------------------GESTIONES-------------------------
def gestion_locales(): 
    size=os.path.getsize(afl)
    if (size==0):
        all = open (afl,"w+b")
    else:
        all = open (afl,"r+b")
        regLoc=pickle.load(all)
    all.seek(0,0)#out of range ijo epuuuu
    size=os.path.getsize(afl)
    pantalla_locales()
    valid_opc_loc()
    match opcloc:
        case "a":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Crear locales---")
            exit = input('\n ¿Desea ver los locales cargados? ('+ Fore.GREEN + 'S' + Fore.WHITE + '/' + Fore.RED + 'N'+ Fore.WHITE+'): ').upper()
            
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            size=os.path.getsize(afl)
            if exit=="S" and size==0:
                centrar_texto(Fore.WHITE + Style.BRIGHT + "No hay locales cargados hasta el momento.")
            else:
                if exit=="S":
                    locales_cargados()
            if(contowner==0):
                centrar_texto(Style.BRIGHT + "No hay dueños registrados. Primero debe crear una cuenta de dueño de local...")
                exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
                exit(gestion_locales())
            else:
                crear_locales()
        case "b":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Modificar locales---")
            exit = input('\n ¿Desea ver los locales cargados? ('+ Fore.GREEN + 'S' + Fore.WHITE + '/' + Fore.RED + 'N'+ Fore.WHITE+'): ').upper()

            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            size=os.path.getsize(afl)
            
            if exit=="S" and size==0:
                centrar_texto(Fore.WHITE + Style.BRIGHT + "No hay locales cargados hasta el momento.")
            else:
                if exit=="S" and size!=0:
                    locales_cargados()
                    modificar_local()
            if(size!=0 and exit=="N"):
                modificar_local()
            gestion_locales()
        case "c":
            clear_screen()
            print("---Eliminar locales---")
            exit = input("\n ¿Desea ver los locales cargados? (S/N): ").upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            size=os.path.getsize(afl)
            if exit=="S" and size==0:
                print("\n       No hay locales cargados hasta el momento.")
            else:
                if exit=="S" and size!=0:
                    locales_cargados()
                    eliminar_loc()
            gestion_locales()

        case "d":
            clear_screen()
            mapa(shopping_loc)
            exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
            enter(gestion_locales())
        case "e":
            menu_admin()
    all.close()     

#-------------------------LOGIN----------------------------
def login():
    global name,cont,cod
    alu = open (afu, "r+b")
    regUser=user()
    alu.seek(0,0)
    regUser=pickle.load(alu)
    size=os.path.getsize(afu)
    correcto=0
    cont=1
    clear_screen()
    centrar_texto(Fore.MAGENTA+Style.BRIGHT+"---Log In---")
    print()
    nombre=centrar_input("Ingrese el nombre: ")

    ancho_consola, _ = shutil.get_terminal_size()
    espacio_adicional = max(0, (ancho_consola  - 33) // 2)
    texto_centrado =  " " * espacio_adicional +"Ingresar contraseña: "

    password = maskpass.askpass(prompt=texto_centrado, mask="*")
    
    while correcto!=1 and cont<3:
        alu.seek(0,0)
        bandera=0
        while(alu.tell() < size) and bandera==0:
            if(regUser.usuario.rstrip()==nombre):             
                if(regUser.clave.rstrip()==password.rstrip()):
                    bandera=1
                else:
                    regUser=pickle.load(alu)
            else:
                regUser=pickle.load(alu)

        if(regUser.usuario.rstrip()==nombre.rstrip() and regUser.clave.rstrip()==password.rstrip()):  
            correcto=1
        else:
            nombre=centrar_input("Ingrese el nombre: ")
            password = maskpass.askpass(prompt=texto_centrado, mask="*")

            cont=cont+1 #=?????
            alu.seek(0,0)
    if (regUser.usuario.rstrip()==nombre.rstrip() and regUser.clave.rstrip()==password.rstrip()):  
            correcto=1    
    if(correcto==1):
        name=regUser.usuario.rstrip()
        cod=regUser.cod
        select_menu(regUser.tipo.rstrip())
    else:
        centrar_texto(Fore.RED+Style.BRIGHT+"Cantidad de MAXIMA de intentos permitidos")

    alu.close()

#-------------------------SIGN IN----------------------------
def signin(user1):
    global contuser

    alu = open (afu, "r+b")
    regUser= user()
    size=os.path.getsize(afu)
    flag=0
    centrar_texto(Fore.MAGENTA+Style.BRIGHT+"---Sign In---")
    print()
    nombre=centrar_input("Ingrese el nombre: ")
    ancho_consola, _ = shutil.get_terminal_size()
    espacio_adicional = max(0, (ancho_consola  - 50) // 2)
    texto_centrado =  " " * espacio_adicional +"Ingrese una contraseña con 8 caracteres: "
    texto_centrado2 =  " " * espacio_adicional +Fore.RED+"La contraseña debe contener 8 caracteres: "+Fore.RESET



    while flag!=1:
        alu.seek(0,0)
        while(alu.tell() < size) and (regUser.usuario.rstrip()!=nombre.rstrip()):
            regUser=pickle.load(alu)
        if(regUser.usuario.rstrip()==nombre.rstrip()):  
            nombre=centrar_input(Fore.RED+"      Ese nombre ya existe. Ingrese el nombre: "+Fore.RESET)
            print()
        else:
            flag=1
            alu.seek(0,0)

    password = maskpass.askpass(prompt=texto_centrado, mask="*")
    while len(password)!=8:
        password = maskpass.askpass(prompt=texto_centrado2, mask="*")

    alu.seek(0,2)
    contuser=contuser+1
    regUser.cod=contuser
    regUser.usuario = nombre.ljust(100)
    regUser.clave = password.ljust(8)
    regUser.tipo = user1.ljust(14)
    pickle.dump(regUser,alu)
    alu.flush()
    alu.close()
    usercargados()
    exit = input("Toque Enter para volver. ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER. ")
    centrar_texto(Fore.GREEN + Style.BRIGHT + 'La cuenta ha sido creada EXITOSAMENTE!')
    time.sleep(1.7)

#-------------------------MENU'S----------------------------
def menu_admin():
   global contowner
   barracarga()
   pantalla_adm()
   valid_adm()
   match opcadm:
      case "1":
        #clear_screen()
        gestion_locales()
        #orden_rub(shopping_loc)
      case "2":
        clear_screen()
        centrar_texto(Fore.WHITE + Style.BRIGHT + '---Crear cuentas de dueños de locales---')
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
        mainMenu()

        """ centrar_texto(chau_franchu)
        exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
        while exit != "":
                exit = input("Respuesta inválida. Presione ENTER: ")
        print("\nSaliendo...") """


#Main Menu
def mainMenu():
    clear_screen()
    mostrar_menu()
    ingreso_main_menu(valid_opc())

def PP():
    mainMenu()

PP()







