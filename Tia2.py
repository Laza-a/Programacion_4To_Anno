class Instrument:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def play_sound(self):
        print("The instrument is playing a note.")


class Guitar(Instrument):
    def play_sound(self):
        print("Strumming strings!")


class Drum(Instrument):
    def play_sound(self):
        print("Boom boom!")


# Crear objetos
guitar = Guitar("Guitar", "String")
drum = Drum("Drum", "Percussion")

# Llamar al método
guitar.play_sound()
drum.play_sound()