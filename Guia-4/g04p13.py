# 13 Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).
nombreCompleto=input("ingreso de un nombre completo en la forma 'nombre apellido': ")
nombreSeparado=nombreCompleto.split(" ")
nombreSeparado.reverse()
nombreSeparado= ", ".join(nombreSeparado)
print(nombreSeparado)