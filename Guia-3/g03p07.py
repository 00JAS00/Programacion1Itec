# 7- Eliminar todos los valores iguales de una lista. Previamente, solicitar el valor y si no está, mostrar un cartel diciendo que no lo ha encontrado.

valores=["a","b","c","d","e","f",1,2,3,4,5,  6,"a","b",1, 2]
valoresUnicos=[]
findValor=input("Ingrese el valor a buscar: ")

if findValor in valores:
    for valor in valores:
        # Contador para saber si en la lista original solo hay un solo dato con el mismo valor
        contador=0
        for elemento in valores:
            if elemento==valor:
                contador+=1
        # si hay un solo valor en la lista original agrega a la lista de valores unicos
        if contador==1:
            valoresUnicos.append(valor)
    print("VALORES SIN REPETIR: ", valoresUnicos)
elif findValor not in valores:
    print("No se encontro el valor Ingresado")
                
                    

