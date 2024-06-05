# 11 Averiguar qué cantidad de letras tiene la palabra más larga y cual es.
texto="Quiero comer manzanas, solamente manzanas."
oracionLimpia=""
for caracter in texto:
    if caracter in ".,":
        oracionLimpia+=""
    else:
        oracionLimpia+=caracter
palabras=oracionLimpia.split(" ")
palabraMasLarga=["",0]
for palabra in palabras:
    if len(palabra) > palabraMasLarga[1]:
        palabraMasLarga=[palabra,len(palabra)]
print(f"La palabra mas larga es '{palabraMasLarga[0]}' y con una cantidad de letras de {palabraMasLarga[1]}")