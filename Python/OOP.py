class Persona:

    piernas=2

    def inicializar(self,nombre):
        self.nombre=nombre

    def imprimir(self):
        print("Nombre: {}".format(self.nombre))

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()
print(persona1.piernas)

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()
# -----------------------------------------------------------------------------
class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Desaprobado")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("Diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("Ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()
# -----------------------------------------------------------------------------
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def __del__(self):
        print('Método delete llamado')

    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Sueldo: {}".format(self.sueldo))

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

# bloque principal

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
# -----------------------------------------------------------------------------
class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    @staticmethod
    def metodo_estatico():
        print("método estático")

    def imprimir(self):
        print("Coordenada del punto")
        print("({}:{})".format(self.x,self.y))

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrante")
        elif self.x<0 and self.y>0:
            print("Segundo cuadrante")
        elif self.x<0 and self.y<0:
            print("Tercer cuadrante")
        else: 
            print("Cuarto cuadrante")

# bloque principal

punto1=Punto(10,-30)
Punto.metodo_estatico()
punto1.imprimir()
punto1.imprimir_cuadrante()
# -----------------------------------------------------------------------------
class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es: {}".format(suma))

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es: {}".format(resta))

    def multiplicar(self):
        producto=self.valor1*self.valor2
        print("El producto es: {}".format(producto))

    def dividir(self):
        division=self.valor1/self.valor2
        print("La division es: {}".format(division))


# bloque principal

operacion1=Operacion()
# -----------------------------------------------------------------------------
class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()

    def cargar(self):
        for x in range(5):
            nombre=input("Ingrese nombre del alumno:")
            self.nombres.append(nombre)
            nota=int(input("Nota del alumno:"))
            self.notas.append(nota)

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print("{} - {}".format(self.nombres[x],self.notas[x]))
        print("_____________________")            

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print("{} - {}".format(self.nombres[x],self.notas[x]))
        print("_____________________")                


# bloque principal
alumnos=Alumnos()
alumnos.menu()
# -----------------------------------------------------------------------------
class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def extraer(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print("{} tiene depositada la suma de {}".format(self.nombre,self.monto))


class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es: {}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


# bloque principal        

banco1=Banco()
banco1.operar()
banco1.depositos_totales()
# -----------------------------------------------------------------------------
import random

class Dado:

    def tirar(self):
        self.valor=random.randint(1,6)

    def imprimir(self):
        print("Valor del dado: {}".format(self.valor))

    def retornar_valor(self):
        return self.valor


class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Ganó")
        else:
            print("Perdió")


# bloque principal del programa

juego_dados=JuegoDeDados()
juego_dados.jugar()
# -----------------------------------------------------------------------------
class Cliente:
    suspendidos=[]

    @staticmethod
    def get_suspendidos():
        return Cliente.suspendidos

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo: {}".format(self.codigo))
        print("Nombre: {}".format(self.nombre))
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


# bloque principal

cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()   
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.get_suspendidos())
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------
class Familia:

    def __init__(self,padre,madre,hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        cadena=self.padre+","+self.madre
        for hijo in self.hijos:
            cadena=cadena+","+hijo
        return cadena


# bloque principal

familia1=Familia("Pablo","Ana",["Pepe","Julio"])
familia2=Familia("Jorge","Carla")
familia3=Familia("Luis","Maria",["Marcos"])

print(familia1)
print(familia2)
print(familia3)
# -----------------------------------------------------------------------------
class ListadoBebidas:

    def __init__(self):
        self.__bebida = 'Naranja'
        self.__bebidas_validas = ['Naranja', 'Manzana']

    @property
    def bebida(self):
        return "La bebida oficial es: {}".format(self.__bebida)

    @bebida.setter
    def bebida(self, bebida):
        self.__bebida = bebida

bebidas = ListadoBebidas()
print(bebidas.bebida)
bebidas.bebida = 'Limonada'
print(bebidas.bebida)
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
