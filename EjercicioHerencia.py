class persona:
    def __init___(self,nombre,edad, nacionalidad ):
        self.nombre=nombre 
        self.edad= edad
        self.nacionalidad= nacionalidad 

    def saludar (self):
        print("hola como estas? ")

class empleado (persona):
    def __init__(self,nombre,edad, nacionalidad,salario, puesto):
        super().__init__(nombre,edad, nacionalidad)
        self.salario= salario
        self.puesto= puesto

pepito= empleado ("pepito",35, "colombiano", 1400000, "programador")
juan= persona("juan", "32", "tangamandapio")


print(pepito.nombre)
print(pepito.edad) 
print(pepito.nacionalidad) 
print(pepito.salario) 
print(pepito.puesto)

pepito.saludar()
print(juan.nombre)
print(juan.edad)
print(juan.nacionalidad)
