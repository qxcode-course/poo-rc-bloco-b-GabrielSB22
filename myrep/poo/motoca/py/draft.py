class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        
    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def __str__(self):
        return f"{getName}:{getAge}"

class Motoca:
    def __init__(self, potencia: int, time:int, pessoa):
        self.__potencia = 1
        self.__time = 0
        self.__pessoa = None

    def __str__(self):
        return f"power:{self.__potencia}, time:{self.__time}, person:({self.__pessoa})"

    def Inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
        self.__pessoa = Pessoa
        return

    def Remover(self):
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        pessoaremovida = self.__pessoa
        self.__pessoa = None
        return pessoaremovida

    def BuyTime(self, time: int):
         self.__time += time

    def Drive(self, time: int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        elif self.__pessoa is None:
            print("fail: empty motorcicle")
            return
        elif self.__age > 10:
            print("fail: too old to drive")
            return
        elif time > self.__time:
            print("fail: time finished after", self.__time, "minutes")
            self.__time = 0
            return
        else:
            self.__time -= time
            return

    def Init(self):
        self.__potencia = 1
        self.__time = 0
        self.__pessoa = None

    def Honk(self):
        print("P" + "e" * self.__potencia + "m!")


def main():
    motinha = Motoca()

    while True:
        line = input()
        print("$" + line)
        args = line.split()
    
    if args[0] == "end":
        break
    elif args[0] == "show":
        print(motinha)
    elif args[0] == "init":
        motinha.Init()
    elif args[0] == "enter":
        nome = args[1]
        idade = int(args[2])
        motinha.Inserir(nome, idade)
    elif args[0] == "leave":
        motinha.leave()
    elif args[0] == "buy":
        motinha.BuyTime(int(args[1]))
    elif args[0] == "honk":
        motinha.Honk()
    else:
        print("fail: comando inválido")
main()     