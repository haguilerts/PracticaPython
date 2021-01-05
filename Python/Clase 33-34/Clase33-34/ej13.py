#           IMPLEMENTACION DE OBJETOS 

class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        Catalogo.peliculas.append(p)

    def mostrar(self):
        for p in Catalogo.peliculas:
            print(p)  # Print toma por defecto str(p)


p = Pelicula("El Padrino", 175, 1972)
c = Catalogo([p])  # Añado una lista con una película desde el principio
c.mostrar()
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  # Añadimos otra
c.mostrar()

# ----------------- COMPARACION DE OBJETOS ----------------------------

class Persona():

    def __init__(self, nombre, edad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def __gt__(self, persona):
        return self.edad > persona.edad 

    def __lt__(self, persona):
        return self.edad < persona.edad

    def __ge__(self, persona):
        return self.edad >= persona.edad

    def __le__(self, persona):
        return self.edad <= persona.edad

    def __eq__(self, persona):
        return self.edad == persona.edad

    def __ne__(self, persona):
        return self.edad != persona.edad

print("-------------- comparacion ------------------")
# http://elclubdelautodidacta.es/wp/2015/06/comparando-objetos-en-python/
pedro = Persona("Pedro", 62, 1.65, 71)
luis = Persona("Luis", 40, 1.80, 82)
carmen = Persona("Carmen", 62, 1.70, 60)

#  || '>' __gt__ // '<' __lt__ // '>=' __ge__ // '<=' __le__ // '==' __eq__ // '!=' __ne__  ||
print( pedro.__gt__(luis) ) # true
print( luis.__gt__(pedro) ) # false

print( pedro.__eq__(carmen) )   # true
print( luis.__le__(pedro) )     # true



