class Watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0

        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def getHora(self):
        return self.__hora

    def setHora(self, h: int):
        if h >= 0 and h <= 23:
            self.__hora = h
        else:
            print("fail: hora invalida")

    def getMinuto(self):
        return self.__minuto

    def setMinuto(self, m: int):
        if m >= 0 and m <= 59:
            self.__minuto = m
        else:
            print("fail: minuto invalido")

    def getSegundo(self):
        return self.__segundo

    def setSegundo(self, s: int):
        if s >= 0 and s <= 59:
            self.__segundo = s
        else:
            print("fail: segundo invalido")

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0
    
def main():
    reloj = Watch()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
            
        if args[0] == "show":
            print(reloj)

        if args[0] == "set":
            h, m, s = map(int, args[1:])
            reloj.setHora(h)
            reloj.setMinuto(m)
            reloj.setSegundo(s)

        if args[0] == "next":
            reloj.nextSecond()

        if args[0] == "init":
            h, m, s = map(int, args[1:])
            reloj = Watch(h, m, s )
main()