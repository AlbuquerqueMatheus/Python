class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def eh_maior_idade(idade):
        if idade >= 18:
            return True
        else:
            return False
    
p = Pessoa("Matheus", 26)
print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1998, 3, 2, "Matheus")
print(p2.nome, p2.idade)

print(Pessoa.eh_maior_idade(26))
print(Pessoa.eh_maior_idade(17))