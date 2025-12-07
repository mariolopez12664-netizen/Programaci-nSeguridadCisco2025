class Estudiante:
    def __init__(self, nombre, calificaciones):
       
        self.nombre = nombre
        self.calificaciones = calificaciones 

    def calcular_promedio(self):
   
        if not self.calificaciones:
            return 0.0 

       
        suma_calificaciones = sum(self.calificaciones)
        promedio = suma_calificaciones / len(self.calificaciones)
        return promedio


print("\n--- Estudiante ---")
estudiante1 = Estudiante("Mikeas Medina", [99, 99, 90.5, 95.0])
promedio_estudiante = estudiante1.calcular_promedio()

print(f"Estudiante: {estudiante1.nombre}")
print(f"Calificaciones: {estudiante1.calificaciones}")
print(f"El promedio de calificaciones es: {promedio_estudiante:.2f}")

   