datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/04/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]
inicialesYapellidos=[]


# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

print("Iniciales y apellido de las personas: ")
for persona in datos:
    apellido, nombre =persona[0].split(", ")
    nuevoNombre=nombre[0]+". "+apellido
    print(nuevoNombre)
    

# 2) Decir cuál es el nombre de pila más largo.

nombreMasLargo= ""
for persona in datos:
    indiceNombre=persona[0].find(",")
    nombre=persona[0][indiceNombre+2:]
    
    if len(nombre)>len(nombreMasLargo):
        nombreMasLargo=nombre
print("El nombre mas largo es:",nombreMasLargo)

# 3) Mostrar el promedio de edad de las mujeres.

diaHoy,mesHoy,aniHoy=6,5,2024
edadTotal=0
totalMujeres=0

for persona in datos:
    
    if persona[1] == "f":
        totalMujeres+=1
        diaNac,mesNac,aniNac= persona[2].split("/")
        diaNac,mesNac,aniNac= int(diaNac),int(mesNac),int(aniNac)
        edad= aniHoy - aniNac
        if mesNac>=mesHoy and diaNac>diaHoy:
            edad-=1
        edadTotal+= edad
promedio=round(edadTotal/totalMujeres)
print("El promedio de edad de las mujeres es: ",promedio)
