## Clases ##

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es " + self.nombre)

persona1 = Persona("Juan", 30)
persona1.saludar()

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def presentar(self):
        print("Hola, soy " + self.nombre + " y trabajo como " + self.puesto)

empleado1 = Empleado("Ana", 28, "Desarrolladora")
empleado1.saludar()
empleado1.presentar()