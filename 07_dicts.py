### diccionarios ###

# Los diccionarios son colecciones desordenadas de pares clave-valor. Permiten almacenar y acceder a datos de manera eficiente.
# Las claves deben ser únicas e inmutables, mientras que los valores pueden ser de cualquier tipo.

my_dict = dict()
my_other_dict = {}

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(my_dict)

print(type(my_dict))  # Tipo de dato del diccionario

# Acceso a elementos

print(my_dict["nombre"])  # Acceso al valor asociado a la clave "nombre"
print(my_dict.get("edad"))  # Acceso al valor asociado a la clave "edad" (método get)

# Modificación de elementos

my_dict["edad"] = 31  # Modificación del valor asociado a la clave "edad"
print(my_dict)

# Eliminación de elementos

del my_dict["ciudad"]  # Eliminación del par clave-valor asociado a la clave "ciudad"
print(my_dict)

# Funciones

print(my_dict.keys())  # Devuelve una vista de las claves del diccionario
print(my_dict.values())  # Devuelve una vista de los valores del diccionario
print(my_dict.items())  # Devuelve una vista de los pares clave-valor del diccionario   
