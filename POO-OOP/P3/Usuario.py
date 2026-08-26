class Usuario:
    def __init__(self, nombre, apellido, correo, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.__contrasena = contrasena  

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena