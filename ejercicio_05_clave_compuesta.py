# Buscar con una clave compuesta
# Tupla de categoría y proveedor → lista de códigos.

from base import productos, normalizar, mostrar

indice = {}
for codigo, datos in productos.items():
    clave = (normalizar(datos["categoria"]),
             normalizar(datos["proveedor"]))
    indice.setdefault(clave, []).append(codigo)

clave = (normalizar("Arte"), normalizar("Sur"))
codigos = indice.get(clave, [])
if not codigos:
    print("No hay productos para esa combinación")
for codigo in codigos:
    mostrar(codigo)
