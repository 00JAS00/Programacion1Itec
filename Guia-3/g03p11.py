# 11- Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.

nombres = ["Juan", "María", "Pedro", "Ana"]
fechasNacimiento = ["2000-05-15", "1998-10-20", "2005-03-10", "1985-12-31"]

# Fecha actual
añoActual = 2024
mesActual = 4
diaActual = 30


for i in range(len(nombres)):
    # Extraer el año, mes y día de la fecha de nacimiento
    fechaNacimiento = fechasNacimiento[i].split("-")
    anioNacimiento = int(fechaNacimiento[0])
    mesNacimiento = int(fechaNacimiento[1])
    diaNacimiento = int(fechaNacimiento[2])
    
    edad = añoActual - anioNacimiento

    if (mesActual, diaActual) < (mesNacimiento, diaNacimiento):
        edad -= 1
    if edad >= 18:
        print(nombres[i])