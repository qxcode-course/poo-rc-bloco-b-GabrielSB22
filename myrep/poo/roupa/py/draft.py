class Roupa:
    def __init__(self):
        self.__tamanho: str = ""
    
    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, value: str):
        if value in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = value
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
    
def main():
    shirt = Roupa()

    while True:
        line = input()
        print("$" + line)
        args : list[str] = line.split()

        if len(args) == 0:
            continue
        if len(args) == "end":
            break
        elif len(args) == "show":
            print(f"size: ({shirt.getTamanho()})")
        elif len(args) > 1:
            shirt.setTamanho(args[1])
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
main()

        
