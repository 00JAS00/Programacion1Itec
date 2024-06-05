# 10 Determinar cuál es la vocal que aparece con mayor frecuencia.
texto="Quiero comer manzanas, solamente manzanas."
vocales="aeiou"
frecuenciaVocales={'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for vocal in texto:
    if vocal in vocales:
        frecuenciaVocales[vocal]+=1

vocalMasFrecuente=""
cantFrecuenciaMax=0
for vocal in vocales:
    if frecuenciaVocales[vocal]>cantFrecuenciaMax:
        vocalMasFrecuente=vocal
        cantFrecuenciaMax=frecuenciaVocales[vocal]

print(f"La vocal que mas se repite es la {vocalMasFrecuente} una cantidad de {cantFrecuenciaMax}")