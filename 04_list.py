## Listas ##

my_list = list()

my_other_list = []

print(len(my_list))  # Longitud de la lista

my_list = [1, 2, 3, 4, 5]

print(my_list)
print(len(my_list))  # Longitud de la lista

my_other_list = [6, 7, 8, 9, 10]

print(my_other_list)
print(len(my_other_list))  # Longitud de la lista
print(type(my_other_list))  # Tipo de dato de la lista

print(my_list[1] + my_other_list[1])  # Concatenación de listas añadimos 
#posicion en la lista ( el cero es la primera posicion)

#Funciones 

print(my_list[0:3])  # Slice de la lista (desde el 0 al 3 sin incluir el 3)
print(my_list.count(1)) # Cuenta cuántas veces aparece el 1 en la lista
print(my_list.index(3))  # Índice del elemento 3 en la lista
print(my_list + my_other_list)  # Concatenación de listas   
print(my_list * 2)  # Multiplicación de listas
print(my_list[0:5:2])  # Slice de la lista con paso de 2 (desde el 0 al 5 con paso de 2)
print(my_list[::-1])  # Inversión de la lista
print(my_list[-1])  # Último elemento de la lista
print(my_list[-2])  # Penúltimo elemento de la lista
print(my_list[-3])  # Antepenúltimo elemento de la lista
print(my_list.append(6))  # Añade el elemento 6 al final de la lista
print(my_list)  # Muestra la lista actualizada

#ordenar
my_list.sort()
print(my_list)  # Muestra la lista ordenada


#ordenar de mayor a menor

my_list.sort(reverse=True)
print(my_list) 



