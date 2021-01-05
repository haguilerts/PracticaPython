class Punto:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({},{})".format(self.x,self.y)


# bloque principal

punto1=Punto(10,3)
punto2=Punto(3,4)
print(punto1)
print(punto2)
# al no estars el toString (__str__()) e imprimomos el objeto nos muestra solo el espacio de memoria
# pero una ves añadido muestra su contenido.
# un cosntructos es similiar a un SET, -- mientras un toString es similar a un  GET.
 