### LISTAS ###
Lista=[11,"hola",0.2]
print(Lista[1])
Lista.append("el append agrega un valor al final de la variable")
print(Lista)
Lista.insert(2,"el insert agrega un valor a la posicion indicada")
print(Lista)
## El pop elimina el valor de la ultima pocicion de la lista o arreglo
Lista.pop()
print(Lista)
#hace lo mismo pero guarda el valor borrado en la variable dato
dato=Lista.pop(1)
#Borra cualquier valor de la lista que sean iguales a "hola"
Lista.remove("hola")
print(Lista)

#Recorrido a la lista
for i in range(len(Lista)):
    #el end en el print sirve para decir lo que uno quiera cuando termine de printear 
    print(Lista[i], end='---')

#recorrido por elemento
for elemento in Lista:
    print(elemento)
    
#Listas paralelas
nombres=["julian","alice","jack"]
edades=[11,22,33]
### listos ###r