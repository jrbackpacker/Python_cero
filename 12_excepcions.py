## Excepciones ##

try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
except Exception as e:
    print("Error:", e)
finally:
    print("Bloque finally ejecutado.")

# otro bloque de código

try:
    numero = int(input("Introduce un número: "))
    print("Número introducido:", numero)
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número entero.")       

    # Manejo de la excepción
    pass