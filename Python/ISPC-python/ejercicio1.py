# https://github.com/narcisoperez/3SemanaProgramacion_110521
# https://github.com/narcisoperez/3erSemanaProg/blob/main/03Semana3Prog.ipynb

# Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
# Cn = C * (1 + x/100) ^ n
# Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.
C=int("3")
x=int("5")
n=int("2")
Cn=C*( (1+x/100)**n)
print(Cn)


#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
C=int("25")
F= 9/5*C+32
print(F)

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla el nombre en mayúsculas y el número de caracteres que contiene en líneas distintas.

name="giovanny aguilar "
NAME=name.upper()
cantidad=0
for i in name:
    if(i!=" "):
        cantidad=cantidad+1
print("name: "+NAME)
print("cantidad de caracter: ",cantidad)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad=int("-1")


if( int(edad)<0):
    print("NO EXISTE ESA EDAD!!")
if(int(edad)<18):
    print("es MENOR de edad")
else:
    print("es MAYOR de edad")

#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a $1000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

