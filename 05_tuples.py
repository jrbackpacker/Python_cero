## Tuplas ##

# Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
# Esto las hace más seguras y eficientes en términos de rendimiento en comparación con las listas.
# Además, las tuplas pueden ser utilizadas como claves en diccionarios, mientras que las listas no pueden.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print(type(my_tuple))  # Tipo de dato de la tupla

print(my_tuple[1] + 2)  # Acceso a un elemento de la tupla (el cero es la primera posición )

# funciones

print(my_tuple.count(2))  # Cuenta cuántas veces aparece el 2 en la tupla
print(my_tuple.index(3))  # Índice del elemento 3 en la tupla
print(my_tuple + my_other_tuple)  # Concatenación de tuplas
print(my_tuple * 2)  # Multiplicación de tuplas
print(my_tuple[0:3])  # Slice de la tupla (desde el 0 al 3 sin incluir el 3)
print(my_tuple[::-1])  # Inversión de la tupla
print(my_tuple[-1])  # Último elemento de la tupla
print(my_tuple[-2])  # Penúltimo elemento de la tupla
print(my_tuple[-3])  # Antepenúltimo elemento de la tupla


