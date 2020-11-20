# https://docs.hektorprofe.net/python/entradas-y-salidas/salida-por-pantalla/
# https://devcode.la/tutoriales/diccionarios-en-python/
print("-----hola mundo------")
#-------------Sentencia y mas de una linea---------
a=2 + 3 + 5  + \
    7 + 9 + 4 + \
    6
print("a0:",a)
# es es un comentario de primera_linea
a = [1, 2, 7,
    3, 8, 4,
    9]
print("a1:",a)
# bloque de codigo 
def suma_numeros(numeros):    # Bloque 1
    suma = 0                    # Bloque 2
    for n in numeros:           # Bloque 2
        suma += n                 # Bloque 3
        print(suma)               # Bloque 3
    return suma                 # Bloque 2 

"""     Palabras reservadas de Python:
and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from,
global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, yield,
while y with
"""
# Entradas y salidas de python
nombre="Giovanny"   #input("Ingrese su NOMBRE: ")
apellido='Aguilar'  #input("Ingrese su APELLIDO: ")
edad=25             #input("Ingrese su EDAD: ")
print("Nombre: '{}'. Apellido: '{}'. Edad:  '{}'\n".format(nombre,apellido,edad))
print( "mi nombre es '{0}' - '{1}' y tengo '{2}'".format(nombre,apellido,edad) )
print( "my name is '{name}'  '{surname}' and '{age}'. ".format(name=nombre,surname=apellido,age=edad) )
print("{g},{g},{g}".format(g=nombre))
print( "{:>10}".format("Alineamiento a la derecha ") )      #
print( "{:30}".format("Alineamiento a la izquierda") )
print( "{:^30}".format("Alineamiento al centro") ) 
print( "{:.5}".format("Truncamiento ") )  
print( "{:>30.5}".format("Alineamiento ") )    
print("{:4d}".format(10))           #  10
print("{:4d}".format(100))          # 100
print("{:4d}".format(1000))         #1000
print("{:04d}".format(10))          #0010
print("{:04d}".format(100))         #0100
print("{:04d}".format(1000))        #1000
print("{:7.3f}".format(3.1415926))  #  3.142
print("{:7.3f}".format(153.21))     #153.210
print("{:07.3f}".format(3.1415926)) #003.142
print("{:07.3f}".format(153.21))    #153.210
print(f"hola {nombre}")             #hola Giovanny

print(type(edad)) # el resultado  sera un str(String) apesar de ingresar un number
# Convercion de variables
cantidad=123#int(input("Ingresar la cantidad de personas:"))
altura=123.456#float(input("Ingresar la altura de la persona en metros ej:1.70:"))

print(type(cantidad),type(altura)) #<class 'int'> <class 'float'>

#  inicio de una cadena de caracteres
precentar="my "+"name"+" is"
nombre='rhonny'
apellido='AGUILAR'
print() #se imprime una j
if nombre[0]=="G": #verificamos si el primer caracter del string es una j
    print(nombre,"comienza con la letra:",nombre[0])
print("Longitud de ",nombre,len(nombre))   
print("Capitalize():",precentar.capitalize(),"UPPER(): ",nombre.upper(),"- lower: ",apellido.lower())

"""
OPERADORES: <, >, >=, <=, ==, !=, +, -, *, /, %, //, **.
"""
print(10/3)  #div_decimal:  3.3333333333333335
print(10//3) #vid_Entero:   3
print(10%3)  #resto:        1
print(2**3)  #potencia:     8

"""
OPERADORES LOGICOS: OR, AND ,NOT
"""
a=True
b=False
if (a or b) and (a==True) or (b!=True) or ( not(a)):
    print("a:",a,"- b: ",b)
    print("negacion de a:",not(a))
    print("ok\n")
else:
    print("mal") 

""" AuntoIncrementable: 
    X += 2 : X = X+2
    X -= 2 : X = X-2 
    X *= 2 : X = X*2 
    X /= 2 : X = X/2 
    X %= 2 : X = X%2 
    X //= 2 : X = X//2 
    X **= 2 : X = X**2 
"""
a=0
b="a"
while a<5:
    print(a,b)
    a+=1
    b*=2
# listas
lista = [1, 3, 2, 7, 9, 8, 6]
print(4 in lista)       #False
print(3 in lista)       #True
print(4 not in lista)   #True

lista1=[10, 5, 3]                       # lista de enteros
lista2=[1.78, 2.66, 1.55, 89,4]         # lista de valores float
lista3=["lunes", "martes", "miercoles"] # lista de string
lista4=["juan", 45, 1.92]               # lista con elementos de distinto tipo

print("long lista1: ",len(lista1),"\n") # imprime un 3

lista=[10, 20, 30]
print(lista)        #[10, 20, 30]
lista.append(100)
print("Añade: ",lista)        #[10, 20, 30, 100]
print(lista[3])     # imprime un 100
lista.pop(0)
print("Elimina: ",lista)        #[20, 30, 100]


myLista=[[1,2,3], [4,5,6], [7,8,9]]
print(myLista[0][0])

#Estructura de datos tipo Tupla
tupla=(1, 2, 3)
fecha=(25, "Diciembre", 2016)
punto=(10, 2)
persona=("Rodriguez", "Pablo", 43)

print("\n",tupla)
print(type(punto)) #<class 'tuple'>
print(fecha)
print(punto)
print("punto[0]: ",punto[0]) # primer elemento de la tupla
print("punto[1]: ",punto[1]) # segundo elemento de la tupla
print(persona)

x=10
y=30
punto=x,y
print(punto)

fecha=(18, "diciembre", 2020)
print(fecha)
dd,mm,aa=fecha
print("Dia",dd)
print("Mes",mm)
print("Año",aa)

empleado=["juan", 53, (25, 11, 1999)]
print("\n",empleado)            #['juan', 53, (25, 11, 1999)]
empleado.append((1, 1, 2016))   
print(empleado)                 #['juan', 53, (25, 11, 1999), (1, 1, 2016)]

alumno=("pedro",[7, 9])
print(alumno)               #('pedro', [7, 9])
alumno[1].append(10)    
print(alumno)               #('pedro', [7, 9, 10])

lista1=[0,1,2,3,4,5,6]
print("\n",lista1)  # [0, 1, 2, 3, 4, 5, 6]
lista2=lista1[2:5]
print(lista2)       # 2,3,4
lista3=lista1[1:3]
print(lista3)       # 1,2
lista4=lista1[:3]
print(lista4)       # 0,1,2
lista5=lista1[2:]
print(lista5)       # 2,3,4,5,6
print(lista1[-1])   # 6
print(lista1[-2])   # 5

# Diccionario
productos={"manzanas":39, "peras":32, "lechuga":17}
print("\n",productos)
del productos["manzanas"] #elimina un valor del diccionario 
print("\n Productos: ",productos) # Productos:  {'peras': 32, 'lechuga': 17}

#definicion de llamadas
def saludar():
    print("Hola! Este definicion de llamadas se llama desde la función saludar()")
saludar()

def dibujar_tabla_del_5():
    print("tabla del 5")
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))
dibujar_tabla_del_5()

def suma(a, b):  # valores que se reciben
    return a + b
resultado = suma(2, 5)  # valores que se envían
print(resultado)

def resta(a, b):
    return a - b
print(resta(30, 10) ) # argumento 30 => posición 0 => parámetro a
               # argumento 10 => posición 1 => parámetro b
print(resta(b=30, a=10) )

def resta(a=None, b=None):
    if a == None or b == None:
        print("se puede tener valores por defecto ")
        return   # indicamos el final de la función aunque no devuelva nada
    return a-b
print(resta())

def doblar_valor(numero):
   return numero * 2
n = 5
n = doblar_valor(n)
print(n) #10

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] += 2
    return numeros
ns = [10,50,100]
print(doblar_valores(ns[:]))  # Una copia al vuelo de una lista con [:]
print(ns)

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5,"Hola",[1,2,3,4,5]) #Por posición

def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5]) #Por nombre

def super_funcion(*args,**kwargs):
    total = 0
    for arg in args:
        total += arg
    print("sumatorio => ", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])
super_funcion(10, 20, -1, 1.56, 1, 0, 30, nombre="Hector", edad=27) #sumatorio => 390.56 | nombre => Hector | edad => 27

#Funciones recursivas
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)
cuenta_atras(5)

def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num
print(factorial(5))

#Funciones integradas
n = int("10")
print(n)
f = float("10.5")
print(f)
c = "Un texto y dos números " + str(10) + " y " + str(3.14)
print(c)

print(bin(10)) #0b1010
print(hex(10)) #0xa
print(int('0b1010', 2)) #10
print(int('0xa', 16))   #10
print(abs(-10))   #10
print(round(5.5))   #6
print(round(5.4))   #5
print(eval('2 + 5')) #7
n = 10
print(eval('n * 10 - 5'))   #95
print(len("Una cadena"))    #10
print(len([]))              #0
#print(help())

#Errores y Exepciones
"""
try:
    n = float(input("Introduce un número : "))
    m = 100
    print("{}/{} = {}".format(m,n,m/n))
except:
    print("Ha ocurrido un error, introduce un numero distinto de cero y letra")

while(True):
    try:
        n = float(input("Introduce un número y no letra: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien

while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta

try:
    n = input("Introduce un número: ")  # no transformamos a número
    5/n
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__)
"""
# typos
"""
print(type(1))          #<class 'int'>
print(type(3.14))       #<class 'float'>
print(type([]))         #<class 'list'>
print(type(()))         #<class 'tuple'>
print(type({}))         #<class 'dict'>
print( type(e).__name__)    #TypeError
print(type(1).__name__)     #int
print(type(3.14).__name__)  #float
print(type([]).__name__)    #list
print(type(()).__name__)    #tuple
print(type({}).__name__)    #dict
"""
try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )

#-----------------Programacion Orientado A Opjeto (POO)-------------------------
# Definimos unos cuantos clientes
clientes= [
    {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
    {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
]

# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print('Cliente no encontrado')

# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    for clave,valor in enumerate(clientes):
        if (dni == valor['dni']):
            del( clientes[clave] )
            print(str(valor),"> BORRADO")
            return

    print('Cliente no encontrado')    

### Fíjate muy bien cómo se utiliza el código estructurado

print("==LISTADO DE CLIENTES==")
print(clientes) 
#[ {'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'},
#  {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'} ]

print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A') #Hector Costa Guzman
mostrar_cliente(clientes, '11111111Z') #Cliente no encontrado

print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V') #Cliente no encontrado
borrar_cliente(clientes, '22222222B') #{'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'} > BORRADO

print("\n==LISTADO DE CLIENTES==")
print(clientes) #[{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}]

