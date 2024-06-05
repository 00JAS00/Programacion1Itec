# 5 Recibir por teclado una cadena de números, dejarlo en formato string e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  “1234567890” debería devolver “1.234.567.890”
# 10
# 100
# 1.000
# 12.000
# 123.000
# 1.000.000
# 12.000.000
# 123.000.000
# 1.000.000.000
numero=str(input("Ingrese un numero: "))
resultado=""
longitud=len(numero)
contador=0
for i in range(len(numero)-1,-1,-1):
    contador+=1
    longitud-=1
    resultado=numero[i]+resultado
    if contador==3 and longitud>0:
        resultado="."+resultado
        contador=0

print(resultado)
