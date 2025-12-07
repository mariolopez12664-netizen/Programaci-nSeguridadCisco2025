import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    label_resultado.config(text=f"Texto: {texto}")

ventana = tk.Tk()
ventana.title("Ejercicio 2")
ventana.geometry("300x200")

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack()

label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

ventana.mainloop()
