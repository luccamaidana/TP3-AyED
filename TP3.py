global cont,contowner,codloc,regLoc,contuser,codpromo,dias
con=1 #cont 2 en el de valen? 
contuser=1
contowner=0
codloc=0
codpromo=1
contuser=1
dias = [0]*7


#------------------------IMPORT-------------------------------
import os
import pickle
import os.path
import io
import shutil
import maskpass
import math
import datetime
import time
import colorama
from colorama import Fore, Style, Back,init
# Inicializar colorama
colorama.init(autoreset=True)
init()


#--------------------------CLEAR SCREEN------------------------------
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
        self.codUsuario = 0
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
        self.codUsuario = 0

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
#afu="c:\tp3\USUARIOS.dat"
#afl="c:\tp3\LOCALES.dat"
#afp="c:\tp3\PROMOCIONES.DAT"
#afup="c:\tp3\USO_PROMOCIONES.DAT"



#afu = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USUARIOS.dat"
afu = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USUARIOS.dat"
#afu = "D:\\Descargas\\Facultad\\TP3-AyED\\USUARIOS.dat"
alu = open (afu, "w+b")
regUser = user()

#locales
#afl = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\LOCALES.dat"
afl = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\LOCALES.dat"
#afl = "D:\\Descargas\\Facultad\\TP3-AyED\\LOCALES.dat"
all = open (afl, "w+b") 
regLoc = locales()

#promos
#afp = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\PROMOCIONES.DAT"
afp = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\PROMOCIONES.DAT"
#afp = "D:\\Descargas\\Facultad\\TP3-AyED\\PROMOCIONES.DAT"
alp = open (afp, "w+b")
regProm = promociones()

#uso promos
#afup = "c:\\Users\\lucca\\Desktop\\UTN\\AyED\\TP\\TP3-AyED\\USO_PROMOCIONES.DAT"
afup = "c:\\Users\\Gaston\\Documents\\GitHub\\TP2-AyED\\TP3-AyED\\USO_PROMOCIONES.DAT"
#afup = "D:\\Descargas\\Facultad\\TP3-AyED\\USO_PROMOCIONES.DAT"
alup = open (afup, "w+b")
regUP = uso_promociones()

#-------------------------EL AJUSTE---------------------------






#-------------------------PRECARGAS/CARGAS---------------------------
#--------Locales-------------


#-------Usuarios----------
def precarga_admin():
    alu=open(afu,"w+b")
    alu.seek(0,0)
    size=os.path.getsize(afu)
    print(size)
    alu.flush
    user1= user
    pickle.dump(user,alu)
    alu.flush
    alu.seek(0,0)
    print("puntero",alu.tell())
    cod=1
    usuario="5".ljust(100)
    clave="6".ljust(8)
    tipo="Administrador".ljust(14)
    user1.cod=cod
    user1.usuario=usuario
    user1.clave=clave
    user1.tipo=tipo
    alu.seek(0,0)
    pickle.dump(user,alu)
    cod=1
    usuario="8".ljust(100)
    clave="9".ljust(8)
    tipo="fhdfhf".ljust(14)
    user1.cod=cod
    user1.usuario=usuario
    user1.clave=clave
    user1.tipo=tipo
    pickle.dump(user,alu)

    alu.flush()
    size=os.path.getsize(afu)
    print(size)
    

    print("puntero",alu.tell())
    
    alu.seek(0,0)
    while alu.tell()<size:
        print(user1)
        user1=pickle.load(alu)
        

    alu.close()
    exit = input("Toque Enter para volver. ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER. ")

precarga_admin()
exit = input("Toque Enter para volver. ")
while exit != "":
    exit = input("Respuesta inválida. Presione ENTER. ")

#------------------------PANTALLAS-------------------------
def centrar_texto(texto):
    ancho_consola, _ = shutil.get_terminal_size()
    espacio_adicional = max(0, (ancho_consola - len(texto)) // 2)
    texto_centrado = " " * espacio_adicional + texto
    print(texto_centrado)

def centrar_texto_var(texto, var):
    ancho_consola, _ = shutil.get_terminal_size()
    ancho_t = len(texto)
    ancho_v = len(var)
    espacio_disponible = ancho_consola - ancho_t - ancho_v
    espacio_adicional_izquierda = (espacio_disponible // 2) -5 
    espacio_adicional_derecha = espacio_disponible - espacio_adicional_izquierda
    texto_centrado = " " * espacio_adicional_izquierda + texto + var + " " * espacio_adicional_derecha 
    print(texto_centrado)

def mostrar_menu():
    
    fecha_actual = datetime.datetime.today()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

    ancho_ventana = shutil.get_terminal_size().columns

    menu_texto = "Menú"

    espacio_blancos = (ancho_ventana - len(menu_texto) - 2) // 2

    print("-" * ancho_ventana)
    print(f"|{' ' * espacio_blancos}{Fore.WHITE+Style.BRIGHT+menu_texto}{' ' * espacio_blancos}|")
    print("-" * ancho_ventana)
    print(fecha_formateada)
    print(Style.BRIGHT +'\nIngrese una opción ' +  Fore.YELLOW + '1-3\n')
    print(Style.BRIGHT + Fore.YELLOW + '1_' + Fore.WHITE + ' Ingresar con usuario registrado')
    print(Style.BRIGHT + Fore.YELLOW + '2_' + Fore.WHITE +' Registrarse como cliente')
    print(Style.BRIGHT + Fore.YELLOW + '3_' + Fore.WHITE +' Salir')

def pantalla_adm():
    global name
    clear_screen()
    centrar_texto(Style.BRIGHT  + Fore.WHITE +'Menú ADMIN')
    centrar_texto_var('Bienvenido, ',name)
    print(Style.BRIGHT +'Ingrese una opción ' +  Fore.YELLOW + '0-5\n')
    print(Style.BRIGHT + Fore.YELLOW + '1_' + Fore.RESET + ' Gestión de locales')
    print(Style.BRIGHT + Fore.YELLOW + '2_' + Fore.RESET +' Crear cuentas de dueños de locales')
    print(Style.BRIGHT + Fore.YELLOW + '3_' + Fore.RESET +' Aprobar / Denegar solicitud de descuento')
    print(Style.BRIGHT + Fore.YELLOW + '4_' + Fore.RESET +' Gestión de novedades')
    print(Style.BRIGHT + Fore.YELLOW + '5_' + Fore.RESET +' Reporte de utilización de descuentos')
    print(Style.BRIGHT + Fore.YELLOW + '0_' + Fore.RESET +' Volver al Menú Principal')

def pantalla_owner():
    global name
    clear_screen()
    centrar_texto(Style.BRIGHT  + Fore.WHITE +'Menú DUEÑO')
    centrar_texto_var('Bienvenido, ',name)
    print(Style.BRIGHT +'Ingrese una opción ' +  Fore.YELLOW + '0-3\n')
    print(Style.BRIGHT + Fore.YELLOW + '1_' + Fore.RESET + ' Crear descuento')
    print(Style.BRIGHT + Fore.YELLOW + '2_' + Fore.RESET +' Reporte de uso de descuento')
    print(Style.BRIGHT + Fore.YELLOW + '3_' + Fore.RESET +' Ver novedades')
    print(Style.BRIGHT + Fore.YELLOW + '0_' + Fore.RESET +' Volver al Menú Principal')

def pantalla_costumer():
    global name
    clear_screen()
    centrar_texto(Style.BRIGHT  + Fore.WHITE +'Menú CLIENTE')
    centrar_texto_var('Bienvenido, ',name)
    print(Style.BRIGHT +'Ingrese una opción ' +  Fore.YELLOW + '0-3\n')
    print(Style.BRIGHT + Fore.YELLOW + '1_' + Fore.RESET + ' Buscar descuentos en local')
    print(Style.BRIGHT + Fore.YELLOW + '2_' + Fore.RESET +' Solicitar descuentos')
    print(Style.BRIGHT + Fore.YELLOW + '3_' + Fore.RESET +' Ver novedades')
    print(Style.BRIGHT + Fore.YELLOW + '0_' + Fore.RESET +' Volver al Menú Principal')

def pantalla_locales():
    clear_screen()
    centrar_texto(Fore.WHITE + Style.BRIGHT + "Gestión de locales")
    print(Style.BRIGHT +'Ingrese una opción ' +  Fore.YELLOW + 'a-d\n')
    print(Style.BRIGHT + Fore.YELLOW + 'a_' + Fore.RESET + ' Crear locales')
    print(Style.BRIGHT + Fore.YELLOW + 'b_' + Fore.RESET + ' Modificar local')
    print(Style.BRIGHT + Fore.YELLOW + 'c_' + Fore.RESET + ' Eliminar local')
    print(Style.BRIGHT + Fore.YELLOW + 'd_' + Fore.RESET + ' Mapa de locales')
    print(Style.BRIGHT + Fore.YELLOW + 'e_' + Fore.RESET + ' Volver')

def barracarga():
    clear_screen()
    print(Style.BRIGHT + Fore.WHITE + "         CARGANDO...")
    bar_len = 25
    elements = ['-','\\', '|', '/']
    for i in range(bar_len+1):
        frame =i%len(elements)
        print(Fore.GREEN + Style.BRIGHT + f'\r[{elements[frame]*i:=^{bar_len}}]', end='')
        time.sleep(0.07) 







#------------------------LECTURAS-------------------------
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

def valid_owner():
    global opcown
    opcown = input("\nOPCION: ")
    while opcown != "1" and opcown != "2" and opcown != "3" and opcown != "0":
        opcown = input("Mal ingresado. Repetir opción. OPCION: ")
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

def valid_codProm(cod):#este es nuevo revisar
    alp = open (afp, "r+b")
    regProm = promociones()
    alp.seek(0,0)
    size=os.path.getsize(afp)
    while alp.tell() < size and cod!=regProm.codPromo:
        regProm = pickle.load(alp)
    if (cod!=regProm.codPromo): 
        bandera=1
    else:
        bandera=0
    return bandera

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
        bandera=1 #no encontro
        all.seek(0,0)
    else:
        bandera=0 #encontro
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

def valid_costumer():
    global opccostumer
    opccostumer = input("\nOPCION: ")
    while opccostumer != "1" and opccostumer != "2" and opccostumer != "3" and opccostumer != "0":
        opccostumer = input("Mal ingresado. Repetir opción. OPCION: ")
    clear_screen()

def enter(menu):
    #COPIAR ESTA LINEA DE ABAJO PARA CADA EXIT
    #exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER: ")
    if exit=="":
        clear_screen()
        menu

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

#----------------------------BUSQUEDA DICOATOMICA-----------------------------
def buscadicotomica(elem): 
        global bandera, med
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
def busquedaUser(codigo): #te dice si esxiste el coduser
    global coduser
    alp=open(afp,"r+b")
    regProm=promociones()
    alp.seek(0,0)
    size=os.path.getsize(afp)
    bandera=1
    while alp.tell()<size and codigo!=regProm.codUsuario and bandera==1:
        regProm=pickle.load(alp)
    if(codigo!=regProm.codUsuario):
        bandera=1
        alp.seek(0,0)
    else:
        bandera=0
    return bandera

def busquedaUserLoc(coduser): #te dice si existe el codloc
    all=open(afl,"r+b")
    regLoc=locales()
    all.seek(0,0)
    size=os.path.getsize(afl)
    bandera=1
    while all.tell()<size and coduser!=regLoc.codUsuario and bandera==1:
        regLoc=pickle.load(all)
    if(coduser!=regLoc.codUsuario):
        bandera=1
        all.seek(0,0)
    else:
        bandera=0
    return bandera

def buscadorLoc(cod): 
    all=open(afl,"r+b")
    all.seek(0,0)
    point=all.tell()
    regLoc=locales()
    regLoc=pickle.load(all)
    
    point=all.tell()
    if(regLoc.codLocal!=cod):
        point=all.tell()
    else:
        all.seek(0,0)
        while regLoc.codLocal!=cod:
            point=all.tell()
            regLoc=pickle.load(all)
    return point

def buscadordesc(cod): 
    alp=open(afp,"r+b")
    alp.seek(0,0)
    point=alp.tell()
    regProm=promociones()
    alp.seek(0,0)
    regProm=pickle.load(alp)
    alp.seek(0,0)
    point=alp.tell()
    while regProm.codPromo!=cod:
        point=alp.tell()
        regProm=pickle.load(alp)
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
    print(matriz[0])#poner lindo el print
    print(matriz[1])

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
    clear_screen()
    locales_cargados()
    
    rubros()
    exit = input("Toque Enter para volver. ")
    while exit != "":
        exit = input("Respuesta inválida. Presione ENTER. ")
    if exit=="": 
        gestion_locales()
    alu.close()
    all.close()

#----------------------------MODIFICATIO LOCALATIO-----------------------------
def modificar_local():
    global bandera, med,campo,codloc,coduser,rubrolocal,codLoc
    
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
    centrar_texto(Fore.GREEN + Style.BRIGHT + Back.BLACK + 'La modificación fue EXITOSA.')
    rubros()
    orden_rub(rubrolocal)

    exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    enter(gestion_locales())

#----------------------------ELIMINATIO LOCALATIO-----------------------------
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
        baja = input("Este local esta activo. Desea darlo de baja? (S/N): ").upper()
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
    
    codStr=str(regLoc.codLocal)
    print(f"El local {Fore.RED + codStr}{Style.RESET_ALL} fue dado de baja.")
    orden()
    rubros()
    orden_rub(rubrolocal)

    exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
    enter(gestion_locales())

#----------------------------GOOGLE MAPS-----------------------------
def mapa():
    all = open (afl,"r+b")
    tamarch=os.path.getsize(afl)
    if(tamarch==0):
        print("No hay Locales cargados hasta el momento.")
    else:
        orden()
        regLoc = locales()
        bandera=0 
        all.seek(0,0)
        regLoc=pickle.load(all)
        tamreg=all.tell()
        tamarch=os.path.getsize(afl)
        cant=(tamarch//tamreg)
        cantred=math.ceil((tamarch//tamreg)/5)
        all.seek(0,0)
        localesmap = [["0"] * 5 for i in range(10)]
        h = 0
        j = 0
        contador = 0
        all.seek(0,0)
        while h <= 10 and contador < cant:
            all.seek(contador*tamreg,0)
            regLoc=pickle.load(all)
            if (regLoc.estado=="B"):
                localesmap[h][j] = regLoc.codLocal+0.5
                localesmap[h][j]=localesmap[h][j]
            else:
                localesmap[h][j] = regLoc.codLocal
            contador=contador+1
            j = j + 1
            if j == 5:
                h = h + 1
                j = 0
        for fila in localesmap:
            print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")
            for elemento in fila:
                dou=float(elemento)
                if (dou%1!=0):
                    elemento=str(int(dou-0.5))
                    print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"|" +Fore.RED+Back.BLACK+str(elemento).center(5), end="")
                else:
                    if(elemento!="0"):
                        print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"|" + Fore.GREEN+Back.BLACK+str(elemento).center(5), end="")
                    else:
                        print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"|"+Fore.WHITE +Back.BLACK+str(elemento).center(5), end="")
                    
            print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"|")
        print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")

#------------------------GESTIONES-------------------------
def gestion_locales(): 
    size=os.path.getsize(afl)
    if (size==0):
        all = open (afl,"w+b")
    else:
        all = open (afl,"r+b")
        regLoc=pickle.load(all)
    all.seek(0,0)
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
                time.sleep(1.3)
            else:
                if exit=="S":
                    locales_cargados()
            if(contowner==0):
                centrar_texto(Style.BRIGHT + "No hay dueños registrados. Primero debe crear una cuenta de dueño de local...")
                time.sleep(1.3)
            else:
                crear_locales()
            gestion_locales()
        case "b":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Modificar locales---")
            exit = input('\n ¿Desea ver los locales cargados? ('+ Fore.GREEN + 'S' + Fore.WHITE + '/' + Fore.RED + 'N'+ Fore.WHITE+'): ').upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            size=os.path.getsize(afl)
            if exit=="S" and size==0:
                centrar_texto(Fore.WHITE + Style.BRIGHT + "No hay locales cargados hasta el momento.")
                time.sleep(1.3)
            else:
                if exit=="S" and size!=0:
                    locales_cargados()
                    modificar_local()
            if(size!=0 and exit=="N"):
                modificar_local()
            gestion_locales()
        case "c":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Eliminar locales---")
            exit = input('\n ¿Desea ver los locales cargados? ('+ Fore.GREEN + 'S' + Fore.WHITE + '/' + Fore.RED + 'N'+ Fore.WHITE+'): ').upper()
            while exit.upper() != "S" and exit.upper() != "N":
                exit = input("Respuesta inválida. ¿Desea seguir cargando? (S/N): ").upper()
            size=os.path.getsize(afl)
            if exit=="S" and size==0:
                centrar_texto(Fore.WHITE + Style.BRIGHT + "No hay locales cargados hasta el momento.")
                time.sleep(1.3)
            else:
                if exit=="S" and size!=0:
                    locales_cargados()
                    eliminar_loc()
            gestion_locales()
        case "d":
            clear_screen()
            mapa()
            exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
            enter(gestion_locales())
        case "e":
            menu_admin()
    all.close()     

#------------------------APROBAR O DENEGAR DESCUENTOS-------------------------
def aprob_den_desc():
    alp=open(afp,"r+b")
    all=open(afl,"r+b")
    regProm=promociones()
    regLoc=locales()
    alp.seek(0,0)
    all.seek(0,0)
    sizeloc=os.path.getsize(afl)
    sizeprom=os.path.getsize(afp)
    if (sizeloc==0 or sizeprom==0):
        if(sizeloc==0):
            print("No hay locales creados aun.")
        else:
            print("No hay promociones creadas aun.")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_admin()
             
    else:
        regProm=pickle.load(alp)
        regLoc=pickle.load(all)
        alp.seek(0,0)
        all.seek(0,0)
        
        while alp.tell()<sizeprom:
            regProm=pickle.load(alp)
            regLoc=pickle.load(all)
            all.seek(0,0)
            if(regProm.estado=="Pendiente"):
                while all.tell()<sizeloc and regProm.codLocal!=regLoc.codLocal: #busca el nombre del local
                    regLoc=pickle.load(all)
                
                print(regLoc.nombreLocal,regProm.codPromo,regProm.textoPromo) #agregar el print piola
        ##### aca estan todos los locales en pendiente mostrados 
        codpromo=int(input("Ingrese el codigo de promocion para Aprobar/Denegar"))
        bandera=valid_codProm(codpromo)
        while bandera==1:
            codpromo=int(input("Ingrese un codigo de promocion existente para Aprobar/Denegar")) 
            bandera=valid_codProm(codpromo)
        
        point=buscadordesc(codpromo)
        alp.seek(point,0)
        regProm=pickle.load(alp)
        alp.seek(point,0)
        print(Fore.BLUE+Back.BLACK+Style.BRIGHT+'-----------------------------------------')
        print(f"{Fore.BLUE+Style.BRIGHT}Código promoción: {Fore.WHITE+str(regProm.codPromo)}")
        print(f"{Fore.BLUE+Style.BRIGHT}Texto promoción: {Fore.WHITE+regProm.textoPromo}")
        print(f"{Fore.BLUE+Style.BRIGHT}Fecha Desde: {Fore.WHITE+regProm.fechaDesdePromo}")
        print(f"{Fore.BLUE+Style.BRIGHT}Fecha Hasta: {Fore.WHITE+regProm.fechaHastaPromo}")
        match regProm.estado.rstrip():
            case "Aprobado":
                print(f"{Fore.BLUE+Style.BRIGHT}Estado promoción: {Fore.GREEN+Style.BRIGHT+regProm.estado}")
            case "Rechazado":
                print(f"{Fore.BLUE+Style.BRIGHT}Estado promoción: {Fore.RED+Style.BRIGHT+regProm.estado}")
            case "Pendiente":
                print(f"{Fore.BLUE+Style.BRIGHT}Estado promoción: {Fore.YELLOW+Style.BRIGHT+regProm.estado}")
        print(Fore.BLUE+Back.BLACK+Style.BRIGHT+'-----------------------------------------')
        
        exit = input("\n ¿Desea APROBAR el descuento? (S/N): ").upper()
        while exit.upper() != "S" and exit.upper() != "N":
            exit = input("Respuesta inválida. ¿Desea APROBAR el descuento? (S/N): ").upper()
        if(exit=="S"):
            print(alp.tell())
            regProm.codPromo = regProm.codPromo
            regProm.textoPromo = regProm.textoPromo.ljust(100)
            regProm.fechaDesdePromo = regProm.fechaDesdePromo
            regProm.fechaHastaPromo = regProm.fechaHastaPromo
            regProm.diasSemana = regProm.diasSemana
            regProm.estado = "Aprobado".ljust(9)
            regProm.codLocal = regProm.codLocal
            regProm.cantUsoPromo= regProm.cantUsoPromo
            regProm.codUsuario = regProm.codUsuario
            pickle.dump(regProm,alp)
            alp.flush()
            alp.seek(0,0)
            centrar_texto(Fore.GREEN + Style.BRIGHT + 'La promoción fue APROBADA EXITOSAMENTE.')
            time.sleep(1.7)
        else:
            regProm.codPromo = regProm.codPromo
            regProm.textoPromo = regProm.textoPromo.ljust(100)
            regProm.fechaDesdePromo = regProm.fechaDesdePromo
            regProm.fechaHastaPromo = regProm.fechaHastaPromo
            regProm.diasSemana = regProm.diasSemana
            regProm.estado = "Rechazado".ljust(9)
            regProm.codLocal = regProm.codLocal
            regProm.cantUsoPromo= regProm.cantUsoPromo
            regProm.codUsuario = regProm.codUsuario
            pickle.dump(regProm,alp)
            alp.flush()
            alp.seek(0,0)
            centrar_texto(Fore.RED + Style.BRIGHT + 'La promoción fue RECHAZADA EXITOSAMENTE.')
            time.sleep(1.7)
    alp.close()
    all.close()   

#------------------------REPORTE UTILIZACION ADMIN-------------------------
def reporteadmin():
    alp=open(afp,"r+b")
    all=open(afl,"r+b")
    alup=open(afup,"r+b")
    regProm=promociones()
    regLoc=locales()
    regUP=uso_promociones()
    alp.seek(0,0)
    all.seek(0,0)

    sizeprom=os.path.getsize(afp)
    if(sizeprom==0):
        print("No hay promociones creadas")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_admin()
    else:
        fecha_actual = datetime.datetime.today()
        fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
        fecha_datetime = datetime.datetime.strptime(fecha_formateada, "%d/%m/%Y")#nueva manera

        desde_str = input("Ingrese día que inicia el rango de promociones: ")
        while valid_fecha(desde_str)==0:
            desde_str = input("Fecha no valida: ")
            valid_fecha(desde_str)

        desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")
        while desde <= fecha_datetime:
            desde_str = input("Fecha de inicio del rango de promoción no válida. Ingrese otra fecha: ")
            desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")

        hasta_str = input("Ingrese día que finaliza el rango de promociónes: ")
        while valid_fecha(hasta_str)==0:
            hasta_str = input("Fecha no valida: ")
            valid_fecha(hasta_str)
        hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
        while desde >= hasta:
            hasta_str = input("Fecha de finalización de rango de promociónes no válida. Ingrese otra fecha: ")
            hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")

        alp.seek(0,0)
        sizeprom=os.path.getsize(afp)
        while alp.tell()<sizeprom:
            regProm=pickle.load(alp)
            if(desde>=datetime.datetime.strptime(regProm.fechaDesdePromo,"%d/%m/%Y") and hasta<=datetime.datetime.strptime(regProm.fechaHastaPromo,"%d/%m/%Y") and regProm.estado=="Aprobado"):# cambiar el regprom a formato datetime
                alup.seek(0,0)
                sizeuprom=os.path.getsize(afup)
                cantusos=0
                while alup.tell()<sizeuprom:
                    regUP=pickle.load(alup)
                    if(regProm.codPromo==regUP.codPromo and datetime.datetime.strptime(regUP.fechaUsoPromo,"%d/%m/%Y")<=hasta and datetime.datetime.strptime(regUP.fechaUsoPromo,"%d/%m/%Y")>=desde):#cambiar le regprom a formato datetime
                        cantusos=cantusos+1
                print(regProm.codPromo,cantusos)#hacer el print de todo todito
                col_codPromo = 20
                col_cantUso= 20
                print(
                Back.BLACK + Fore.BLUE + Style.BRIGHT + Back.BLACK +
                f'{"Código de la promoción".center(col_codPromo)} | ' +
                f'{"Cantidad de usos.".center(col_cantUso)} | ')

#------------------------MENU OWNER------------------------------------------------------------------------------------------
def carga_dias(matriz,day):
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
    global nombredia, fecha_actual, fecha_formateada, nombredia, codpromo, dias, cod,desde_str
    bandera=0

    size = os.path.getsize(afp)

    alp = open (afp, "r+b")
    all = open (afl, "rb")
    alp.seek(0,0)
    all.seek(0,0)  
    regProm = promociones()
    regLoc = locales()
    sizeloc = os.path.getsize(afl)
    #regLoc = pickle.load(all)

    fecha_actual = datetime.datetime.today()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
    fecha_datetime = datetime.datetime.strptime(fecha_formateada, "%d/%m/%Y")#nueva manera

    

    if sizeloc == 0:
        print("\nNo existen locales creados. Cree uno para poder continuar.")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
    else:

        size = os.path.getsize(afp)
        if size==0:
            print("\nNo hay promociones cargadas aún.")
            exit = input("Toque Enter para seguir. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            clear_screen()

        alp = open (afp,"r+b")
        size= os.path.getsize(afp)
        alp.seek(0,0)
        while alp.tell() < size :
            regProm = pickle.load(alp)
            if regProm.codUsuario==cod:
                print(Fore.BLUE+Back.BLACK+Style.BRIGHT+'-----------------------------------------')
                print(f"{Fore.BLUE+Style.BRIGHT}Código promoción: {Fore.WHITE+str(regProm.codPromo)}")
                print(f"{Fore.BLUE+Style.BRIGHT}Texto promoción: {Fore.WHITE+regProm.textoPromo}")
                print(f"{Fore.BLUE+Style.BRIGHT}Fecha Desde: {Fore.WHITE+regProm.fechaDesdePromo}")
                print(f"{Fore.BLUE+Style.BRIGHT}Fecha Hasta: {Fore.WHITE+regProm.fechaHastaPromo}")
                match regProm.estado.rstrip():
                    case "Aprobado":
                        print(f"{Fore.BLUE+Style.BRIGHT}Estado promoción: {Fore.GREEN+Style.BRIGHT+regProm.estado}")
                    case "Rechazado":
                        print(f"{Fore.BLUE+Style.BRIGHT}Estado promoción: {Fore.RED+Style.BRIGHT+regProm.estado}")
                    case "Pendiente":
                        print(f"{Fore.BLUE+Style.BRIGHT}Estado promoción: {Fore.YELLOW+Style.BRIGHT+regProm.estado}")
                print(Fore.BLUE+Back.BLACK+Style.BRIGHT+'-----------------------------------------')
        alp.seek(0,0)
        all.seek(0,0)
        print()
        locales_cargados() #como se cual es el codigo del local?
        print()
        exitmain = "N"
        codigo = int(input("Identifique el código del local al que quiere cargar un descuento o 0 si quiere salir: "))
        bandera = valid_codLoc(codigo)

        
        all.seek(0, 0)
        if codigo==0:
            menu_owner()
        while bandera==1:
            print("Código de local no existe.")
            codigo = int(input("Vuelva a ingresar el código de local: "))
            bandera = valid_codLoc(codigo)

        flag2 = 1
        all.seek(0, 0)
        while all.tell() < sizeloc and bandera == 0 and flag2 == 1:
            regLoc = pickle.load(all)
            if codigo == regLoc.codLocal:
                match cod:
                    case regLoc.codUsuario:
                        match codigo:
                            case regLoc.codLocal:
                                flag2 = 0
                    case _:
                        print("Código de local no válido o no pertenece al dueño.")
                        codigo = int(input("Vuelva a ingresar el código de local: "))
                        bandera = valid_codLoc(codigo)
                        all.seek(0, 0)

        if flag2 == 0:
            exitmain = "S"
            alp.seek(0, 0)
            size= os.path.getsize(afp)
            while alp.tell() < size and exitmain == "S" or size==0: 
                alp.seek(0,2)
                texto = input("Ingrese texto de la promocion: ")
                desde_str = input("Ingrese día que inicia la promoción: ")
                while valid_fecha(desde_str)==0:
                    desde_str = input("Fecha no valida: ")
                    valid_fecha(desde_str)
                
                desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")

                while desde < fecha_datetime:
                    desde_str = input("Fecha de inicio de la promoción no válida. Ingrese otra fecha: ")
                    desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")
                
                hasta_str = input("Ingrese día que finaliza la promoción: ")
                while valid_fecha(hasta_str)==0:
                    hasta_str = input("Fecha no valida: ")
                    valid_fecha(hasta_str)
                hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
                while desde >= hasta:
                    hasta_str = input("Fecha de finalización de la promoción no válida. Ingrese otra fecha: ")
                    hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")

                dias=[0]*7
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
                
                regProm.codPromo=codpromo
                codpromo=codpromo+1
                regProm.textoPromo = texto.ljust(100)
                regProm.fechaDesdePromo = desde.strftime("%d/%m/%Y")
                regProm.fechaHastaPromo = hasta.strftime("%d/%m/%Y")
                regProm.estado = "Pendiente".ljust(9)
                regProm.codLocal=codigo
                regProm.codUsuario=cod
                pickle.dump(regProm, alp)
                alp.flush()
                size= os.path.getsize(afp)
            print(Fore.GREEN + Style.BRIGHT +'¡Promoción creada exitosamente!')
            time.sleep(1.5)
        alp.close()
        alu.close()
        all.close()

def uso_descuento(): 
    global cod
    alp = open (afp, "r+b")
    alup = open (afup, "r+b")
    all = open(afl, "r+b")
    regProm = promociones()
    regUP=uso_promociones()
    regLoc=locales()
    alp.seek(0,0)
    all.seek(0,0)
    alup.seek(0,0)
    size = os.path.getsize(afp)
    sizeloc = os.path.getsize(afl)
    sizeUP = os.path.getsize(afup)

    if size==0: 
        print("\nNo hay promociones cargadas aún.")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_owner()
    else:
        flag2=1 
        alp.seek(0,0)
        while alp.tell() < size:
            regProm = pickle.load(alp)
            all.seek(0,0)
            while all.tell() < sizeloc and flag2 == 1:
                regLoc = pickle.load(all)
                if cod == regLoc.codUsuario:
                    match regLoc.codLocal:
                        case regProm.codLocal:
                            match cod:
                                case regLoc.codUsuario:
                                    flag2 = 0
        
        if flag2==0:
            desde_str = input("Ingrese el primer dia del rango: ")
            desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")
            fechaDesdePromo = datetime.datetime.strptime(regProm.fechaDesdePromo, "%d/%m/%Y")
            while fechaDesdePromo >= desde and valid_fecha(desde_str)==0:
                desde_str = input("Fecha de rango no válida. Ingrese otra fecha: ")
                valid_fecha(desde_str)
                desde = datetime.datetime.strptime(desde_str, "%d/%m/%Y")

            hasta_str = input("Ingrese el ultimo dia del rango: ")
            hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
            fechaHastaPromo = datetime.datetime.strptime(regProm.fechaHastaPromo, "%d/%m/%Y")
            while fechaHastaPromo <= hasta and valid_fecha(hasta_str)==0:
                hasta_str = input("Fecha de rango no válida. Ingrese otra fecha: ")
                valid_fecha(hasta_str)
                hasta = datetime.datetime.strptime(hasta_str, "%d/%m/%Y")
            
            hasta1 = datetime.datetime.strftime(hasta, "%d/%m/%Y")
            desde1 = datetime.datetime.strftime(desde, "%d/%m/%Y")
            print("Fecha desde:", desde1,"    Fecha hasta:", hasta1)


        sizeUP=os.path.getsize(afup)
        if(sizeUP==0):
            print("No se uso ningun descuento")
            exit = input("Toque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="": 
                menu_owner()
        else:
            alup.seek(0,0)
            regUP = pickle.load(alup)
            tamreg = alup.tell()
            cantreg = sizeUP//tamreg
            flag2=1

            all.seek(0,0)
            alp.seek(0,0)

            var=0
            var2=0
            while alp.tell() < size:
                ban2=0
                ban=0
                regProm = pickle.load(alp)
                all.seek(0,0)
                while all.tell() < sizeloc and flag2 == 1:
                    regLoc = pickle.load(all)
                    var2=regLoc.codLocal
                    if cod == regLoc.codUsuario:
                        ban=1
                        match regLoc.codLocal:
                            case regProm.codLocal:
                                match cod:
                                    case regLoc.codUsuario:
                                        flag2 = 0

                if ban!=0 and flag2==0 and ban2==0 and var!=var2:
                    if fechaDesdePromo>=desde and fechaHastaPromo<=hasta and regProm.estado.rstrip()=="Aprobado" and fechaHastaPromo<=hasta :
                        print("Local", regLoc.codLocal,":", regLoc.nombreLocal)
                        print("|-----------------|----------------------------------------|---------------|---------------|-------------------|")
                        print("| Codigo Promo    |               Texto                    |  Fecha Desde  |  Fecha Hasta  |  Cant. Uso Promo  |")
                        print("|-----------------|----------------------------------------|---------------|---------------|-------------------|") 
                        ban2=1
                    else:
                        print("No se encuentra ninguna promoción entre las fechas proporcionadas.")                          
                                    
                if flag2==1:
                    print("El usuario no tiene promociones creadas.")
                    exit = input("\nToque Enter para volver. ")
                    while exit != "":
                        exit = input("Respuesta inválida. Presione ENTER. ")
                    if exit == "":
                        menu_owner()

                if fechaDesdePromo>=desde and fechaHastaPromo<=hasta and regProm.estado.rstrip()=="Aprobado" and fechaHastaPromo<=hasta :
                    if flag2==0:
                        print(f"| {regProm.codPromo:<15} | {regProm.textoPromo.rstrip():<38} | {regProm.fechaDesdePromo:<15} | {regProm.fechaHastaPromo:<15} | {cantreg:<17} |")
                        print("|-----------------|--------------------------------------|---------------|---------------|-------------------|")
                        flag2=1
                var=regProm.codLocal
            
        
        alp.close()
        all.close()
        alup.close()

    exit = input("\nToque Enter para volver. ")
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

def buscadorLoc(cod): 
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
    global fecha_actual, desde_str,fecha_datetime
    bandera=0
    alp = open (afp, "r+b")
    regProm=promociones()
    alp.seek(0,0)
    size = os.path.getsize(afp) 
    if size == 0:
        print("No hay promociones creadas")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_costumer()
    else:
        regProm = pickle.load(alp) 
        codigo=int(input("\nIdentifique el código del local para buscar descuentos: "))
        while alp.tell() < size and codigo!=regProm.codLocal and bandera==0:
            regProm = pickle.load(alp)
            if (codigo!=regProm.codLocal): 
                codigo=int(input('Código de local no válido, volver a ingresar. CÓDIGO: '))
                alp.seek(0,0)
        bandera = 1 

        if regProm.codLocal==regLoc.codLocal and regProm.codLocal==0:
            print("El local no tiene promociones creadas.")
            exit = input("Toque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="": 
                menu_costumer()

        fecha_str = input("Ingrese una fecha para buscar descuentos: ")
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

        fecha_actual=datetime.datetime.now()#obtiene fecha del sist
        fecha_formateada= fecha_actual.strftime("%d/%m/%Y")#la transforma en str para poder aplicarle formato
        fecha_datetime = datetime.datetime.strptime(fecha_formateada, "%d/%m/%Y")#nueva manera. Lo transforma de vuelta en datetime

        while fecha >= fecha_datetime and valid_fecha(desde_str)==0:
            fecha_str = input("Fecha no válida. Ingrese otra fecha: ")
            valid_fecha(fecha_str)
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

        dia_semana = fecha.strftime("%A")

        alp.seek(0,0)
        datetime.datetime.strptime(regProm.fechaDesdePromo, "%d/%m/%Y")
        
        while alp.tell() < size :
            if regProm.codLocal == codigo and regProm.estado.rstrip() == "Aprobado" and fecha >= datetime.datetime.strptime(regProm.fechaDesdePromo, "%d/%m/%Y") and fecha <= datetime.datetime.strptime(regProm.fechaHastaPromo, "%d/%m/%Y") and regProm.diasSemana[num_dias(dia_semana)]==1:
                
                regProm = pickle.load(alp)
                
                # Definir ancho de cada columna de la tabla
                col_codPromo = 20
                col_textoPromo = 40
                col_fechaDesdePromo = 15
                col_fechaHastaPromo = 15

                # Encabezados de la tabla
                print(
                (Back.BLACK + Fore.BLUE + Style.BRIGHT  +
                f'{"Código Promo".center(col_codPromo)} | ' +
                f'{"Texto".center(col_textoPromo)} | ' +
                f'{"Fecha Desde".center(col_fechaDesdePromo)} | ' +
                f'{"Fecha Hasta".center(col_fechaHastaPromo)}'))
                
                
                # Formatear y centrar cada columna en la tabla
                print((Fore.WHITE + Style.BRIGHT +
                f'{str(regProm.codPromo).center(col_codPromo)} | ' +
                f'{regProm.textoPromo.strip().center(col_textoPromo)} | ' +
                f'{regProm.fechaDesdePromo.center(col_fechaDesdePromo)} | ' +
                f'{regProm.fechaHastaPromo.center(col_fechaHastaPromo)}'))
                #print(formatted_row)
            else: 
                    if regProm.diasSemana[num_dias(dia_semana)]==0:
                        centrar_texto_var("No hay descuentos disponibles para ",fecha_str)
                    else:
                        centrar_texto("No hay promociones en el local buscado.")

            alp.close()
            exit = input("\nToque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="":
                menu_costumer()

def solicitardesc(): 
    global fecha_formateada, fecha_datetime

    alp = open (afp, "r+b")
    alup = open (afup, "r+b")
    alu = open (afu, "r+b")
    regProm = promociones()
    regUP = uso_promociones()
    regUser = user()
    alp.seek(0,0)
    alup.seek(0,0)
    alu.seek(0,0)
    
    size = os.path.getsize(afp)
    if size == 0:
        print("No hay promociones creadas")
        exit = input(Fore.WHITE + Style.BRIGHT + "\nToque Enter para volver: ")
        while exit != "":
                exit = input("Respuesta inválida. Presione ENTER: ")
    else:
        regProm = pickle.load(alp)
        fecha_actual=datetime.datetime.now()#obtiene fecha del sist
        fecha_formateada= fecha_actual.strftime("%d/%m/%Y")#la transforma en str para poder aplicarle formato
        fecha_datetime = datetime.datetime.strptime(fecha_formateada, "%d/%m/%Y")#nueva manera. Lo transforma de vuelta en datetime
        dia_semana = fecha_datetime.strftime("%A")#cambiado a date_time antes:fecha_formateada
        
        alp.seek(0,0)
        codigo=int(input("Ingresar código de promoción: "))
        bandera=valid_codProm(codigo)
        while bandera==1:
            codigo=int(input("Código de promoción no válido, volver a ingresar. CÓDIGO: "))
            bandera=valid_codProm(codigo)
        
        fechovich=datetime.datetime.strptime(fecha_formateada, "%d/%m/%Y")
        fechaDesdePromo = datetime.datetime.strptime(regProm.fechaDesdePromo, "%d/%m/%Y")
        fechaHastaPromo = datetime.datetime.strptime(regProm.fechaHastaPromo, "%d/%m/%Y")

        alp.seek(0,0)
        while alp.tell()<size :
            regProm=pickle.load(alp)
            if codigo==regProm.codPromo and regProm.estado.rstrip()=="Aprobado" and fechovich >= fechaDesdePromo and fechovich <= fechaHastaPromo and regProm.diasSemana[num_dias(dia_semana)]==1:
                regUP.codCliente = regUser.cod
                regUP.codPromo = codigo
                regUP.fechaUsoPromo = fecha_formateada
                point=buscadorLoc(codigo)
                alp.seek(point,0)
                regProm.cantUsoPromo = regProm.cantUsoPromo + 1
                pickle.dump(regProm, alp)
                pickle.dump(regUP, alup)
                alp.flush()
                alup.flush()
                alup.close()
                alp.close()
                alu.close()
                print(Fore.GREEN + Style.BRIGHT +'¡La promoción se aplico con exito!')

            else:
                print(Fore.RED + Style.BRIGHT + "La promoción no es valida el dia de hoy.")
                
            exit = input("\nToque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="":
                menu_costumer()
   
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
    nombre=input("\nIngrese el nombre: ").ljust(100)
    password = maskpass.askpass(prompt="\nIngresar contraseña: ", mask="*").ljust(8)
    
    while correcto!=1 and cont<3:
        alu.seek(0,0)

        while(alu.tell() < size) and (regUser.usuario.strip()!=nombre.strip()) and (regUser.clave.strip()!=password.strip()):
            regUser=pickle.load(alu)

        if(regUser.usuario.strip()==nombre.strip() and regUser.clave.strip()==password.strip()):  
            correcto=1
        else:
            nombre=input("\nIngrese el nombre: ").ljust(100)
            password = maskpass.askpass(prompt="\nIngresar contraseña: ", mask="*").ljust(8)
            cont=cont+1 #=?????
            alu.seek(0,0)
    if (regUser.usuario.strip()==nombre.strip() and regUser.clave.strip()==password.strip()):  
            correcto=1    
    if(correcto==1):
        name=regUser.usuario.strip()
        cod=regUser.cod
        select_menu(regUser.tipo.strip())
    else:
        print("Cantidad de maxima de intentos permitidos")

    alu.close()

#-------------------------SIGN IN----------------------------
def signin(user):
    global contuser
    alu = open (afu, "r+b")
    size=os.path.getsize(afu)
    regUser=pickle.load(alu)
    flag=0


    nombre=input("\nIngrese el nombre: ").ljust(100)

    while flag!=1:
        alu.seek(0,0)

        while(alu.tell() < size) and (regUser.usuario.rstrip()!=nombre.rstrip()):
            regUser=pickle.load(alu)
        if(regUser.usuario.rstrip()==nombre.rstrip()):  
            nombre=input("\nEse nombre ya existe. Ingrese el nombre: ").ljust(100)
        else:
            flag=1
            alu.seek(0,0)

    password = maskpass.askpass(prompt="\nIngrese una contraseña con 8 caracteres: ", mask="*").ljust(8)
    while len(password)!=8:
        password = maskpass.askpass(prompt="\nLa contraseña debe contener 8 caracteres: ", mask="*").ljust(8)

    alu.seek(0,2)
    contuser=contuser+1
    regUser.cod=contuser
    regUser.usuario = nombre.ljust(100)
    regUser.clave = password.ljust(8)
    regUser.tipo = user.ljust(14)

    pickle.dump(regUser, alu)
    alu.flush()
    alu.close()
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
        print("\nGestión de locales")
        gestion_locales()
      case "2":
        clear_screen()
        centrar_texto(Fore.WHITE + Style.BRIGHT + '---Crear cuentas de dueños de locales---')
        signin("Dueño de local")
        contowner=contowner+1
        menu_admin()
      case "3":
        clear_screen()
        centrar_texto(Fore.WHITE + Style.BRIGHT + '---Aprobar / Denegar solicitud de descuento---')
        aprob_den_desc()
        menu_admin()
      case "4":
        clear_screen()
        centrar_texto(Fore.WHITE + Style.BRIGHT + '---Ver Novedades---')
        print("\nDiagramado en chapin")
        exit = input("Toque Enter para volver. ")
        while exit != "":
            exit = input("Respuesta inválida. Presione ENTER. ")
        if exit=="": 
            menu_admin()
      case "5":
        clear_screen()
        centrar_texto(Fore.WHITE + Style.BRIGHT + '---Reporte de utilizacion de descuentos---')
        reporteadmin()
      case "0":
        clear_screen()
        mainMenu()

def menu_owner():
    barracarga()
    pantalla_owner()
    valid_owner()
    match opcown:
        case "1":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Crear Descuento---")
            crear_descuento()
            menu_owner()
        case "2":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Reporte de uso de descuento---")
            uso_descuento()
        case "3":
            clear_screen()
            centrar_texto(Style.BRIGHT + Fore.WHITE + "---Ver Novedades---")
            centrar_texto("\nDiagramado en chapin") 
            exit = input("Toque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="": 
                menu_owner()
        case "0":
            barracarga()
            mainMenu()

def menu_costumer():
    barracarga()
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
            menu_costumer()
        case "3":
            clear_screen()
            print("Ver novedades")
            print("\nDiagramado en chapin")
            exit = input("Toque Enter para volver. ")
            while exit != "":
                exit = input("Respuesta inválida. Presione ENTER. ")
            if exit=="": 
                menu_costumer()
        case "0":
            barracarga()
            mainMenu()

#Main Menu
def mainMenu():
    clear_screen()
    mostrar_menu()
    ingreso_main_menu(valid_opc())

def PP():
    mainMenu()

PP()








