class Empleado:
   
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
       
        return self.salario * 0.05 

class Gerente(Empleado):
   
    def calcular_bono(self):
     
        return self.salario * 0.15

class Tecnico(Empleado):

    def calcular_bono(self):
       
        return 500.00

print("\n--- 2. Empleado ---")
empleado1 = Empleado("Mikeas", 30000)
gerente1 = Gerente("Luis", 60000)
tecnico1 = Tecnico("Migui", 25000)

print(f"{empleado1.nombre} (Bono Base): ${empleado1.calcular_bono():.2f}")
print(f"{gerente1.nombre} (Bono Gerente): ${gerente1.calcular_bono():.2f}")
print(f"{tecnico1.nombre} (Bono Técnico): ${tecnico1.calcular_bono():.2f}")