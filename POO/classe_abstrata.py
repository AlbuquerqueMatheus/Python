from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv")

    def desligar(self):
        print("Desligando a tv")

    @property
    def marca(self):
        return "Philco"

class Controle_arcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o arcondicionado")

    def desligar(self):
        print("Desligando o arcondicionado")

    @property
    def marca(self):
        return "LG"
    
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = Controle_arcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)