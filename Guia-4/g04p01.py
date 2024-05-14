# 1 Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python". Cortar la cadena original, agregarle el literal "Programación en" y concatenar.
oracion="Curso de Python"
palabra1,palabra2=oracion.split("de")
oracion=palabra1+"de Programación en"+palabra2
print (oracion)
