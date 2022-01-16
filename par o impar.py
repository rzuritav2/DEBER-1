#Dado un (1) número, imprimir 0 si es par y 1 si es impar
numero = int(input("Introduce un número: "))
if numero == 0:
    print ("Este número es par:")
elif numero %2 == 0:
    print ("Este numero es par:")
else:
    print ("Este numero es impar:")