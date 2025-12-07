import math

class Figura:
    
    def area(self):
        raise NotImplementedError("Las clases derivadas deben implementar este método.")

class Circulo(Figura):
   
    def __init__(self, radio):
        self.radio = radio

    def area(self):
      
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
  
    def __init__(self, lado):
        self.lado = lado

    def area(self):
      
        return self.lado * self.lado


print("\n--- 3. Figura ---")
circulo1 = Circulo(radio=5)
cuadrado1 = Cuadrado(lado=4)

print(f"Área del Círculo (radio 5): {circulo1.area():.2f}")
print(f"Área del Cuadrado (lado 4): {cuadrado1.area()}")