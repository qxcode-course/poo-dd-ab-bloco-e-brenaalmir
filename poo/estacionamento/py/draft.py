from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, tipo, id, entrada):
        self.tipo = tipo
        self.id = id
        self.entrada = entrada

    @abstractmethod
    def calcularValor(self, saida):
        pass

    def toString(self):
        return(self.tipo.rjust(10, "_") + " : " + self.id.rjust(10, "_") + " : " + str(self.entrada))


class Bike(Veiculo):
    def __init__(self, id, entrada):
        super().__init__("Bike", id, entrada)

    def calcularValor(self, saida):
        return 3.0


class Moto(Veiculo):
    def __init__(self, id, entrada):
        super().__init__("Moto", id, entrada)

    def calcularValor(self, saida):
        minutos = saida - self.entrada
        return minutos / 20


class Carro(Veiculo):
    def __init__(self, id, entrada):
        super().__init__("Carro", id, entrada)

    def calcularValor(self, saida):
        minutos = saida - self.entrada
        valor = minutos / 10
        return valor if valor >= 5 else 5.0


class Estacionamento:
    def __init__(self):
        self.veiculos = {}
        self.hora_atual = 0

    def tempo(self, minutos):
        self.hora_atual += minutos

    def estacionar(self, tipo, id):
        if tipo == "bike":
            v = Bike(id, self.hora_atual)
        elif tipo == "moto":
            v = Moto(id, self.hora_atual)
        else:
            v = Carro(id, self.hora_atual)
        self.veiculos[id] = v

    def pagar(self, id):
        v = self.veiculos[id]
        valor = v.calcularValor(self.hora_atual)
        print(f"{v.tipo} chegou {v.entrada} saiu {self.hora_atual}. Pagar R$ {valor:.2f}")
        del self.veiculos[id]

    def show(self):
        for v in self.veiculos.values():
            print(v.toString())
        print(f"Hora atual: {self.hora_atual}")


def main():
    est = Estacionamento()
    while True:
        line = input().strip()
        if not line:
            continue
        print("$" + line)
        args = line.split()

        if args[0] == "tempo":
            est.tempo(int(args[1]))

        elif args[0] == "estacionar":
            est.estacionar(args[1], args[2])

        elif args[0] == "pagar":
            est.pagar(args[1])

        elif args[0] == "show":
            est.show()

        elif args[0] == "end":
            break

main()