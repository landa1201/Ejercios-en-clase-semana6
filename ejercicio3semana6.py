class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año



class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo


mi_coche = Coche("Toyota", 2020, "Corolla")

        
print (mi_coche.marca)
print (mi_coche.año)
print (mi_coche.modelo)
