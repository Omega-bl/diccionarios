# Localizar productos de un proveedor
# Proveedor → lista de códigos.

from base import productos, normalizar, mostrar

indice = {}
for codigo, datos in productos.items():
    proveedor = normalizar(datos["proveedor"])
    indice.setdefault(proveedor, []).append(codigo)

proveedor = normalizar("Sur")
codigos = indice.get(proveedor, [])
if not codigos:
    print("Proveedor no encontrado")
for codigo in codigos:
    mostrar(codigo)
