

numero_secreto = 7
adivinanza = -1
intentos = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número secreto: "))
    intentos = intentos + 1
    
    if adivinanza < numero_secreto:
        print("El número es mayor")
    elif adivinanza > numero_secreto:
        print("El número es menor")
    else:
        print(f"¡Correcto! Adivinaste en {intentos} intentos")
