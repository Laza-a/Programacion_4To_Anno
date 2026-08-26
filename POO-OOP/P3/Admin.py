from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, apellido, correo, contrasena):
        super().__init__(nombre, apellido, correo, contrasena)
        self.rol = "Administrador"