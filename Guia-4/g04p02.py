# 2 Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.
Letras="Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido."
contador=0
for letra in Letras:
    print(letra)
    if letra in "aA":
        contador+=1
print(f"La cantidad de veces que aparece la letra en la oracion es: {contador}")
