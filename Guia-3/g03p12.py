# 12- Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una.

personas = []
total_mujeres = 0

while True:
    nombre = input("Ingrese el nombre de la persona (o 'fin' para terminar): ")
    if nombre == 'fin':
        break
    
    sexo = input("Ingrese el sexo de la persona (M/F): ")
    
    if sexo in "Ff":
        total_mujeres += 1
        personas.append((nombre, sexo))

# Mostrar el total de mujeres y sus nombres
print("Total de mujeres:", total_mujeres)
print("Nombres de las mujeres:")
for persona in personas:
    if persona[1] in "Ff":
        print(persona[0])