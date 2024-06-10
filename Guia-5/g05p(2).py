# 2.  Buscar una palabra y reemplazarla por otra todas las veces que aparezca. Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'
def reemplazo():
    texto="Quiero comer manzanas, solamente manzanas.".lower()
    print(f"texto de referencia:\n {texto}")
    palabraBuscar=input("Ingrese la palabra a buscar:").lower()
    palabraRemplazo=input("Ingrese la palabra de remplazo:").lower()
    texto=texto.split(palabraBuscar)
    texto=palabraRemplazo.join(texto)
    print(texto)
reemplazo()