class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animales = []

    def add_animal(self, name):
        self.animales.append(name)
        return self

    def print_all_info(self):
        print("-"*30, "Animales en", self.name, "-"*30)
        for animal in self.animales:
            animal.display_info()