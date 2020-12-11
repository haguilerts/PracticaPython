# ============================ If() ============================
sueldo=int(input("Ingrese cual es su sueldo:"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")

num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
if num1>num2:
    print("El valor mayor es {}".format(num1))
else:
    print("El valor mayor es {}".format(num2))

nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
promedio=(nota1+nota2+nota3)/3

if promedio>=7:
    print("Promocionado")
else:
    if promedio>=4 and promedio<7:
        print("Regular")
    else:
        print("Reprobado")

if promedio>=7:
    print("Promocionado")
elif promedio>=4 and promedio<7:
    print("Regular")
else:
    print("Reprobado")
# ============================ While() ============================
contador=1
suma=0
while contador<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    contador+=1
promedio=suma/10
print("La suma de los 10 valores es {}".format(suma))
print("El promedio es {}".format(promedio))

piezas_acumuladas=0
contador=1
cantidad=int(input("Cuantas piezas cargará:"))
while contador<=cantidad:
    largo=float(input("Ingrese la longitud de la pieza:"))
    if largo>=1.2 and largo<=1.3:
        piezas_acumuladas+=1
    contador+=1
print("La cantidad de piezas aptas son {}".format(piezas_acumuladas))

print("Ejemplo con while:")
x=0
while x<101:
    print(x)
    x=x+1
# ============================ for() ============================
    
print("Ejemplo range() con un parametro:")
for x in range(101): #fin - range(): rango en el cual va reccorrer
    print(x) 

print("Ejemplo range() con dos parametros:")
for x in range(20,35): #inicio,fin
    print(x)

print("Ejemplo range() con tres parametros")
for x in range(1,100,2): # inicio,fin,pasos
    print(x)
suma=0
for contador in range(10):
    valor=int(input("Ingrese valor {}:".format(contador+1)))
    suma=suma+valor
print("La suma es {} y el promedio {}".format(suma,suma/10))

aprobados=0
reprobados=0
for contador in range(10):
    nota=int(input("Ingrese la nota {}:".format(contador+1)))
    if nota>=7:
        aprobados+=1
    else:
        reprobados+=1
print("Cantidad de aprobados: {}".format(aprobados))
print("Cantidad de reprobados: {}".format(reprobados))

multiplos_de_tres=0
multiplos_de_cinco=0
for contador in range(10):
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        multiplos_de_tres+=1
    if valor%5==0:
        multiplos_de_cinco+=1
print("Cantidad de valores ingresados múltiplos de 3: {}".format(multiplos_de_tres))
print("Cantidad de valores ingresados múltiplos de 5: {}".format(multiplos_de_cinco))

# ============================ Listas ============================

lista = ["Azul","Rojo","Amarillo","Verde"] 
for elemento in range(len(lista)):
    # muestra posición y elemento
    print ("Elemento: {} - Valor: {}".format(elemento, lista[elemento]))  

cadena1 = 'tengo una yama que Yama se llama'            # declara variable
lista1 = ['pera', 'manzana', 'naranja', 'uva']  	    # declara lista

longitud = len(cadena1)  			            # 32, devuelve longitud de la cadena
elem = len(lista1)  				            # 4, devuelve nº elementos de la lista 

cuenta = cadena1.count('yama')  	            # 1, cuenta apariciones de 'yama'
print(cadena1.find('yama'))                     # 10, devuelve posición de búsqueda 

cadena2 = cadena1.join('***')                   # inserta cadena1 entre caracteres  
lista1 = cadena1.split(' ')                     # divide cadena por separador → lista
tupla1 = cadena1.partition(' ')                 # divide cadena por separador → tupla 

cadena2 = cadena1.replace('yama','cabra',1) 	# busca/sustituye términos 
numero = 3.14  			                        # asigna número con decimales

cadena3 = str(numero)  		                    # convierte número a cadena

if cadena1.startswith("tengo"):		            # evalúa si comienza por “tengo” (Falta definir el bloque)
    print("La cadena1 empieza con tengo")
if cadena1.endswith("llama"):                   # evalúa si termina por “llama” (Falta definir el bloque)
    print("La cadena1 empieza con llama")
if cadena1.find("llama") != -1:                 # evalúa si contiene “llama” (Falta definir el bloque)
    print("La cadena1 contiene la palabra llama")

cadena4 = 'Python'                              # asigna una cadena a una variable
print(cadena4[0:4])  				            # muestra desde la posición 0 a 4: "Pyth"
print(cadena4[1])  				                # muestra la posición 1: "y"
print(cadena4[:3] + '-' + cadena4[3:])  		# muestra "Pyt-hon"
print(cadena4[:-3])  				            # muestra todo menos las tres últimas: "Pyt"

# declara variable con cadena alfanumérica
cadena5 = "  abc;123  "

# suprime caracteres en blanco por la derecha
print(cadena5.rstrip())  		# "  abc;123"

# suprime caracteres en blanco por la izquierda
print(cadena5.lstrip())  		# "abc;123  "

# suprime caracteres en blanco por derecha e izquierda 
print(cadena5.strip())  	    # "abc;123"

cadena6 = "Mar"             	# declara una variable
print(cadena6.upper())   		# convierte a MAYUSCULA: "MAR"
print(cadena6.lower())   		# convierte a minúsculas: "mar"


lista1 = ['uno', 2, True] 			 # declara una lista heterogénea
lista2 = [1, 2, 3, 4, 5]  			 # declara lista numérica (homogénea)
lista3 = ['nombre', ['ap1', 'ap2']]  # declara lista dentro de otra
lista4 = [54,45,44,22,0,2,99]  		 # declara una lista numérica

print(lista1)  				 # ['uno', 2, True], muestra toda la lista
print(lista1[0])  			 # uno, muestra el primer elemento de la lista
print(lista2[-1])  			 # 5, muestra el último elemento de la lista
print(lista3[1][0])  			 # calle, primer elemento de la lista anidada
print(lista2[0:3:1])  			 # [1,2,3], responde al patrón inicio:fin:paso
print(lista2[::-1])  			 # devuelve la lista ordenada al revés

lista1[2] = False  			        # cambia el valor de un elemento de la lista
lista2[-2] = lista2[-2] + 1  		# 4+1 → 5 – cambia valor de elemento

lista2.pop(0)  				    # borra elemento indicado o último si no indica
lista1.remove('uno')  			# borra el primer elemento que coincida
del lista2[1]  			 	    # borra el segundo elemento (por índice)  

lista2 = lista2 + [6]  			# añade elemento al final de la lista
lista2.append(7)  			    # añade un elemento al final con append()
lista2.extend([8, 9]) 			# extiende lista con otra por el final
lista1.insert(1, 'dos')  		# inserta nuevo elemento en posición

del lista2[0:3]  				# borra los elementos desde:hasta
lista2[:] = []  				# borra todos los elementos de la lista 

print(lista1.count(2)) 			# cuenta el nº de veces que aparece 2
print(lista1.index("dos"))  	# busca posición que ocupa elemento

lista4.sort()  				    # ordena la lista
lista4.sort(reverse=True)  		# ordena la lista en orden inverso

lista5 = sorted(lista4)  		# ordena lista destino 
# =========================== Tuplas ============================

tupla1 = (1, 2, 3)  			# declara tupla (se usan paréntesis)...
tupla2 = 1, 2, 3  			    # ...aunque pueden declararse sin paréntesis
tupla3 = (100,)  			    # con un elemento hay terminar con “,”
tupla4 = tupla1, 4, 5, 6  		# anida tuplas
tupla5 = ()  				    # declara una tupla vacía
tupla6 = tuple([1, 2, 3, 4, 5])  		 # Convierte una lista en una tupla
tupla2[0:3]  				    # (1, 2, 3), accede a los valores desde:hasta
# ============================ Diccionario ============================

dic1 = {'Lorca':'Escritor', 'Goya':'Pintor'} 	    # declara diccionario 
print(dic1) 					                    # {'Goya': 'Pintor', 'Lorca': 'Escritor'}

dic2 = dict((('mesa',5), ('silla',10))) 		    # declara a partir de tupla
dic3 = dict(ALM=5, CAD=10) 			                # declara a partir de cadenas simples 

print(dic1['Lorca'])  				                # escritor, acceso a un valor por clave
print(dic1.get('Gala', 'no existe'))  		        # acceso a un valor por clave

if 'Lorca' in dic1: print('está')  			        # comprueba si existe una clave

print(dic1.items())  				    # obtiene una lista de tuplas clave:valor
print(dic1.keys())  				    # obtiene una lista de las claves
print(dic1.values())  				    # obtiene una lista de los valores

dic1['Lorca'] = 'Poeta'  				    # añade un nuevo par clave:valor
dic1['Amenabar'] = 'Cineasta'  			    # añade un nuevo par clave:valor
dic1.update({'Carreras' : 'Tenor'}) 		# añadir con update()
del dic1['Amenabar']  				        # borra un par clave:valor 
print(dic1.pop('Amenabar', 'no está'))  	# borra par clave:valor


artistas = {'Lorca':'Escritor', 'Goya':'Pintor'} 		# diccionario
paises = ['Chile','España','Francia','Portugal'] 		# declara lista
capitales = ['Santiago','Madrid','París','Lisboa']  	# declara lista
for c, v in artistas.items():       # c:clave - v:valor 
    print(c,':',v)  		      # recorre diccionario
for i, c in enumerate(paises):      # [i]:indice - c:clave
    print(i,':',c)  		       # recorre lista 
for p, c in zip(paises, capitales):  
    print(c,' ',p) 		           # recorre listas
for p in reversed(paises): 
    print(p,)  			# recorre en orden inverso
for c in sorted(paises): 
    print(c,)  			# recorre secuencia ordenada


cadena = 'Python' 					# asigna cadena a variable
lista = [1, 2, 3, 4, 5]  					# declara lista
if 'y' in cadena: 
    print('“y” está en “Python”')  		# contiene
if 6 not in lista: 
    print('6 no está en la lista') 		# no contiene
if 'abcabc' == 'abc' * 2: 
    print('Son iguales')  		# son iguales
#----------------------------------------------------

