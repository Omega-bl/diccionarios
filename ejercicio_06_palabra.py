# Crear un índice por palabras
# Palabra del nombre → lista de códigos.

from base import productos, normalizar, mostrar

indice = {}
for codigo, datos in productos.items():
    palabras = normalizar(datos["nombre"]).split()
    # Evita repetir un código si una palabra aparece varias veces.
    for palabra in dict.fromkeys(palabras):
        indice.setdefault(palabra, []).append(codigo)

palabra = normalizar("lápiz")
codigos = indice.get(palabra, [])
if not codigos:
    print("Palabra no encontrada")
for codigo in codigos:
    mostrar(codigo)
