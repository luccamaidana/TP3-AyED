global cont,contowner,codloc, codpromo, dias
cont=2
contowner=0
codloc=1
codpromo=0
dias = [0]*7

#------------------------IMPORT-------------------------------
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
        self.diasSemana = dias
        self.estado = ""
        self.codLocal = 0
        self.cantUsoPromo= 0

class uso_promociones: 
    def __init__(self):
        self.codCliente = 0
        self.codPromo = ""
        self.fechaUsoPromo = ""
"""        self.cantUsoPromo= 0"""

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
#afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
afu = "D:\\Descargas\\Facultad\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

#locales
#afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
#afl = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\LOCALES.dat"
afl = "D:\\Descargas\\Facultad\\TP3-AyED\\LOCALES.dat"
all = open (afl, "w+b") 
regLoc = locales()

#promos
#afp = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\PROMOCIONES.DAT"
#afp = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\PROMOCIONES.DAT"
afp = "D:\\Descargas\\Facultad\\TP3-AyED\\PROMOCIONES.DAT"
alp = open (afp, "w+b")
regProm = promociones()


#uso promos
#afup = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USO_PROMOCIONES.DAT"
#afup = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USO_PROMOCIONES.DAT"
afup = "D:\\Descargas\\Facultad\\TP3-AyED\\USO_PROMOCIONES.DAT"
alup = open (afup, "w+b")
regUP = uso_promociones()

#novedades
#afn = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\NOVEDADES.DAT"
#afn = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\NOVEDADES.DAT"
afn = "D:\\Descargas\\Facultad\\TP3-AyED\\NOVEDADES.DAT"
aln = open (afn, "w+b")
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

regProm.codPromo=0
regProm.textoPromo=""
regProm.fechaDesdePromo=""
regProm.fechaHastaPromo=""
regProm.diasSemana=""
regProm.estado=""
regProm.codLocal=0


alp.flush()
alp.close()

regLoc.codLocal=0
regLoc.nombreLocal=""
regLoc.ubicacionLocal=""
regLoc.rubroLocal=""
regLoc.codUsuario=0
regLoc.estado=""
pickle.dump(regLoc, all)

all.flush()
all.close()

regUP.codCliente = 0
regUP.codPromo = ""
regUP.fechaUsoPromo = ""
regUP.cantUsoPromo=0
pickle.dump(regUP, alup)

alup.flush()
alup.close()
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
    global name
    clear_screen()
    print("        Menú ADMIN")
    print("      Bienvenido",name)   
    print("\nIngrese una opcion 0-5\n")
    print("1_ Gestión de locales")
    print("2_ Crear cuentas de dueños de locales")
    print("3_ Aprobar / Denegar solicitud de descuento")
    print("4_ Gestión de novedades")
    print("5_ Reporte de utilización de descuentos")
    print("0_ Volver al menú principal")

def pantalla_owner():
    global name
    clear_screen()
    print("        Menú de Dueño")
    print("       Bienvenido",name)
    print("\nIngrese una opcion 0-3\n")
    print("1_ Crear descuento")
    print("2_ Reporte de uso de descuento")
    print("3_ Ver novedades") #SOLO CHAPIN
    print("0_ Salir")

def pantalla_costumer():
    global name
    clear_screen()
    print("        Menú de Cliente")
    print("       Bienvenido",name)
    print("\nIngrese una opcion 0-3\n")
    print("1_ Buscar descuentos en local")
    print("2_ Solicitar descuento")
    print("3_ Ver novedades") #SOLO CHAPIN
    print("0_ Salir")


def pantalla_locales():
    print("\n        Gestión de locales")
    print("\nIngrese una opción a-d\n")
    print("a- Crear locales")
    print("b- Modificar local")
    print("c- Eliminar local")
    print("d- Mapa de locales")
    print("e- Volver")

def barracarga():
    clear_screen()
    print(Style.BRIGHT + "         CARGANDO...")
    bar_len = 25
    elements = ['-','\\', '|', '/']
    for i in range(bar_len+1):
        frame =i%len(elements)
        print(Fore.GREEN + Style.BRIGHT + f'\r[{elements[frame]*i:=^{bar_len}}]', end='')
        time.sleep(0.1)



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
def locales_cargados(): #agregar linduras p/
    all = open (afl,"r+b")
    size= os.path.getsize(afl)

    while all.tell() < size:
        regLoc = pickle.load(all)
        print(regLoc.codLocal,regLoc.nombreLocal,regLoc.ubicacionLocal,regLoc.rubroLocal,regLoc.codUsuario,regLoc.estado)
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

def valid_owner():
    global opcown
    opcown = input("\nOPCION: ")
    while opcown != "1" and opcown != "2" and opcown != "3" and opcown != "0":
        opcown = input("Mal ingresado. Repetir opción. OPCION: ")
    clear_screen()

def valid_costumer():
    global opccostumer
    opccostumer = input("\nOPCION: ")
    while opccostumer != "1" and opccostumer != "2" and opccostumer != "3" and opccostumer != "0":
        opccostumer = input("Mal ingresado. Repetir opción. OPCION: ")
    clear_screen()

def valid_opc_loc():
    global opcloc
    opcloc = input("\nOPCION: ")
    opcloc = opcloc.lower()
    while opcloc != "a" and opcloc != "b" and opcloc != "c" and opcloc != "d" and opcloc != "e":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")
        opcloc = opcloc.lower()
    clear_screen()

def valid_dia(opcdia):
    opcdia = opcdia.upper()
    while opcdia != "LUNES" and opcdia != "MARTES" and opcdia != "MIERCOLES" and opcdia != "JUEVES" and opcdia != "VIERNES" and opcdia != "SABADO" and opcdia != "DOMINGO":
        opcdia = input("Mal ingresado. Repetir opción: ")
        opcdia = opcdia.upper()
    
def valid_fecha(fecha_str):
    es_valida = 1
    partes = fecha_str.split('/')
    if len(partes) != 3:
        es_valida = 0
    else:
        día, mes, año = map(int, partes)
        if año < 2023 or mes < 1 or mes > 12 or día < 1:
            es_valida = 0
        else:
            if día > 31 or (mes in [4, 6, 9, 11] and día > 30) or (mes == 2 and (año % 4 != 0 or (año % 100 == 0 and año % 400 != 0)) and día > 28) or (mes == 2 and día > 29):
                es_valida = 0
    
    return es_valida

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

#----------------------------CASE-----------------------------
def select_menu(m):
    match m:
        case "Administrador":
            menu_admin()
        case "Dueño de local":
            menu_owner()
        case "Cliente":
            menu_costumer()

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

#----------------------------ORDEN EN LA SALA-----------------------------
def orden(archivo,archfis,campo):#duda si parametro y duda si seek 0,0 #sacar parametros si no funca
    archivo.seek(0,0)
    reg=pickle.load(archivo)   
    tamreg=archivo.tell()
    tamarch=os.path.getsize(archfis)  
    cantreg=tamarch//tamreg #cantidad de "filas"
    i=0
    j=0
    for i in range (cantreg-1):
            for j in range(i+1,cantreg):
                if archivo.campo[i]>archivo.campo[j]:#ver si parametro .nombreloc
                        aux = archivo[i]
                        archivo[i] = archivo[j]
                        archivo[j] = aux

def orden_rub(matriz):
    i=0
    j=1
    k=0
    aux=[]
    for i in range(len(matriz)-1):
            for j in range(i+1,len(matriz)):
                if matriz[1][i] != "" and matriz[1][j] != "" and (matriz[1][i]<matriz[1][j]):
                    for k in range (1):
                        aux = matriz[k][i]
                        matriz[k][i] = matriz[k][j]
                        matriz[k][j] = aux
    locales_cargados()

#----------------------------CONTADURIA RUBROS-----------------------------
def rubros():
    all.seek(0,0)
    reg=pickle.load(all)   
    size=os.path.getsize(afl)
    rubrolocal = [[0] * 2 for i in range(3)]
    rubrolocal[0][0]="Indumentaria"
    rubrolocal[0][1]="Perfumeria"
    rubrolocal[0][2]="Comidas"
    for i in range (size):
        if reg.estado[i] == "A":

            if reg.rubroLocal[i] == "Indumentaria":
                rubrolocal[1][0] += 1

            elif reg.rubroLocal[i] == "Perfumeria":
                rubrolocal[1][1] += 1

            elif reg.rubroLocal[i] == "Comidas":
                rubrolocal[1][2] += 1

    orden(rubrolocal)

#----------------------------CARGA LOCALES-----------------------------
def crear_locales():
    global k,i, shopping_loc,codloc,bandera, med,rubroLocal,rub1,rub2,rub3#dejar codloc
    k = 0
    alu = open (afu,"r+b")
    regUser=pickle.load(alu)
    all = open (afl,"r+b")
    regLoc=pickle.load(all)
    exit = "S" 
    while exit.upper() == "S":

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
        regLoc.estado="A"
        codloc=codloc+1
        regLoc.codLocal=codloc



        orden(all,afl,"nombreLoc")#agregar archivo ordenar 

        exit = input("\n ¿Desea seguir cargando? (S/N): ")
        while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ")
                gestion_locales()

    pickle.dump(regLoc, all)
    all.flush()
    orden(all,afl,"nombreLoc") #ojo al nombre local
    locales_cargados()
    
    rubros()
    exit = input("\n Toque Enter para volver: ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER: ")
    if exit=="": 
        clear_screen()
        gestion_locales()
    alu.close()
    all.close()
#standby recordar close ambos alu afu 

#------------------------GESTIONES-------------------------
def gestion_locales(): 
    
    global shopping_loc, i
    all = open (afl,"r+b")
    all.seek(0,0)#out of range ijo epuuuu
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
            if exit=="S" and size==0:
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

#------------------------MENU OWNER------------------------------------------------------------------------------------------
def carga_dias(matriz,day):
    matriz = [0]*7
    d = day.upper()
    match d:
        case "LUNES":
            matriz[0]=1
        case "MARTES":
            matriz[1]=1
        case "MIERCOLES":
            matriz[2]=1
        case "JUEVES":
            matriz[3]=1
        case "VIERNES":
            matriz[4]=1
        case "SABADO":
            matriz[5]=1
        case "DOMINGO":
            matriz[6]=1
    return (matriz)

def crear_descuento():
    global nombredia, fecha_actual, fecha_formateada, nombredia, codpromo, dias
    bandera=0

    size = os.path.getsize(afp)

    alp = open (afp, "r+b")
    all = open (afl, "r+b")
    alu = open(afu, "r+b")
    alp.seek(0,0)
    all.seek(0,0)  
    alu.seek(0,0)
    regProm = promociones()
    regLoc = locales()
    regUser = user()
    regProm = pickle.load(alp)
    regLoc = pickle.load(all)
    regUser = pickle.load(alu)


    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

    if regLoc.codLocal == 0:
        print("\nNo existen locales creados. Cree uno para poder continuar.")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_owner()
    
    size = os.path.getsize(afp)
    if size==0:
        print("No hay promociones cargadas aún.")
    else:
        while (alp.tell() < size) and (regUser.cod==regLoc.codUsuario) and (regProm.codLocal == regLoc.codLocal) and (regLoc.estado == "A") and (regProm.fechaDesdePromo>=fecha_formateada) and (regProm.fechaHastaPromo<=fecha_formateada):
            regProm = pickle.load(alp)
            print("\nLas promociones del local", regLoc.nombreLocal,"son:")
            print("Codigo de la promoción:", regProm.codPromo)
            print("Texto de la promoción:", regProm.textoPromo)
            print("Promoción valida desde:", regProm.fechaDesdePromo)
            print("Promoción valida hasta:", regProm.fechaHastaPromo)
            if (regProm.fechaDesdePromo>=fecha_formateada) and (regProm.fechaHastaPromo<=fecha_formateada):
                print("Promoción vigente.")
            else: 
                print("La promocin ya no se encuentra vigente.")
            print("Estado de la promoción:",regProm.estado)

    alp.seek(0,0)

    codigo=int(input("Identifique el codigo del local al que quiere cargar un descuento: "))
    """while alp.tell() < size and codigo!=regLoc.codLocal and bandera==0:
        regLoc = pickle.load(all)
        if (codigo!=regLoc.codLocal): 
            codigo=int(input("Código de local no válido, volver a ingresar. CÓDIGO: "))
            alp.seek(0,0)

    bandera=1"""

    exitmain="S"
    while valid_codLoc(codigo)==0 and exitmain=="S":
        alp.seek(0,2)
        texto = input("Ingrese texto de la promocion: ")
        regProm.textoPromo = texto

        desde_str = input("Ingrese día que inicia la promoción: ")
        desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")
        regProm.fechaDesdePromo = desde.strftime("%d/%m/%Y")
        while desde <= fecha_actual and valid_fecha(desde_str)==0:
            desde_str = input("Fecha de inicio de la promoción no válida. Ingrese otra fecha: ")
            valid_fecha(desde_str)
            desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")
            regProm.fechaDesdePromo = desde.strftime("%d/%m/%Y")

        hasta_str = input("Ingrese día que finaliza la promoción: ")
        hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
        regProm.fechaHastaPromo = hasta.strftime("%d/%m/%Y")
        while desde > hasta and valid_fecha(hasta_str)==0:
            hasta_str = input("Fecha de finalización de la promoción no válida. Ingrese otra fecha: ")
            valid_fecha(hasta_str)
            hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
            regProm.fechaHastaPromo = hasta.strftime("%d/%m/%Y")

        regProm.estado = "Pendiente"

        regProm.codLocal=codigo

        regProm.codPromo=codpromo

        codpromo=codpromo+1

        
        
        exit="S"
        while exit=="S":
            dia=input("Dias habiles de la promocion: ")
            valid_dia(dia)
            carga_dias(dias, dia)
            regProm.diasSemana = dias
            exit=input("¿Desea cargar más dias? (S/N): ")
            exit=exit.upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ")
        
        exitmain=input("¿Desea cargar más promociones? (S/N): ")
        exitmain=exitmain.upper()
        while exitmain.upper() != "S" and exitmain.upper() != "N":
            exitmain = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ")
        
        pickle.dump(regProm, alp)
        alp.flush()

    print("¡Promoción/es creada/s exitosamente!")
    
    alp.close()
    alu.close()
    all.close()

def uso_descuento():
    alp = open (afp, "r+b")
    regProm = promociones()
    alup = open (afup, "r+b")
    regUP = pickle.load(alup)
    all = open(afl, "r+b")
    regLoc = pickle.load(all)
    alp.seek(0,0)
    all.seek(0,0)  
    alup.seek(0,0)

    size = os.path.getsize(afp)

    if size==0:
        print("\nNo hay promociones cargadas aún.")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_owner()

    regProm = pickle.load(alp)
    desde_str = input("Ingrese el primer dia del rango: ")
    desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")
    while regProm.fechaDesdePromo>=desde and valid_fecha(desde_str)==0:
        desde_str = input("Fecha de rango no válida. Ingrese otra fecha: ")
        valid_fecha(desde_str)
        desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")

    hasta_str = input("Ingrese el ultimo dia del rango: ")
    hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
    while regProm.fechaHastaPromo <= hasta and valid_fecha(hasta_str)==0:
        hasta_str = input("Fecha de rango no válida. Ingrese otra fecha: ")
        valid_fecha(hasta_str)
        hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")

    print(f"{'Codigo Promo':<15}{'Texto':<40}{'Fecha Desde':<15}{'Fecha Hasta':<15}{'Cant. Uso Promo':<15}")
    while alp.tell() < size and regProm.estado=="Aprobada" and regProm.codPromo==regUP.codPromo:
        if regProm.fechaDesdePromo>=desde and regProm.fechaHastaPromo<=hasta:
           print("Fecha desde:", desde,"    Fecha hasta:", hasta)
           print("Local", regLoc.codLocal,":", regLoc.nombreLocal)
           print(f"{regProm.codPromo:<15}{regProm.textoPromo:<40}{regProm.fechaDesdePromo:<15}{regProm.fechaHastaPromo:<15}{regProm.cantUsoPromo:<15}")
        regProm = pickle.load(alp)
            
            
        """print("Fecha desde: ", desde,"    Fecha hasta: ", hasta)
        print("Local ", regLoc.codLocal,": ", regLoc.nombreLocal) #mal
        print(regProm.codPromo)
        print(regProm.textoPromo)
        print(regProm.fechaDesdePromo)
        print(regProm.fechaHastaPromo)
        print(regUP.cantUsoPromo)"""
    
    alp.close()
    all.close()
    alup.close()

    exit = input("\n Toque Enter para volver. ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER. ")
    if exit=="": 
        menu_owner()
    
#------------------------MENU CLIENTE------------------------------------------------------------------------------------------
def num_dias(day):
    match day:
        case "Monday":
            num_dia=0
        case "Tuesday":
            num_dia=1
        case "Wednesday":
            num_dia=2
        case "Thursday":
            num_dia=3
        case "Friday":
            num_dia=4
        case "Saturday":
            num_dia=5
        case "Sunday":
            num_dia=6
    return num_dia

def buscadorLoc(cod): #NO TOCAR, JUSTIN TE MATA SI LO HACES
    alp=open(afp,"r+b")
    alp.seek(0,0)
    point=alp.tell()
    regProm=promociones()
    regProm=pickle.load(alp)
    alp.seek(0,0)
    point=alp.tell()
    while regProm.codPromo!=cod:
        point=alp.tell()
        regProm=pickle.load(alp)
    return point

def buscardesc():
    global fecha_actual
    bandera=0
    alp = open (afp, "r+b")
    alp.seek(0,0)

    size = os.path.getsize(afp) 
    if size == 0:
        print("No hay promociones creadas")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_costumer()

    regProm = pickle.load(alp)

    codigo=int(input("Identifique el codigo del local para buscar descuentos: "))
    while alp.tell() < size and codigo!=regProm.codLocal and bandera==0:
        regProm = pickle.load(alp)
        if (codigo!=regProm.codLocal): 
            codigo=int(input("Código de local no válido, volver a ingresar. CÓDIGO: "))
            alp.seek(0,0)
    bandera = 1 #creo que la bandera es al pedo

    if regProm.codLocal==regLoc.codLocal and regProm.cod==0:
        print("El local no tiene promociones creadas.")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_costumer()

    fecha_str = input("Ingrese una fecha para buscar descuentos: ")
    fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
    while fecha >= fecha_actual and valid_fecha(desde_str)==0:
        fecha_str = input("Fecha no válida. Ingrese otra fecha: ")
        valid_fecha(fecha_str)
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

    dia_semana = fecha.strftime("%A")

    alp.seek(0,0)

    print(f"{'Codigo Promo':<15}{'Texto':<40}{'Fecha Desde':<15}{'Fecha Hasta':<15}")
    while alp.tell() < size and regProm.codLoc==codigo and regProm.estado=="Aprobado" and fecha >= regProm.fechaDesdePromo and fecha <= regProm.fechaHastaPromo and regProm.diasSemana[num_dias(dia_semana)]==1:
        print(f"{regProm.codPromo:<15}{regProm.textoPromo:<40}{regProm.fechaDesdePromo:<15}{regProm.fechaHastaPromo:<15}")
        regProm = pickle.load(alp)   
        
        """print("\nLas promociones del local", regLoc.nombreLocal,"son:")
        print("Codigo de la promoción:", regProm.codPromo)
        print("Texto de la promoción:", regProm.textoPromo)
        print("Promoción valida desde:", regProm.fechaDesdePromo)
        print("Promoción valida hasta:", regProm.fechaHastaPromo)"""
    
    alp.close()

def solicitardesc():
    global fecha_formateada
    alp = open (afp, "r+b")
    alp.seek(0,0)  
    regProm = promociones()
    alup = open (afup, "r+b")
    alup.seek(0,0)
    regUP = uso_promociones()
    alu = open (afu, "r+b")
    alu.seek(0,0)  
    regUser = pickle.load(alu)

    size = os.path.getsize(afp) 
    if size == 0:
        print("No hay promociones creadas")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_costumer()

    regProm = pickle.load(alp)
    
    dia_semana = fecha_formateada.strftime("%A")

    codigo=int(input("Código de la promoción: "))
    while alp.tell() < size and codigo!=regProm.codPromo:
        regProm = pickle.load(alp)
        if (codigo!=regProm.codPromo): 
            codigo=int(input("Código de promoción no válido, volver a ingresar. CÓDIGO: "))
            alp.seek(0,0)

    while codigo==regProm.codPromo and regProm.estado=="Aprobado" and fecha_formateada >= regProm.fechaDesdePromo and fecha_formateada <= regProm.fechaHastaPromo and regProm.diasSemana[num_dias(dia_semana)]==1:
        regUP.codCliente = regUser.cod
        regUP.codPromo = codigo
        regUP.fechaUsoPromo = fecha_formateada
        point=buscadorLoc(codigo)
        alp.seek(point,0)
        regProm.cantUsoPromo = regProm.cantUsoPromo + 1
        
#-------------------------LOGIN----------------------------
def login():
    global name
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
        name=regUser.usuario
        select_menu(regUser.tipo)
    else:
        print("Cantidad de maxima de intentos permitidos")

    alu.close()
#-------------------------SIGN IN----------------------------

def signin(usuario):
    global cont
    alu = open (afu, "r+b")
    size=os.path.getsize(afu)
    regUser=user()
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
    regUser.tipo = usuario

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
        mainMenu()

def menu_owner():
    pantalla_owner()
    valid_owner()
    match opcown:
        case "1":
            clear_screen()
            print("Crear descuento")
            crear_descuento()
            menu_owner()
        case "2":
            clear_screen()
            print("Reporte de uso de descuento")
            uso_descuento()
        case "3":
            clear_screen()
            print("Ver novedades")
            print("\nDiagramado en chapin") 
            exit = input("Toque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="": 
                menu_owner()
        case "0":
            barracarga()
            mainMenu()

def menu_costumer():
    pantalla_costumer()
    valid_costumer()
    match opccostumer:
        case "1":
            clear_screen()
            print("Buscar descuentos en local")
            buscardesc()

        case "2":
            clear_screen()
            print("Solicitar descuento")
            solicitardesc()
            menu_owner()
        case "3":
            clear_screen()
            print("Ver novedades")
            print("\nDiagramado en chapin")
            exit = input("Toque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="": 
                menu_owner()
        case "0":
            barracarga()
            mainMenu()


def mainMenu():
    clear_screen()
    mostrar_menu()
    ingreso_main_menu(valid_opc())

def PP():
    mainMenu()

PP()
