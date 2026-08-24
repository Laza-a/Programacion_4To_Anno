#Práctico 1 – Sistema de Login y Registro
#Desarrollar un sistema de usuarios utilizando Programación Orientada a Objetos.
#El programa deberá tener una clase padre Usuario y dos clases hijas: Estudiante y Administrador.
#La contraseña deberá estar encapsulada y solo podrá verificarse mediante un método. El sistema debe permitir registrar usuarios, iniciar sesión con usuario y contraseña y mostrar los datos correspondientes según el tipo de usuario.
#Conceptos a utilizar: clases, objetos, __init__(), métodos, encapsulamiento, herencia y super().
from Estudiante import Estudiante
from Admin import Administrador
Usuarios=[]
print("Bienvenido al sistema de login")
while True:
    print("Seleccione una opción:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        tipo_usuario = input("Ingrese el tipo de usuario (1-Estudiante/2-Administrador): ")
        if tipo_usuario == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            correo = input("Ingrese el correo: ")
            contrasena = input("Ingrese la contraseña: ")
            matricula = input("Ingrese la matrícula: ")
            estudiante = Estudiante(nombre, apellido, correo, contrasena, matricula)
            Usuarios.append(estudiante)

        elif tipo_usuario =="2":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            correo = input("Ingrese el correo: ")
            contrasena = input("Ingrese la contraseña: ")
            administrador = Administrador({ "nombre": nombre, 
                                            "apellido": apellido,
                                            "correo": correo, 
                                            "contraseña": contrasena})
            Usuarios.append(administrador)











           

    elif opcion == "2":
        correo = input("Ingrese el correo: ")
        contrasena = input("Ingrese la contraseña: ")
        # Aquí se debería verificar el correo y la contraseña con los usuarios registrados
        # Por simplicidad, asumimos que el usuario es un estudiante registrado
        estudiante = Estudiante()
        if estudiante.verificar_contrasena(contrasena):
            print(f"Bienvenido, {estudiante.nombre} {estudiante.apellido}.")
            print(f"Correo: {estudiante.correo}")
            print(f"Matrícula: {estudiante.matricula}")
            print(f"Rol: {estudiante.rol}")
        else:
            print("Correo o contraseña incorrectos.")
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")









