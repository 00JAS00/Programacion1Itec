# 4 Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII de referencia (googlear la tabla y las funciones de conversión en Python).
palabra=input("Ingrese una palabra: ")
palabraMayus=""
# >=97
for letra in palabra:
    if 97 <= ord(letra) <= 122:
        palabraMayus+=chr(ord(letra)-32)
    else:
        palabraMayus+=letra
print(palabraMayus)