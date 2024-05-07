# lista_saludo = ['h', 'o', 'l', 'a']
# for i in range(len(lista_saludo)):
#     print(lista_saludo[i])

# string_saludo = 'hola' # una string se comporta como una lista de caracteres
# for i in range(len(string_saludo)):
#     print(string_saludo[i])


# # concatenar
# nombre = 'Ana'
# edad = 76
# frase = nombre + ' Torres tiene ' + str(edad) + ' años'
# print(frase)

# for letra in nombre:
#     print(letra)

# print('La inicial del nombre', nombre, 'es', nombre[0])


# # método find: búsqueda de una subcadena dentro de una cadena
# cadena = 'La mesa está llena de platos'

posicionMesa = cadena.find('mesa') # encuentra la posición donde comienza la palabra buscada en la frase
print(posicionMesa)

print(cadena.find('t')) # muestra la posición de la primera 't'

posiSubcadenaSinSentido = cadena.find('á l') # puedo buscar cualquier subcadena, el único requisito es que sean caracteres adyacentes
print(posiSubcadenaSinSentido)

print(cadena.find('silla')) # devuelve -1 que significa que la subcadena buscada no existe en la cadena

posiZ = cadena.find('z')
print('Posición de la letra z: ', posiZ)

chirimbolos = '1@#$(*&¨GhkjJKmk)'
print(chirimbolos.find('$(*')) # no solamente sirve para letras sino cualquier conjunto de caracteres

# slicing: obtener subcadenas
frase = 'La mesa está llena de platos'

primeraParte = frase[0:7] # recorta desde el principio hasta la posición final menos 1 (6)
print(primeraParte)
parteFinal = frase[15:] # recorta desde posición 15 hasta el final
print(parteFinal)
print(frase[13:18]) # muestra "llena", porque va desde pos 13 hasta 17 inclusive

nombres = "Juan y Lisa"
posicionY = nombres.find('y')
nombre1 = nombres[:posicionY]
nombre2 = nombres[posicionY+2:]
print(nombre1)
print(nombre2)
print(nombres.split()) # convierte en lista, sin argumento usa el espacio como separador

deportes = 'futbol---basquet---natacion---tenis'
print(deportes)
listaDeportes = deportes.split('---') # crea la lista y elimina el separador ---
print(listaDeportes)

print('$'.join(listaDeportes)) # construye una string agregando como separador en este caso el caracter $

