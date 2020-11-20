### No intentes entender este código, sólo fíjate en cómo se utiliza abajo  
"""
# Creo una estructura para los clientes
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:
    def __init__(self, clientes):
        self.clientes = clientes
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras 
# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")# el orden segun es constructor 

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)

"""
class Gato:
    especie="mamifero"      # es un atributo de clases (similar a un static constante)
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[]
    def verEtapaDeVida(self):
        if self.edad>18:
            print(self.nombre," es adulto")
        else:
            print(self.nombre," es cachorro")
    def esAlimentoFovorito(self, alimento):
        return alimento in self.alimentos

myGato=Gato("felin",2)
print(myGato) #<__main__.Gato object at 0x000002544DA1EFD0>
print(myGato.nombre)
print(myGato.edad)
myGato.alimentos.append("pescado")
myGato.alimentos.append("leche")
myGato.alimentos.append("chocolatada")
print(myGato.alimentos)
myGato.alimentos=["galleta","chocolate"] #remplazo los valores de la lista
print(myGato.alimentos)
print(myGato.especie)
myGato.color="negro" # agrego un nuevo atributo
print(myGato.color)

print("-----------------")
tom=Gato("Pelusa",20)
tom.verEtapaDeVida()
tom.edad=10
tom.verEtapaDeVida()
tom.alimentos=["lechess","pan","factura"]
print(tom.alimentos)
print(tom.esAlimentoFovorito("lechess")) #true
print(tom.esAlimentoFovorito("LECHESS"))  #false

print("tom: ",tom.especie)          # mamifero
print("myGato: ",myGato.especie)    # mamifero
print("Gato: ",Gato.especie)    # mamifero




