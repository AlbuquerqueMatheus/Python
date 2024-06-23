class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("Auau")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

def criar_cachorro():
    c = Cachorro("Marley", "caramelo", False)
    print(c)

c = Cachorro("belinha", "branca")
c.falar()

criar_cachorro()

#Forçar remoção de referencia de um objeto: del