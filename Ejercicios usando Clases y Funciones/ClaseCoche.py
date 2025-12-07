class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad 

    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Velocidad: {self.velocidad} km/h")

    def aumentar_velocidad(self, incremento):
        self.velocidad += incremento
        print(f"El {self.marca} va ahora a {self.velocidad} km/h")

    def mostrar_informacion(self):
        print(f"Marca: {self.marca} | Velocidad: {self.velocidad} km/h")


el_coche = Coche("Honda", 100)


el_coche.mostrar_informacion()

el_coche.aumentar_velocidad(30)


el_coche.mostrar_informacion()
