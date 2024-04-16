# Bucles
# iteraciones de cantidad determindos
print("antes  del For")

# el forhace dos cosas automaticamente:
# 1.asigna elvalor inicial a la variable 2. la incrementa cada vuelta
for x in range(3):
    print(x," hola")
    print("Dentro Del FOR")

print("despues del For")

# el for con range, tiene los siguientes elementos:
# variable de recorrido: que se va a mover por el rango, desde valor inicial hasta valor final-1
# valor iniciañ puede no ponerse y en ese caso asume cero

valorInicial= 3
valorFinal= 7
for variable in range(valorInicial,valorFinal):
    print("chau: ",variable)

# iteraciones de cantidad indeterminada
# primer ejemplo: simulacion de for, para mostrar que no es lo mas apropiado
x=0
while x<3:
    print(x,"Hola")
    x=x+1 # x  es un contador (se incrementa de 1 en 1)

# ejemplo apropiado, con cantidad indeterminadad e iteraciones
sigue=""
while sigue!="fin":
    print("dentro del while")
    n=int(input("ingrese un numero: "))
    print("el doble es: ",n*2)
    sigue=input("desea continuar? (fin para terminar) ")
print("gracias por participar")

# Ordenamiento de instucciones de control de flujo
n=0
while n<5:
    print("dentro del while")
    n=n+1
    print(n)
    if n==3:
        print("llego el 3!!!!")
print("afuera del while porque dejo de cumplir la condicion")


