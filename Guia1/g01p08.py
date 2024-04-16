# Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.

entrada=int(input("ingrese un periodo en segundos: "))

segundosXdia=24*60*60
segundosXhora=60*60
segundosXminuto=60
resto=entrada

# dias
dias=entrada//segundosXdia
resto-=dias*segundosXdia

# horas
horas=resto//segundosXhora
resto-=horas*segundosXhora

# minutos
minutos=resto//segundosXminuto

# segundos
resto-=minutos*segundosXminuto

print("dias: ",dias," horas: ",horas," minutos: ",minutos," segundos: ",resto)