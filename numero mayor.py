#15
n1 = int(input("ingres el primeronumero:"))
n2 = int(input("ingres el pegundo numero:"))
n3 = int(input("ingres el tercer numero:"))
if n2<n1>n3:
    print("el numero mayor es el primer numero:",n1,)
elif n1<n2>n3:
    print("el numero segundo mayor es segundo numero:",n3,)
elif n1<n2>n2:
     print("el numero mayor es el primer numero:",n2,)
else:
    print("todos los numeros son iguales")