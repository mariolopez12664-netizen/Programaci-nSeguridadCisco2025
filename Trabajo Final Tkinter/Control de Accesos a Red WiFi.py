import tkinter as tk
from tkinter import messagebox, ttk

# ---------------- MODELO ----------------
class Dispositivo:
    def __init__(self, usuario, mac, ip):
        self.usuario = usuario
        self.mac = mac
        self.ip = ip

# ---------------- APLICACIÓN ----------------
class ControlWiFiApp:
    def __init__(self, master):
        self.master = master
        master.title("Control de Acceso WiFi")
        master.geometry("800x500")

        # Lista (vector) de dispositivos
        self.dispositivos = []  

        # Matriz de conexiones: usuario -> lista de IPs
        self.historial = {}     

        self.limite_conexiones = 3

        self._crear_interfaz()
        self._crear_tabla()

    # ---------------- INTERFAZ ----------------
    def _crear_interfaz(self):
        frm = tk.Frame(self.master)
        frm.pack(padx=10, pady=10, anchor="nw")

        tk.Label(frm, text="Usuario:").grid(row=0, column=0)
        tk.Label(frm, text="MAC:").grid(row=1, column=0)
        tk.Label(frm, text="IP:").grid(row=2, column=0)

        self.var_usuario = tk.StringVar()
        self.var_mac = tk.StringVar()
        self.var_ip = tk.StringVar()

        tk.Entry(frm, textvariable=self.var_usuario).grid(row=0, column=1, pady=3)
        tk.Entry(frm, textvariable=self.var_mac).grid(row=1, column=1, pady=3)
        tk.Entry(frm, textvariable=self.var_ip).grid(row=2, column=1, pady=3)

        tk.Button(frm, text="Registrar", command=self.registrar_dispositivo).grid(row=3, column=0, pady=6)
        tk.Button(frm, text="Validar Acceso", command=self.validar_acceso).grid(row=3, column=1, pady=6)
        tk.Button(frm, text="Generar Alertas", command=self.generar_alertas).grid(row=3, column=2, pady=6)

    # ---------------- TABLA ----------------
    def _crear_tabla(self):
        columnas = ("usuario", "mac", "ip")

        self.tabla = ttk.Treeview(self.master, columns=columnas, show='headings')
        self.tabla.heading("usuario", text="Usuario")
        self.tabla.heading("mac", text="MAC")
        self.tabla.heading("ip", text="IP")

        self.tabla.pack(padx=10, pady=10, fill="both", expand=True)

    # ---------------- FUNCIONES PRINCIPALES ----------------
    def registrar_dispositivo(self):
        usuario = self.var_usuario.get().strip()
        mac = self.var_mac.get().strip()
        ip = self.var_ip.get().strip()

        if not (usuario and mac and ip):
            messagebox.showwarning("Validación", "Todos los campos son obligatorios.")
            return

        # Registrar en vector
        disp = Dispositivo(usuario, mac, ip)
        self.dispositivos.append(disp)

        # Registrar en matriz (historial)
        if usuario not in self.historial:
            self.historial[usuario] = []
        self.historial[usuario].append(ip)

        self.tabla.insert('', 'end', values=(usuario, mac, ip))
        messagebox.showinfo("OK", "Dispositivo registrado.")

    def validar_acceso(self):
        usuario = self.var_usuario.get().strip()

        if usuario not in self.historial:
            messagebox.showerror("Acceso Denegado", "Usuario no registrado.")
            return

        conexiones = len(self.historial[usuario])

        if conexiones > self.limite_conexiones:
            messagebox.showerror(
                "Límite Excedido",
                f"El usuario '{usuario}' excede el límite de {self.limite_conexiones} conexiones."
            )
        else:
            messagebox.showinfo("Acceso Permitido", "El usuario está dentro del límite de conexiones.")

    def generar_alertas(self):
        alertas = []

        for usuario, conexiones in self.historial.items():
            if len(conexiones) > self.limite_conexiones:
                alertas.append(f"Usuario {usuario} excede conexiones: {len(conexiones)}")

        if not alertas:
            messagebox.showinfo("Alertas", "No hay accesos sospechosos.")
        else:
            messagebox.showwarning("Alertas", "\n".join(alertas))

# ---------------- MAIN ----------------
if __name__ == '__main__':
    root = tk.Tk()
    app = ControlWiFiApp(root)
    root.mainloop()