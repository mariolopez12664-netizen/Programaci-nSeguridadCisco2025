import tkinter as tk

def agregar():
    item = entrada.get()
    if item:
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Ejercicio 4")
ventana.geometry("300x300")

lista = tk.Listbox(ventana, width=25)
lista.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Agregar", command=agregar)
boton.pack(pady=5)

ventana.mainloop()
