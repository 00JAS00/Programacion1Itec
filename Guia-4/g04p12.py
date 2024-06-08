# 12 Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50.
oracion="Juan tiene 25 años y tiene 300 pesos"
palabras=oracion.split(" ")

for palabra in palabras:
    # mas corto seria  if palabra.isnumeric() and len(palabra) == 2
    if len(palabra) == 2 and palabra[0] in "123456789" and palabra[1] in "0123456789":
        print (int(palabra)*2)
