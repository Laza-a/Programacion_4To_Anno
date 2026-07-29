from Personaje import Personaje
try:
    personaje = Personaje(
        input("Ingrese el nombre de su personaje: "),
        int(input("Ingrese la vida de su personaje: ")),
        int(input("Ingrese la resistencia de su personaje: ")),
        int(input("Ingrese la fuerza de su personaje: "))
        )
except ValueError:
    print("Error: ingresaste un valor inválido. Intenta de nuevo.")
total=personaje.vida + personaje.resistencia + personaje.fuerza
if total > 100:
    print("El total de vida, resistencia y fuerza no puede superar los 100 puntos. Por favor, reinicie el juego y vuelva a ingresar los valores.")
    exit()
Otro_Personaje = Personaje(
    input("Ingrese el nombre de su personaje: "),
    int(input("Ingrese la vida de su personaje: ")),
    int(input("Ingrese la resistencia de su personaje: ")),
    int(input("Ingrese la fuerza de su personaje: "))
    )
total=Otro_Personaje.vida + Otro_Personaje.resistencia + Otro_Personaje.fuerza
if total > 100:
    print("El total de vida, resistencia y fuerza no puede superar los 100 puntos. Por favor, reinicie el juego y vuelva a ingresar los valores.")
    exit()

while True:
    personaje.mostrar_datos()
    desicion = int(input("Que desea hacer? (1:atacar-2:recuperarse): "))
    try:
        if desicion == 1:
            personaje.atacar(Otro_Personaje)
        if desicion == 2:
            personaje.recuperarse()
        Otro_Personaje.atacar(personaje)
    except ValueError:
        print("Error: ingresaste un valor inválido. Intenta de nuevo.")
    except IndexError:
        print("Error: ingresaste un valor inválido. Intenta de nuevo.")
            
    if Otro_Personaje.estado == False:
        print("Felicidades, ganaste la pelea")
        break
    if personaje.estado == False:
        print("Perdiste la pelea, wuashin")
        break
   