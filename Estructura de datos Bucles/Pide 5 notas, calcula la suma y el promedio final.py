
suma = 0
contador = 1

while contador <= 5:
    nota = float(input(f"Ingresa la nota {contador}: "))
    suma = suma + nota
    contador = contador + 1

promedio = suma / 5

print(f"\nSuma total de notas: {suma}")
print(f"Promedio final: {promedio}")
