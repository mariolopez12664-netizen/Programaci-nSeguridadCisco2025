import tkinter as tk

def dibujar(event):
    canvas.create_line(event.x, event.y, event.x+1, event.y+1)

ventana = tk.Tk()
ventana.title("Ejercicio 5 - Dibujar")
ventana.geometry("400x400")

canvas = tk.Canvas(ventana, bg="white", width=380, height=380)
canvas.pack(pady=10)

canvas.bind("<B1-Motion>", dibujar)

ventana.mainloop()
