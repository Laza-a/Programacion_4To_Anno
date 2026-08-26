from Estudiante import Estudiante
from Admin import Administrador

Usuarios = []

print("Bienvenido al sistema de login")

while True:
    print("Seleccione una opción:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":

        tipo_usuario = input(
            "Ingrese el tipo de usuario (1-Estudiante/2-Administrador): "
        )
        check=False
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        while check == False:
            correo = input("Ingrese el correo: ")
            if "@" in correo:
                check=True
            else:
                check=False
                print("Su correo es incorrecto (no contiene arroba @)")

        contrasena = input("Ingrese la contraseña: ")

        if tipo_usuario == "1":

            matricula = input("Ingrese la matrícula: ")

            estudiante = Estudiante(
                nombre,
                apellido,
                correo,
                contrasena,
                matricula
            )

            Usuarios.append(estudiante)
            print("Estudiante registrado correctamente.")

        elif tipo_usuario == "2":

            administrador = Administrador(
                nombre,
                apellido,
                correo,
                contrasena
            )

            Usuarios.append(administrador)
            print("Administrador registrado correctamente.")

        else:
            print("Tipo de usuario no válido.")

    elif opcion == "2":

        correo = input("Ingrese el correo: ")
        contrasena = input("Ingrese la contraseña: ")

        usuario_encontrado = None

        for usuario in Usuarios:
            if usuario.correo == correo:
                if usuario.verificar_contrasena(contrasena):
                    usuario_encontrado = usuario
                    break

        if usuario_encontrado:

            print("Bienvenido", usuario_encontrado.nombre ,usuario_encontrado.apellido)
            print("Correo: ",usuario_encontrado.correo)
            print("Rol: ",{usuario_encontrado.rol})

            if isinstance(usuario_encontrado, Estudiante):
                print("Matrícula: ",{usuario_encontrado.matricula})

        else:
            print("Correo o contraseña incorrectos.")

    elif opcion == "3":
        print("Saliendo del sistema. (Fin)")
        break

    else:
        print("Opción no válida. Intente nuevamente.")





