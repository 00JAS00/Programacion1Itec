# 3. Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes). El resultado es el total general.
def esLetra(caracter):
    codigo=ord(caracter)
    return (
        (97 <= codigo <= 122) or  # a-z
        (65 <= codigo <= 90) or   # A-Z
        caracter in "áéíóúÁÉÍÓÚñÑ" #Á-Ú,á-ú y ñ-Ñ
    )
def contarLetras(cadena):
    contador=0
    for caracter in cadena:
        if esLetra(caracter):
            contador+=1
    print(f"La cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes)  es: {contador}\nDe el texto {cadena}")

contarLetras("Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes). El resultado es el total general.")