import Usuario
class Estudiante(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña, matricula):
        super().__init__(nombre, apellido, correo, contraseña)
        self.matricula = matricula

    #def mostrar_datos(self):
    #    return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}, Matrícula: {self.matricula}, Rol: {self.rol}"