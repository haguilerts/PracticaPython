class Empleado: #clase padre 
    def __init__(self,nombre,edad,legajo,sueldo):
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.sueldoBase=sueldo
    def calcularSueldo(self, descuento, bonos):
        self.sueldoBase = descuento+bonos
        return self.sueldoBase 

class AgenteVentas(Empleado): # clase hija
    def __init__(self,mostrador,nombre,edad,legajo,sueldo):
        self.numeroMostrar=mostrador
        super().__init__(nombre,edad,legajo,sueldo)

class Tripulantes(Empleado):
    def mostrarRenovacionLicencia(self):
        if self.edad<50:
            print("renovar la licencia cada 1 año")
        else:
            print("renovar la licencia cada 6 año")




pedro=AgenteVentas(4,"Pedro Martines",25,103061,50.000)
print(pedro.nombre)
print(pedro.calcularSueldo(100,3000))


lucas=Tripulantes("lucas",60,120210,40.000)
lucas.mostrarRenovacionLicencia()