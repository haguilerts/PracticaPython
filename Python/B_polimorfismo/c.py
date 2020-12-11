# import B_polimorfismo.a
from a import A
from b import B

class C(B,A): # en es caso lo herede de A y B por lo tanto pra evitar conflictos B piso a A

    def __init__(self):
        print("Soy de la clase C")
        
    def c(self):
        print("Este método es de C")