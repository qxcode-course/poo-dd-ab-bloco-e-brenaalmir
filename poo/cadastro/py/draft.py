from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, accId: int, clientId: str, typeId: str):
        self.accId = accId
        self.clientId = clientId
        self.typeId = typeId
        self.balance = 0.0

    def deposit(self, value: float):
        self.balance += value

    def withdraw(self, value: float):
        if self.balance < value:
            print("fail: saldo insuficiente")
            return False
        self.balance -= value
        return True

    def transfer(self, other, value: float):
        if self.withdraw(value):
            other.deposit(value)

    def getBalance(self):
        return self.balance

    def getId(self):
        return self.accId

    def getClientId(self):
        return self.clientId

    def getTypeId(self):
        return self.typeId

    @abstractmethod
    def updateMonthly(self):
        pass

    def __str__(self):
        return f"{self.accId}:{self.clientId}:{self.balance:.2f}:{self.typeId}"


class CheckingAccount(Account):
    def __init__(self, accId: int, clientId: str):
        super().__init__(accId, clientId, "CC")
        self.monthlyFee = 20.0

    def updateMonthly(self):
        self.balance -= self.monthlyFee


class SavingsAccount(Account):
    def __init__(self, accId: int, clientId: str):
        super().__init__(accId, clientId, "CP")
        self.monthlyInterest = 0.01

    def updateMonthly(self):
        self.balance += self.balance * self.monthlyInterest


class Client:
    def __init__(self, clientId: str):
        self.clientId = clientId
        self.accounts = []

    def addAccount(self, acc: Account):
        self.accounts.append(acc)

    def getAccounts(self):
        return self.accounts

    def getClientId(self):
        return self.clientId

    def __str__(self):
        ids = [acc.getId() for acc in self.accounts]
        return f"{self.clientId} {ids}"


class Agency:
    def __init__(self):
        self.accounts = {}
        self.clients = {}
        self.nextAccountId = 0

    def addClient(self, clientId: str):
        client = Client(clientId)
        self.clients[clientId] = client
        acc_cc = CheckingAccount(self.nextAccountId, clientId)
        self.accounts[self.nextAccountId] = acc_cc
        client.addAccount(acc_cc)
        self.nextAccountId += 1
        acc_cp = SavingsAccount(self.nextAccountId, clientId)
        self.accounts[self.nextAccountId] = acc_cp
        client.addAccount(acc_cp)
        self.nextAccountId += 1

    def getAccount(self, accId: int):
        if accId not in self.accounts:
            print("fail: conta nao encontrada")
            return None
        return self.accounts[accId]

    def deposit(self, accId: int, value: float):
        acc = self.getAccount(accId)
        if acc:
            acc.deposit(value)

    def withdraw(self, accId: int, value: float):
        acc = self.getAccount(accId)
        if acc:
            acc.withdraw(value)

    def transfer(self, fromId: int, toId: int, value: float):
        accFrom = self.getAccount(fromId)
        accTo = self.getAccount(toId)
        if accFrom and accTo:
            accFrom.transfer(accTo, value)

    def updateMonthly(self):
        for acc in self.accounts.values():
            acc.updateMonthly()

    def show(self):
        print("- Clients")
        for client in self.clients.values():
            print(client)
        print("- Accounts")
        for acc in self.accounts.values():
            print(acc)


def main():
    bank = Agency()
    while True:
        line = input().strip()
        if line == "":
            continue
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        
        elif args[0] == "addCli":
            bank.addClient(args[1])

        elif args[0] == "show":
            bank.show()

        elif args[0] == "deposito":
            bank.deposit(int(args[1]), float(args[2]))

        elif args[0] == "saque":
            bank.withdraw(int(args[1]), float(args[2]))

        elif args[0] == "transf":
            bank.transfer(int(args[1]), int(args[2]), float(args[3]))

        elif args[0] == "update":
            bank.updateMonthly()

main()