# 6 Buscar una palabra completa en un texto y contar cuántas veces está.
texto="Quiero comer manzanas, solamente manzanas."
palabraInp=input("Ingrese una palabra: ").lower()
palabras=""
contador=0
for letra in texto:
    if letra in ".,":
        palabras+=""
    else:
        palabras+=letra
palabras=palabras.lower().split(" ")
for palabra in palabras:
    if palabra == palabraInp:
        contador+=1
print(contador)
