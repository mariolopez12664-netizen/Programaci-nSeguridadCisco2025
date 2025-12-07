import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 1")
ventana.geometry("300x150")

label = tk.Label(ventana, text="¡Bienvenido a Tkinter!", font=("Arial", 14))
label.pack(pady=20)

ventana.mainloop()
