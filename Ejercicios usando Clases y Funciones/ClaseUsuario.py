class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
            
usuario1 = Usuario("Ana", 28)
usuario1.mostrar_datos()