## Variables ##


my_variable_str = "Hola Jesus Romero!"
print(my_variable_str)

my_variable_int = 5
print(my_variable_int)

my_variable_float = 3.14
print(my_variable_float)

my_variable_bool = True
print(my_variable_bool)

my_variable_complex = 3 + 5j
print(my_variable_complex)

print (my_variable_str, my_variable_bool, my_variable_int, my_variable_float, my_variable_complex)

#haremos un cambio de tipo de int a str
my_variable_int = str(my_variable_int)
print(my_variable_int)
print(type(my_variable_str))

#variables en una linea 

name, surname, age = "Jesus", "Romero", 30
print(name, surname, age)
print(type(name), type(surname), type(age))
print("Mi nombre es", name, surname, "y tengo", age, "años.")

#ojo con esta! cambiamos el valor de las variables, 
# al trabajar varias personas esto puede ser un problema

name, surname, age = "Maria", "Gomez", 25
print(name, surname, age)
print(type(name), type(surname), type(age))
print("Mi nombre es", name, surname, "y tengo", age, "años.")

