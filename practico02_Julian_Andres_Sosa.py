personas = [
    "Josefa Taponales,France(Europe),30-10-2007",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

# 1 Los apellidos de las personas nacidas antes de un año solicitado al usuario.
anioInput=int(input("Ingrese un año: "))
print(f"Los apellidos de las personas nacidas antes de {anioInput} son: ")
for persona in personas:
    anioPersona=int(persona[-4:])
    if anioPersona < anioInput:
        apellido=persona[persona.find(" "):persona.find(",")]
        print(apellido)


# 2 La cantidad de personas nacidas en un país ingresado por el usuario.
paisInput=input("Ingrese un pais de nacimiento: ")
contador=0
for persona in personas:
    if paisInput in persona:
        contador+=1
print(f"La cantidad de personas nacidas en {paisInput} son: {contador}")


# 3 El nombre de pila de la persona más joven de Europe.
nombreMasJoven=""
fechaMasJoven=0
for persona in personas:
    if "Europe" in persona:
        fechaNac=int(persona[-4:]+persona[-7:-5]+persona[-10:-8])
        if fechaNac>=fechaMasJoven:
            fechaMasJoven=fechaNac
            nombreMasJoven=persona[:persona.find(" ")]
print(f"La persona más joven de Europe es {nombreMasJoven}")