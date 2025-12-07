class Dispositivo:
    """Clase base para dispositivos con un método 'encender'."""
    def encender(self):
        return "Dispositivo encendido."

class Laptop(Dispositivo):
    """Laptop sobreescribe 'encender' con una secuencia de arranque más larga."""
    def encender(self):
        return "Presionando el botón... Iniciando sistema operativo de la Laptop."

class Telefono(Dispositivo):
    """Teléfono sobreescribe 'encender' con una respuesta rápida."""
    def encender(self):
        return "Presionando la pantalla... El Teléfono se ilumina instantáneamente."

print("\n--- 5. Dispositivo ---")
dispositivo_generico = Dispositivo()
mi_laptop = Laptop()
mi_telefono = Telefono()

print(f"Dispositivo genérico: {dispositivo_generico.encender()}")
print(f"Laptop: {mi_laptop.encender()}")
print(f"Teléfono: {mi_telefono.encender()}")