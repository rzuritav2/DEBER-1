#12
n = int(input("ingrese un numero:"))
if n > 4 and n < 500:
   a = n // 100
   b = n % 10
   if a == b:
    print("el numero",n," es un numero capicua")
   else:
    print("el numero",n,"no es numero capcua")
else:
    print("ingrese un numero de 2 digitos")