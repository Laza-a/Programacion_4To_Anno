from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, correo, contrasena, matricula):
        super().__init__(nombre, apellido, correo, contrasena)
        self.matricula = matricula
        self.rol = "Estudiante"