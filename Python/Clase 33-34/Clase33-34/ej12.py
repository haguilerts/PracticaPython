class Ejemplo: 
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.") 

    def atributo_publico(self): 
        return self.__atributo_privado 

    def metodo_publico(self): 
        return self.__metodo_privado() 

e = Ejemplo() 
print(e.atributo_publico())

# OTRA FORMA DE HACERLO .....
class ListadoBebidas:

    def __init__(self):
        self.__bebida = 'Naranja'
        self.__bebidas_validas = ['Naranja', 'Manzana']

    #getters
    @property
    def bebida(self):
        return "La bebida oficial es: {}".format(self.__bebida)

    #setters
    @bebida.setter
    def bebida(self, bebida):
        self.__bebida = bebida

bebidas = ListadoBebidas()
print(bebidas.bebida)
bebidas.bebida = 'Limonada'
print(bebidas.bebida)