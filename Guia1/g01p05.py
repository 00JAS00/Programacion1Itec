# Leer dos números reales y mostrarlos en orden creciente.
print("Ingresar dos números reales y se mostraran en orden creciente:\n")
n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
if (n1<n2):
    print("El primer numero es menor y el segundo es mayor:")
    print("Orden Creciente: ",n1,":",n2)
else:
    print("El primer numero es mayor y el segundo es menor")
    print("Orden Creciente: ",n2,":",n1)