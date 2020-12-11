### No intentes entender este código, sólo fíjate en cómo se utiliza abajo  

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




