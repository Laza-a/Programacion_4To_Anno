class Usuario:
    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena  # Contraseña encapsulada

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena