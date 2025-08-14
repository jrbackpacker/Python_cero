### sets ###

# Los sets son colecciones desordenadas de elementos únicos. No permiten duplicados y no mantienen un orden específico.
# Son útiles cuando se necesita garantizar la unicidad de los elementos y se desea realizar operaciones de conjunto.

my_set = set()
my_other_set = {}

my_set = {1, 2, 3, 4, 5}
print(my_set)

print(type(my_set))  # Tipo de dato del set

# Operaciones

print(len(my_set))  # Número de elementos en el set
print(2 in my_set)  # Verifica si el 2 está en el set
print(my_set.union(my_other_set))  # Unión de sets
print(my_set.intersection(my_other_set))  # Intersección de sets
print(my_set.difference(my_other_set))  # Diferencia de sets
print(my_set.symmetric_difference(my_other_set))  # Diferencia simétrica de sets
print(my_set.issubset(my_other_set))  # Verifica si un set es subconjunto de otro
print(my_set.issuperset(my_other_set))  # Verifica si un set es superconjunto de otro
print(my_set.pop())  # Elimina y devuelve un elemento aleatorio del set
print(my_set.clear())  # Elimina todos los elementos del set

# Añadir y eliminar elementos


my_set.add(6)  # Añadir un elemento al set
my_set.remove(2)  # Eliminar un elemento del set
print(my_set)       

