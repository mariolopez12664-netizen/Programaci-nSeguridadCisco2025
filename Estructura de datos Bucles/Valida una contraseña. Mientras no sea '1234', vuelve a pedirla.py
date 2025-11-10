
contraseña_correcta = "1234"
contraseña = input("Ingresa la contraseña: ")

while contraseña != contraseña_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña = input("Ingresa la contraseña: ")

print("¡Contraseña correcta! Acceso permitido.")
