import tkinter as tk

def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {n1 + n2}")
    except ValueError:
        resultado.config(text="Error: Solo números")

ventana = tk.Tk()
ventana.title("Ejercicio 3 - Suma")
ventana.geometry("300x250")

tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="Resultado: ")
resultado.pack()

ventana.mainloop()
