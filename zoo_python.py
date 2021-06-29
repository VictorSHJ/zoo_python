# Asignatura: Zoo
# Objetivos : Practica la utilización de la herencia
#             Más práctica con asociaciones entre clases.
#             Practica métodos primordiales
#             Mira el polimorfismo en acción
# Imagina un juego donde puedes crear un zoológico y comenzar a criar diferentes tipos de animales. Digamos que por cada zoológico 
# que crees puede haber varios animales diferentes. Comience creando una clase Animal y luego al menos 3 clases específicas de 
# animales que hereden de Animal. (Tal vez leones, tigres y osos) Cada animal debe tener al menos un nombre, una edad, 
# un nivel de salud y un nivel de felicidad. 
# OK La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal. 
# OK También debe tener un método de alimentación que aumente la salud y la felicidad en 10.
# OK En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único. 
# OK Dele a cada animal diferentes niveles predeterminados de salud y felicidad. 
# Los animales también deben responder al método de alimentación con diferentes niveles de cambios en la salud y la felicidad.
# Una vez que haya probado sus diferentes animales y se sienta más cómodo con la herencia, cree una clase de zoológico para ayudar 
# a manejar a todos sus animales.
# ¡Espero que esto parezca un poco repetitivo, y puede usar sus habilidades y conocimientos para reducir parte del código anterior y divertirse haciendo un zoológico en el proceso!
# Esta tarea es deliberadamente abierta. ¡Que te diviertas!
# Debe subir esta tarea con nombre zoo a Github.
# BONUS: Debe crear una forma interactiva (while True ;)) para poder ir creando animales e ir agregándolos al ZOO.

from colorama import init
from colorama import Fore, Back
from clases.zoos import Zoo
from clases.animales import Carnivoro, Hervivoro, Omnivoro

def agrega_muestra(nrozoo):
    if nrozoo == 1:
        BuinZoo.add_animal(newanimal)
        BuinZoo.print_all_info()
    elif nrozoo == 2:
        Metropolitano.add_animal(newanimal)
        Metropolitano.print_all_info()
    elif nrozoo == 3:
        Safari.add_animal(newanimal)
        Safari.print_all_info()

leon = Carnivoro("Leon Africano", 10, 30, 50)
tigre = Carnivoro("Tigre Siberiano", 12, 20, 40)
puma = Carnivoro("Puma Concolor", 5, 10, 20)
elefante = Hervivoro("Elefante", 50, 100, 200, "Barrito")
jirafa = Hervivoro("Jirafa", 20, 300, 500, "Zumba")

elefante.alimentacion()
jirafa.alimentacion()

lista_zoos = ["BuinZoo", "Metropolitano", "Safari"]
lista_especies = ["Carnivoro", "Hervivoro", "Omnivoro"]

BuinZoo = Zoo(lista_zoos[0])
BuinZoo.add_animal(leon).add_animal(tigre).add_animal(puma)
BuinZoo.print_all_info()

Metropolitano = Zoo(lista_zoos[1])
Metropolitano.add_animal(tigre).add_animal(elefante)
Metropolitano.print_all_info()

Safari = Zoo(lista_zoos[2])
Safari.add_animal(elefante).add_animal(jirafa)
Safari.print_all_info()

print("-"*30, "Fin", "-"*30)

""" Ciclo Interactivo de Ingreso de Informacion """
init()

while True:
    print(Fore.BLACK + Back.YELLOW + "="*30, "Seleccione Zoologico", "="*30)
    for i in range(0, (len(lista_zoos))):
        print(f"{i+1}. {lista_zoos[i]}") 
    print("9. Salir")
    nrozoo = int(input("Ingrese Opción :"))
    if nrozoo == 9:
        print(Fore.YELLOW + Back.BLACK + "*** Bye Bye ***")
        break

    while True:
        print(Fore.WHITE + Back.RED + "="*30, "Zoologico", lista_zoos[nrozoo-1], "="*30)
        print("1. Ingresar Animal")
        print("2. Mostrar Animales del Zoo")
        print("9. Volver")
        opcion = int(input("Ingrese Opción :"))
        if opcion == 9:
            break
        if opcion == 1:
            while True:
                print(Fore.WHITE + Back.BLUE + "="*30, "Ingresar Animal", "="*30)
                for i in range(0, (len(lista_especies))):
                    print(f"{i+1}. {lista_especies[i]}") 
                print("9. Salir")
                nroespecie = int(input("Ingrese Opción:"))
                if nroespecie == 9:
                    break
                elif nroespecie >= 1 and nroespecie <= 3:
                    while True:
                        print(Fore.WHITE + Back.GREEN + "="*30, "Ingresar un nuevo Animal", "="*30)
                        wnombre = input("1. Ingrese el Nombre : ")
                        wedad = input("2. Ingrese la Edad : ")
                        confirma = (input("Los Datos son correctos (S)i, (N)o, (F)in :"))
                        if confirma == "S":
                            print(Fore.WHITE + Back.GREEN + "="*30, "CREAR EL NUEVO ANIMAL", "="*30)
                            if opcion == 1:
                               newanimal = Carnivoro(wnombre, wedad, 10, 10)  
                            elif opcion == 2:
                                newanimal = Hervivoro(wnombre, wedad, 10, 10)
                            elif opcion == 3:
                                newanimal = Omnivoro(wnombre, wedad, 10, 10)
                            agrega_muestra(nrozoo) 
                            break
                        elif confirma == "F":
                            break
        elif opcion == 2:
            if nrozoo == 1:
                BuinZoo.print_all_info()
            elif nrozoo == 2:
                Metropolitano.print_all_info()
            elif nrozoo == 3:
                Safari.print_all_info()