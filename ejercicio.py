class Persona:

    def __init__(self, nombre, apellidos, edad):
        self.nombres = nombre
        self.apellidos = apellidos
        self.edad = edad

    # Metodo para mostrar la informacion de la persona 
    def mostrarPersona(self):
        print("Nombre: ", self.nombres)
        print("Apellidos: ", self.apellidos)
        print("Edad: ", self.edad)
"""
def main():
    print("vamos a aprender POO...")
    persona_1 = Persona ("Daniel", "Hernández", 15)
    persona_1.mostrarPersona()

if __name__ == main():
    main()
"""
