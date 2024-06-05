# 8 Contar la cantidad de letras (no incluir los separadores).
oracion="Quiero comer manzanas, solamente manzanas."
contador = 0
for letra in oracion:
    if letra not in ' ,.':
        contador += 1
print('La cantidad de letras es', contador)