class Animal:
    def __init__(self, ani_name, ani_edad, ani_salud, ani_felicidad):
        self.nombre = ani_name
        self.edad = ani_edad
        self.salud = ani_salud
        self.felicidad = ani_felicidad

    def alimentacion(self):
        self.salud += 10
        self.felicidad += 10
        print(f"*** Alimento a {self.nombre}, Salud: {self.salud}, Felicidad: {self.felicidad} ***")
        return self

    def suenno(self):
        raise NotImplementedError

    def display_info(self):
        print(f"Nombre: {self.nombre}, Salud: {self.salud}, Felicidad: {self.felicidad}")

class Carnivoro(Animal):
    def __init__(self, carnivoro_nombre, carnivoro_edad, carnivoro_salud, carnivoro_felicidad):
        super().__init__(carnivoro_nombre, carnivoro_edad, carnivoro_salud, carnivoro_felicidad)
        self.sonido = "Ruge"
        self.alimento = "Carne"
        self.suenno = 12

    def suenno(self):
        print(f"El animal {carnivoro_nombre}, debe dormir {self.suenno}, horas")    

class Hervivoro(Animal):
    def __init__(self, hervivoro_nombre, hervivoro_edad, hervivoro_salud, hervivoro_felicidad, hervivoro_sonido=""):
        super().__init__(hervivoro_nombre, hervivoro_edad, hervivoro_salud, hervivoro_felicidad)
        self.sonido = hervivoro_sonido
        self.alimento = "Vegetales"
    def display_detalle(self):
        print(f"Emite Sonido; {self.sonido}, Alimento: {self.alimento}")

class Omnivoro(Animal):
    def __init__(self, omnivoro_nombre, omnivoro_edad, omnivoro_salud, omnivoro_felicidad, omnivoro_sonido=""):
        super().__init__(omnivoro_nombre, omnivoro_edad, omnivoro_salud, omnivoro_felicidad)
        self.sonido = omnivoro_sonido
        self.alimento = "Todo"
    def display_detalle(self):
        print(f"Emite Sonido; {self.sonido}, Alimento: {self.alimento}")