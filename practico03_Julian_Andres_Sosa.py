nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nacidos2018=[["19837,Liam,m","18688,Emma,f"],["18267,Noah,m","17921,Olivia,f"],["14516,Michael,m","14924,Ava,f"],["13525,James,m","14464,Isabella,f"],["13389,Oliver,m","13928,Sophia,f"]]

# Organizacion de lista nacidos 2008
listaSeparada=nacidos2008.split(",")
masculinos=[]
femeninos=[]

# variable que se utiliza en lugar de nacidos2008
nac2008New=[]

for i in range(0,len(listaSeparada),3):
    nombre=listaSeparada[i]
    numeroNacidos=listaSeparada[i+1]
    sexo=listaSeparada[i+2]
    if sexo in "mM":
        masculinos.append(",".join([numeroNacidos,nombre,sexo]))
    if sexo in "fF":
        femeninos.append(",".join([numeroNacidos,nombre,sexo]))
        
masculinos.sort(reverse=True)
femeninos.sort(reverse=True)
for i in range(min(len(masculinos),len(femeninos))):
    nac2008New.append([masculinos[i],femeninos[i]])


# La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo. Se solicita posición y sexo. (Ver salidas de ejemplo).
switch=""
while switch!="f":
    posicion=int(input("Ingrese posicion de ranking del 1 al 5: "))
    sexoInput=input("Ingrese sexo del nacido (f/m): ")
    sexoPosicion=0
    if sexoInput in "Mm":
        sexoPosicion=0
    if sexoInput in "Ff":
        sexoPosicion=1
    nacido2008=nac2008New[posicion-1][sexoPosicion]
    nacido2018=nacidos2018[posicion-1][sexoPosicion]
    numeroNacido2008,nombre2008, sexo2008= nacido2008.split(",")
    numeroNacido2018,nombre2018, sexo2018= nacido2018.split(",")
    diferenciaNacimientos=abs(int(numeroNacido2018)-int(numeroNacido2008))
    if numeroNacido2008> numeroNacido2018:
        if sexoInput in "fF":
            print(f"Mujeres en posición #{posicion}:{diferenciaNacimientos} a favor de {nombre2008}(2008) sobre {nombre2018}(2018)")
        if sexoInput in "mM":
            print(f"Varones en posición #{posicion}:{diferenciaNacimientos} a favor de {nombre2008}(2008) sobre {nombre2018}(2018)")
    if numeroNacido2008 < numeroNacido2018:
        if sexoInput in "fF":
            print(f"Mujeres en posición #{posicion}:{diferenciaNacimientos} a favor de {nombre2018}(2018) sobre {nombre2008}(2008)")
        if sexoInput in "mM":
            print(f"Varones en posición #{posicion}:{diferenciaNacimientos} a favor de {nombre2018}(2018) sobre {nombre2008}(2008)")
    switch=input("si desea terminar la consulta ingrese 'f' sino presione ENTER:")

# Los nombres de todos los bebés que comienzan con la misma letra considerando ambos periodos. Se debe solicitar la letra inicial.
letraInicialNombre=input("Ingrese letra inicial para encontrar coincidencias: ").upper()
nombresConLetra=""
nombres=[]
# ! LO PUEDO HACER TODO EN UN SOLO FOR PERO EN CASO DE QUE HAYA DISPARIDAD DE LONGITUD ENTRE LISTAS PREFIERO ASI
# nacidos 2008
for nacido in nac2008New:
    nombreM=nacido[0].split(",")[1]
    nombreF=nacido[1].split(",")[1]
    #el nombre.append es para usar con nombres repetidos
    nombres.append(nombreM)
    nombres.append(nombreF)
    if nombreF[0] in letraInicialNombre:
        nombresConLetra+=" "+nombreF
    if nombreM[0] in letraInicialNombre:
        nombresConLetra+=" "+nombreM
# nacidos 2018
for nacido in nacidos2018:
    nombreM=nacido[0].split(",")[1]
    nombreF=nacido[1].split(",")[1]
    #el nombre.append es para usar con nombres repetidos
    nombres.append(nombreM)
    nombres.append(nombreF)
    if nombreF[0] in letraInicialNombre:
        nombresConLetra+=" "+nombreF
    if nombreM[0] in letraInicialNombre:
        nombresConLetra+=" "+nombreM
print(f"Nombres con {letraInicialNombre}: {nombresConLetra}")


# Los nombres que se repiten en ambos años.
nombresRepiten=""
print(nombres)
for i in range(len(nombres)):
    for x in range(i+1,len(nombres)):
        if nombres[i]==nombres[x] and not(nombres[i] in nombresRepiten):
            nombresRepiten+=" "+nombres[i]
print(f"Nombres que se repiten: {nombresRepiten}")