# 8-Ingresar autos y sus precios y contar cuantos valen entre $17.460.000 
# y $23.850.000. Terminar la carga cuando el valor ingresado sea 0.

valor=1
cantidad=0
while (valor!="0"):
    valor=float(input("ingrese el valor del auto: "))
    if (valor>=17_460_000 and valor<=23_850_000):
        cantidad=cantidad+1
print("la cantidad de autos que valen entre $17.460.000 y $23.850.000 es: ",cantidad)
