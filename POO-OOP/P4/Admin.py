import Usuario 
class Administrador(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, correo, contraseña)
    

    #def mostrar_datos(self):
     #   return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}, contraseña: {self.__contraseña}, Rol: {self.rol}"