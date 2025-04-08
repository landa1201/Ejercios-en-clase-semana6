class persona:
    def __init__ (self,nombre, edad ):
        self.nombre=nombre 
        self.edad = edad 

class estudiante (persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado= grado 

loraine= estudiante ("Loraine", "22", "tercero")
print (loraine.nombre )
print (loraine.edad )
print (loraine.grado )
