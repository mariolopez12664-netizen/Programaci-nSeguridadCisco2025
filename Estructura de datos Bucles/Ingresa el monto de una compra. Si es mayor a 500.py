
monto = float(input("Ingresa el monto de la compra: "))

if monto > 500:
    descuento = monto * 0.10
    total = monto - descuento
    print(f"Monto original: ${monto:.2f}")
    print(f"Descuento (10%): ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
else:
    print(f"Total a pagar: ${monto:.2f}")
