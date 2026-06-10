#Crear una carpeta de trabajo, llamada "POO"
#Dentro de esa carpeta crear dos archivos .py uno llamado carrera.py y otro Personaje_clase.py
#En el archivo Personaje_clase.py desarrollar la clase Personaje  con #atributo de clase "estado = True" #vivo. Y el constructor y los atributos (nombre, altura, velocidad, resistencia, fuerza) y dos metodos, correr y recuperarse.
#Luego en el archivo carrera.py crear un menu: "ingresar participantes"pedirle los datos al usuario para instanciar objetos e imprimirlos por pantalla, "correr carrera" "pedir distancia" y realizar la carrera, "salir"

from personaje import Personaje


personajes=[]
while True:
    opcion=int(input("""                          1-ingresar personaje
                         2-correr carrera
                         3-mostrar datos
                         4-salir"""))
    if opcion == 1:
        nombre = str(input("¿Cual es el nombre de tu personaje?"))
        altura = float(input("¿Cual es la altura de tu personaje en metros?"))
        velocidad = int(input("¿Cual es la velocidad de tu personaje? del 1 - 100"))
        resistencia =int(input("¿Cual es la resistencia de tu personaje? del 1 - 100"))
        fuerza =int(input("¿Cual es la fuerza de tu personaje? del 1 - 100"))
        personaje = Personaje(True,velocidad,fuerza,resistencia,altura,nombre)
        print("Personaje" ,personaje.nombre,"creado" )
        personajes.append(personaje)
    elif opcion == 2:
        print("Los participantes comenzaron a correr")
        for personaje in personajes:
            tiempo= personaje.correr()
            print("los participantes corrieron durante",tiempo,"segundos")
    elif opcion == 3:
        for personaje in personajes:
            personaje.mostrar_datos()
    else:
        break