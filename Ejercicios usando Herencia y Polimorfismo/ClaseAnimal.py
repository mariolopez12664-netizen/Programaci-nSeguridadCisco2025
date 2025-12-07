class Animal:
    """Clase base con el método general 'hablar'."""
    def hablar(self):
        return "El animal hace un sonido genérico."

class Perro(Animal):
    """Clase hija que sobreescribe el método hablar para un perro."""
    def hablar(self):
        return "Guau, guau!"

class Gato(Animal):
    """Clase hija que sobreescribe el método hablar para un gato."""
    def hablar(self):
        return "Miau!"


print("--- 1. Animales ---")
animal_generico = Animal()
perro1 = Perro()
gato1 = Gato()

print(f"Animal: {animal_generico.hablar()}")
print(f"Perro: {perro1.hablar()}")
print(f"Gato: {gato1.hablar()}")