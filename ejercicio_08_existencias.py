# Consultar productos agotados
# Disponibilidad booleana → lista de códigos.

from base import productos, mostrar

indice = {True: [], False: []}
for codigo, datos in productos.items():
    disponible = datos["stock"] > 0
    indice[disponible].append(codigo)

print("PRODUCTOS AGOTADOS")
for codigo in indice[False]:
    mostrar(codigo)
