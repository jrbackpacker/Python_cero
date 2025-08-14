## Funciones ##

def saludar(nombre):
    print("Hola, " + nombre)

saludar("Juan")
saludar("Maria")

def sum_two_numbers(a, b):
    return a + b

result = sum_two_numbers(5, 10)
print("La suma es: " + str(result))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("El factorial de 5 es: " + str(factorial(5)))

