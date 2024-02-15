#Ejercicio 7: Añadir Ítems a un Inventario

#Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.

def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    inventario.append(item)
    return inventario

# Ejemplo de uso
inventario = ["ordenador", "cargador", "movil"]
try:
    agregar_item(inventario, "reloj")
    print(inventario)
    agregar_item(inventario, "cargador")
except ValueError as e:
    print(e)