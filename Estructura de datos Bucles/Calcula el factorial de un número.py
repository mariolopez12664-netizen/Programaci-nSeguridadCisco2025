
numero = int(input("Ingresa un número para calcular su factorial: "))

factorial = 1
contador = numero

while contador >= 1:
    factorial = factorial * contador
    contador = contador - 1

print(f"El factorial de {numero} es: {factorial}")
