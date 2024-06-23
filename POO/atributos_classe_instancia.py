class Estudante:
    # variavel de classe
    escola = "IFCE"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrar_valores(*objts):
    for objt in objts:
        print(objt)

estudante = Estudante("Matheus", 123)
estudante2 = Estudante("Pedro", 456)
mostrar_valores(estudante, estudante2)

# variavel de instancia
Estudante.escola = "DIO"

estudante3 = Estudante("Lucas", 789)
estudante4 = Estudante("Maria", 987)
mostrar_valores(estudante3, estudante4)