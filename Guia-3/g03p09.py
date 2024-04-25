# 9- Cargar en dos listas paralelas nombres y sueldos. Luego mostrar los nombres de las personas que ganan más de $1_850_000.

nombres=[]
sueldos=[]
nombresSueldosMayores=[]
for i in range(5):
    nombres.append(input("INGRESE UN NOMBRE: "))
    sueldos.append(int(input("INGRESE UN SUELDO: ")))
for i in range(len(sueldos)):
    if sueldos[i] > 1_850_000:
        nombresSueldosMayores.append(nombres[i])
        
print("LAS PERSONAS CON EL SUELDO MAYOR A 1_850_000 SON: ",nombresSueldosMayores)

    