class veterinaria:
    def __init__ (self,nombre , especie ):
        self.nombre=nombre 
        self.especie =especie



class animal (veterinaria):
    def __init__(self, nombre, especie,raza):
        super().__init__(nombre,especie)
        self.raza=raza

rocky= animal ("rocky", "canino", "dalmata")

print (rocky.nombre)
print (rocky.especie)
print (rocky.raza )