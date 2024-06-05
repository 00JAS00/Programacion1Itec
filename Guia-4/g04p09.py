# 9 Contar la cantidad de palabras.
oracion="Quiero comer manzanas, solamente manzanas."
contarPalabras=""
# Me gustaria de esta forma pero no esta buena
# contarPalabras=len(oracion.split(" "))
# la correcto seria esto
for caracter in oracion:
    if caracter in ",.[{]}?¿!¡)(":
        contarPalabras+=""
    else:
        contarPalabras+=caracter
contarPalabras=len(contarPalabras.split(" "))

print(contarPalabras)