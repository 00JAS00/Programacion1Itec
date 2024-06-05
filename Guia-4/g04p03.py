# 3 Eliminar el plural en esta frase: “Real Madrid gana las copas.” Recorrer y quitar las eses, construyendo una nueva string.
letras="Real Madrid gana las copas"
singular=""
for letra in letras:
    if letra not in "Ss":
        singular+=letra
print(singular)