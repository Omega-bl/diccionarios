# Crear un índice por nombre
# Nombre normalizado → lista de códigos.

from base import productos, normalizar, mostrar

indice = {}
for codigo, datos in productos.items():
    nombre = normalizar(datos["nombre"])
    indice.setdefault(nombre, []).append(codigo)

busqueda = normalizar("  BOLÍGRAFO AZUL  ")
codigos = indice.get(busqueda, [])
if not codigos:
    print("Nombre no encontrado")
for codigo in codigos:
    mostrar(codigo)
