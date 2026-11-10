# Buscar productos por categoría
# Categoría → lista de códigos.

from base import productos, normalizar, mostrar

indice = {}
for codigo, datos in productos.items():
    categoria = normalizar(datos["categoria"])
    indice.setdefault(categoria, []).append(codigo)

categoria = normalizar("Cuadernos")
codigos = indice.get(categoria, [])
if not codigos:
    print("Categoría no encontrada")
for codigo in codigos:
    mostrar(codigo)
