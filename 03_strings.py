# Strings

my_string = "Hola Jesús"

my_other_string = "Hola Mundo"

print(my_string + " " + my_other_string)

#salto de línea

my_new_line_string = "Este es un String\ncon salto de línea"

print(my_new_line_string)

#con tabulacion

my_tab_string = "Este es un String\tcon tabulación"

print(my_tab_string)

#tabulación mas salto de línea

my_tab_new_line_string = "Este es un String\tcon tabulación\ncon salto de línea"

print(my_tab_new_line_string)   

# Formatear 

name, surname, age = "Jesus", "Romero", 30

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
# Podemos desempaquetar un string en variables individuales
language = "Python"

a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

lenguaje_slice = language[0:3]

print(lenguaje_slice)

#Reverse

lenguaje_reverse = language[::-1]

print(lenguaje_reverse)

# Funciones

print(len(language))  # Longitud del string
print(language.upper())  # Convertir a mayúsculas
print(language.lower())  # Convertir a minúsculas
print(language.replace("o", "0"))  # Reemplazar caracteres
print(language.startswith("Py"))  # Comprobar si empieza con "Py"   
print(language.endswith("on"))  # Comprobar si termina con "on"
print(language.find("th"))  # Buscar subcadena
print(language.count("o"))  # Contar ocurrencias de "o"
print(language.isalpha())  # Comprobar si es alfabético
print(language.isnumeric())  # Comprobar si es numérico     
print(language.isalnum())  # Comprobar si es alfanumérico   
print(language.isupper())  # Comprobar si está en mayúsculas
print(language.islower())  # Comprobar si está en minúsculas
print(language.capitalize())  # Capitalizar el primer carácter
print(language.title())  # Capitalizar el título (primer carácter de cada palabra)
print(language.strip())  # Eliminar espacios al inicio y al final
print(language.split("t"))  # Dividir el string por "t"
print(language.join(["A", "B", "C"]))  # Unir una lista depr
print(language)


