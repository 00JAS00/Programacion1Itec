# 8- Cargar una lista con números. Invertir los elementos sin usar otra lista. 

numeros=[1,2,3,4,5,6,7,8,9,10]
longitud=len(numeros)
for i in range(longitud//2):
     # Intercambiar los elementos simétricos en la lista
    indice_opuesto = longitud - i - 1
    temp = numeros[i]
    numeros[i] = numeros[indice_opuesto]
    numeros[indice_opuesto] = temp
print("Lista revertida: ",numeros)