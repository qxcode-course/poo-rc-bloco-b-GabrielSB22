class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, value: str):
        if value in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = value
        else:
            print("Tamanho de roupa não existente")

def main():
    shirt = Camisa()
    while shirt.getTamanho() == "":
        print("Digite o seu tamanho de roupa")
        tamanho = input(": ")
        shirt.setTamanho(tamanho)
    print("Congratulations, você comprou uma roupa tamanho", shirt.getTamanho())
main()