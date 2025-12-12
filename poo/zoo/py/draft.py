from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(salf):
        pass


class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Roooaaarr")

    def mover(self):
        print("O leão caminha pela savana")


class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Prrruu")

    def mover(self):
        print("O elefante anda pesadamente")

    
class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Sssss")

    def mover(self):
        print("A cobra rasteja pelo chão")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Tipo do objeto: {type(animal)}")
    print("-" * 40)


#testes

animais = [
    Leao("Leão"),
    Elefante("Elefante"),
    Cobra("Cobra")
]

for a in animais:
    apresentar(a)