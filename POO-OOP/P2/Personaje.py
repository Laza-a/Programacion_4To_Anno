import random
class Personaje:
    def __init__(self,nombre,vida,resistencia,fuerza,):
        self.estado= True
        self.nombre= nombre
        self.vida= vida
        self.resistencia= resistencia
        self.fuerza= fuerza
        self.resistencia_inicial = resistencia


    
    def atacar(self, Otro_Personaje):
        if self.estado:
            ataque = random.randint(0, self.fuerza)
            print(self.nombre, "atacó con una fuerza de", ataque, "a", Otro_Personaje.nombre)

            Danno = ataque - Otro_Personaje.resistencia

            if Danno < 0:
              Danno = 0

            Otro_Personaje.vida -= Danno

            print(Otro_Personaje.nombre, "recibió", Danno, "de daño.")

            if Otro_Personaje.vida <= 0:
                Otro_Personaje.estado = False
                print(Otro_Personaje.nombre, "se quedó sin vida")

            return Danno, ataque

        else:
            print("Tu personaje no se encuentra en condiciones para pelear")



    def recuperarse (self):
        self.resistencia += 10
        if self.resistencia > self.resistencia_inicial:
            self.resistencia = self.resistencia_inicial
            print(self.nombre, "tu personaje recupero un poco de resistencia, ahora tiene la maxima resistencia y no aumenta mas")
        print(self.nombre, "tu personaje recupero un poco de resistencia, ahora tiene", self.resistencia, "de resistencia")

    def mostrar_datos(self):
        print(f"""
                Nombre: {self.nombre} 
                Vida: {self.vida}
                Resistencia: {self.resistencia}
                Fuerza: {self.fuerza}""")
