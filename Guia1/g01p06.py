# Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
print("ingrese los dos numeros con los que quiere operar y luego ingrese que operacion necesita ( + o - ) ")
n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
operacion = input("ingrese la operacion (+ o -): ")
if (operacion=="+"):
    print("la suma de los dos numeros es: ",n1+n2)
else:
    print("la resta de los dos numeros es: ",n1-n2)

