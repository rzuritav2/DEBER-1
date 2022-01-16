

print ("Ingrese la cantidad de empleados:")
ce = int( input())
i = 1
smayor = 0.0 #Inicializando Real
print("Ingrese los sueldos: ")
while i <= ce :
  sueldo = int( input("Ingrese sueldo {0}: ")
if sueldo > smayor :
   smayor = sueldo
   c = i
i = i + 1
#Salida
print("\nSALIDA: ")
print ("El empleado numero ", c, "tiene el mayor sueldo que es:", smayor)