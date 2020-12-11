#las funciones lo lee de arriba hacia abajo asta llamar a la funcion
# si llamo antes de q la funcion sea ejecutada dara un error 


def suma(s1,s2):
    return s1 + s2
def calculo(num1=0, num2=0):
    sum=suma(num1,num2)
    res=resta(num1,num2)
    print("suma: %d - Resta: %d "%(sum,res))
def resta(r1,r2):
    return r1 - r2
calculo(5,4) # 9 
calculo()
print("suma(String): ",suma('1','2'))
#-------------------------------------------------
class clase1:
    def multiplicar(n1,n2):
         print("mult: ",(n1 * n2))
    def repetir(cad,r=3): # cad: toma la variable y me repite 3 veces 
        print(cad*r)
    def repetir1(cad, v=2, *tupla): # todo los parametros q estan por demas se gurda dentro de la tupla
        print(cad*v)
        for cadena in tupla:
            print(cadena)
    def repetir2(cad ,v=1, **diccionario): #
        print(cad*v)
        print(diccionario['saludar'])
        print(diccionario['adios'])
#-------------------------------------------------
clase1.multiplicar(2,3)     # 6
clase1.repetir("- gio ")    # - gio - gio - gio
clase1.repetir("- gio ",2)  # - gio - gio 
clase1.repetir1("- rhonny ",2,'hola',' mundo',' como',' estan!!\n')  # - gio - gio 
clase1.repetir2("- kevin ",2, saludar='hello!!', adios="gootBye")  

#*****************************************************

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es: {}".format(suma))

def separacion():
    print("*******************************")    

# programa principal

for x in range(5):
    carga_suma()
    separacion()

def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may

def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    

# bloque principal del programa

lista_valores=[10, 56, 23, 120, 94]
print("La lista completa es: {}".format(lista_valores))
print("La suma de todos su elementos es: {}".format(sumarizar(lista_valores)))
print("El mayor valor de la lista es: {}".format(mayor(lista_valores)))
print("El menor valor de la lista es: {}".format(menor(lista_valores)))

