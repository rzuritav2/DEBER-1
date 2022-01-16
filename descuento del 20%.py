total = float(input("ingrese total de compras:"))
descuento = float()
if total > 100:
    descuento = total * 0.20   
      
else:
    descuento = 0
print("el descuento aplicado es : ",descuento)
print("el total a pagar es:$",total - descuento)

