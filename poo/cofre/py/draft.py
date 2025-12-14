from abc import ABC, abstractmethod

class Valuable(ABC):
    @abstractmethod
    def getLabel(self):
        pass

    @abstractmethod
    def getValue(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

    def __str__(self):
        return f"{self.getLabel()}:{self.getValue():.2f}:{self.getVolume()}"


class Coin(Valuable):
    def __init__(self, label, value, volume):
        self.label = label
        self.value = value
        self.volume = volume

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getVolume(self):
        return self.volume

    def __str__(self):
        return f"{self.label}:{self.value:.2f}:{self.volume}"

    __repr__ = __str__


class Item(Valuable):
    def __init__(self, label, volume, value):
        self.label = label
        self.volume = volume
        self.value = value

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getVolume(self):
        return self.volume

    def __str__(self):
        return f"{self.label}:{self.value:.2f}:{self.volume}"

    __repr__ = __str__


class Pig:
    def __init__(self, volumeMax):
        self.volumeMax = volumeMax
        self.broken = False
        self.valuables = []

    def addValuable(self, valuable):
        if self.broken:
            print("fail: the pig is broken")
            return False

        if self.getVolume() + valuable.getVolume() > self.volumeMax:
            print("fail: the pig is full")
            return False

        self.valuables.append(valuable)
        return True

    def breakPig(self):
        if self.broken:
            return False
        self.broken = True
        return True

    def getItems(self):
        if not self.broken:
            print("fail: you must break the pig first")
            return []

        items = []
        remaining = []

        for v in self.valuables:
            if isinstance(v, Item):
                items.append(v)
            else:
                remaining.append(v)

        self.valuables = remaining
        return items

    def getCoins(self):
        if not self.broken:
            print("fail: you must break the pig first")
            return []

        coins = []
        remaining = []

        for v in self.valuables:
            if isinstance(v, Coin):
                coins.append(v)
            else:
                remaining.append(v)

        self.valuables = remaining
        return coins

    def calcValue(self):
        return sum(v.getValue() for v in self.valuables)

    def getVolume(self):
        if self.broken:
            return 0
        return sum(v.getVolume() for v in self.valuables)

    def getVolumeMax(self):
        return self.volumeMax

    def isBroken(self):
        return self.broken

    def __str__(self):
        content = "[" + ", ".join(str(v) for v in self.valuables) + "]"
        state = "broken" if self.broken else "intact"
        return (f"{content} : {self.calcValue():.2f}$ : {self.getVolume()}/{self.volumeMax} : {state}")


def main():
    pig = None
    while True:
        line = input().strip()
        if line == "":
            continue

        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            pig = Pig(int(args[1]))

        elif args[0] == "show":
            print(pig)

        elif args[0] == "addCoin":
            coin_map = {"10": Coin("M10", 0.10, 1), "25": Coin("M25", 0.25, 2), "50": Coin("M50", 0.50, 3), "100": Coin("M100", 1.00, 4)}
            pig.addValuable(coin_map[args[1]])

        elif args[0] == "addItem":
            label = args[1]
            value = float(args[2])
            volume = int(args[3])
            pig.addValuable(Item(label, volume, value))

        elif args[0] == "break":
            pig.breakPig()

        elif args[0] == "extractItems":
            items = pig.getItems()
            if pig.isBroken():
                print("[" + ", ".join(str(i) for i in items) + "]")

        elif args[0] == "extractCoins":
            coins = pig.getCoins()
            if pig.isBroken():
                print("[" + ", ".join(str(c) for c in coins) + "]")

main()