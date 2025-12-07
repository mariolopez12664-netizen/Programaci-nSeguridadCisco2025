class Rectangulo:
    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def calcular_area(self):
   
        area = self.base * self.altura
        return area

print("\n--- Rectangulo ---")
rectangulo1 = Rectangulo(base=10, altura=5)
area_rectangulo = rectangulo1.calcular_area()
print(f"Base: {rectangulo1.base}, Altura: {rectangulo1.altura}")
print(f"El área del rectángulo es: {area_rectangulo}")