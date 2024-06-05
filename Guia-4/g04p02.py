# 2 Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.
Letras="Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido."
letraInput=input("Ingrese la letra que quiera saber que se repita").lower()
contador=0
for letra in Letras:
    print(letra)
    if letra.lower() == letraInput:
        contador+=1
print(f"La cantidad de veces que aparece la letra {letraInput} en la oracion es: {contador}")
