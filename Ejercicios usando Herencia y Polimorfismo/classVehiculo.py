class Vehiculo:
  
    def mover(self):
        return "El vehículo se está moviendo."

class Carro(Vehiculo):
   
    def mover(self):
        return "El carro arranca y se mueve con motor a cuatro ruedas."

class Bicicleta(Vehiculo):

    def mover(self):
        return "La bicicleta se mueve impulsada por pedales."

print("\n--- 4. Vehiculo ---")
vehiculo_generico = Vehiculo()
mi_carro = Carro()
mi_bici = Bicicleta()

print(f"Vehículo genérico: {vehiculo_generico.mover()}")
print(f"Carro: {mi_carro.mover()}")
print(f"Bicicleta: {mi_bici.mover()}")