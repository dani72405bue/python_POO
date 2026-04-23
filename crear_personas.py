from ejercicio import Persona

juan = Persona("juan", "castellanos", 15)
juan.mostrarPersona()

NameError
Nicol = Persona("Nicol", "Quintero", 15)
Nicol.mostrarPersona()

Nicol.apellidos = "Bueno"
Nicol.mostrarPersona()

juan = Nicol

juan.mostrarPersona()