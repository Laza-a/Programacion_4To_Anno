class Personaje:
    def __init__(self,estado,velocidad,fuerza,resistencia,altura,nombre):
        self.estado= True
        self.velocidad= velocidad
        self.fuerza= fuerza
        self.altura= altura
        self.resistencia= resistencia
        self.nombre= nombre
        
    def correr (self):
        if self.estado == True:
            distancia = 1000
            tiempo= distancia/self.velocidad
            return tiempo
        else:
            print("Tu personaje no se encuentra en condiciones para correr")
    def recuperarse (self):
        self.resistencia += 10
        print(self.nombre, "tu personaje recupero un poco de energia")
    def mostrar_datos(self):
        print(f"""Nombre: {self.nombre} 
                  Altura: {self.altura} Metros
                  velocidad: {self.velocidad} M/s
                  Resistencia: {self.resistencia}
                  Fuerza: {self.fuerza}""")
    
    