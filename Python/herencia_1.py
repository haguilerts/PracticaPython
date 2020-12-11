class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.materia=[]
        self.myMateria={} # es un diccionario
        self.__alumno='' #atributo privado
        self.__prof='' #atributo privado


    def __metodo_Privado():
        return self.__prof
    def agregarMaterias(self,materia,codigo):
        self.myMateria[codigo]=materia
    def setAlumno(self,alum):
        self.__alumno=alum
    def getAlumno(self):
        return self.__alumno
#----------------------------------------------------
class Materia:
    def __init__(self,nomMateria, profesor,fecha=None):
        self.nombre=nomMateria
        self.profesor=profesor
        self.fechaInicioDictado=fecha
    # GET 
    @property
    def fechaInicioDictado(self):
        print("getFecha:")
        return self._fechaInicioDictado
    # SET
    @fechaInicioDictado.setter
    def fechaInicioDictado(self,fecha):
        if fecha<2006:
            self._fechaInicioDictado=2006
        else:
            self._fechaInicioDictado=fecha
#----------------------------------------------------
ing=Carrera("ingenieria")
algebra=Materia("Algebra","Ricardo Quintero",2010)
fisica=Materia("Fisica","Margarita Gomez",2006)
quimica=Materia("Quimica","Lorena Rios",2003)

print("Materia: %s - Prof: %s - año: %d" %(algebra.nombre, algebra.profesor,algebra.fechaInicioDictado) )
print("Materia: %s - Prof: %s - año: %d" %(fisica.nombre, fisica.profesor,fisica.fechaInicioDictado) )

ing.materia.append((123,algebra)) # añado un array con un obj
ing.materia.append((456,fisica))

print("ingAlgebra: ",len(ing.materia))              # ingAlgebra:  2

ing.agregarMaterias(algebra.nombre,103061)
print("myMateria: ",ing.myMateria)                  # myMateria:  {103061: 'Algebra'}

print("fechaAlgebra: ",algebra.fechaInicioDictado)  # 2010
print("fechaQuimica: ",quimica.fechaInicioDictado)  # 2006
ing.setAlumno("Brandon")
print("alumno: ",ing.getAlumno())

#----------------------Porlimorfismo (sobre escribir metodos)------------------------------
class Empleado:
    def __init__(self, nom, leg, sueldoBruto):
        self.nombre=nom
        self.legajo=leg
        self.sueldo=sueldoBruto
    def calcularSueldo(self,decuento):
        return self.sueldo-decuento
#----------------------------------------------------
class Gerente(Empleado):
    def calcularSueldo(self,decuento, bonoficaciones=100):
        return self.sueldo-decuento+bonoficaciones
#----------------------------------------------------

marco=Empleado("Marco Rios",103061, 5000 )
julia=Gerente("Julia Campos", 103162, 3000)

print("sueldo de Marcos: ",marco.calcularSueldo(1000))      # 4000
print("sueldo de Julia: ",julia.calcularSueldo(100,500))    # 3400
print("sueldo de Julia: ",julia.calcularSueldo(100))        # 3000




