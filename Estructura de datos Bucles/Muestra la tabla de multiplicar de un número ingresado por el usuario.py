
numero = int(input("Ingresa un número para su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:\n")

multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador = multiplicador + 1
