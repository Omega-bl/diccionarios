# Buscar un producto por código
# El catálogo base ya está indexado por código.

from base import mostrar

# La búsqueda se hace por la clave del diccionario.
codigo = "P003"
mostrar(codigo)

# También se maneja un código que no existe.
mostrar("P999")
