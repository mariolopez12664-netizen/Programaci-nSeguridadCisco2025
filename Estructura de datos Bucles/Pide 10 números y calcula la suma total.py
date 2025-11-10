
suma = 0
contador = 1

while contador <= 10:
    numero = float(input(f"Ingresa el número {contador}: "))
    suma = suma + numero
    contador = contador + 1

promedio = suma / 10

print(f"\nLa suma total es: {suma}")
print(f"El promedio es: {promedio}")
