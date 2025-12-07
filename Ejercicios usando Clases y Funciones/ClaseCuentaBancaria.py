class CuentaBancaria:
    def __init__(self, titular, balance=0.0):
        
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
     
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depósito de ${cantidad:.2f} realizado.")
        else:
            print("La cantidad a depositar debe ser positiva.")
        self.mostrar_balance()

    def retirar(self, cantidad):
 
        if cantidad > 0:
            if self.balance >= cantidad:
                self.balance -= cantidad
                print(f"Retiro de ${cantidad:.2f} realizado.")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")
        self.mostrar_balance()

    def mostrar_balance(self):
       
        print(f"Balance actual de la cuenta de {self.titular}: ${self.balance:.2f}")


print("\n--- CuentaBancaria ---")
cuenta1 = CuentaBancaria("Mikeas Medina", 100.00)
cuenta1.mostrar_balance()

cuenta1.depositar(50.00)
cuenta1.retirar(25.50)
cuenta1.retirar(300.00) 