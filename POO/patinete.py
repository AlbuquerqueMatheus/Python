class patinete:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Din, din!!!")

    def parar(self):
        print("freiando...")
        print("freiou!")

    def correr(self):
        print("Vrummm!!!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


foston = patinete("Cinza", "foston S09-pro", 2023, 2500)
foston.correr()
foston.buzinar()
foston.parar()
print(foston.cor, foston.modelo, foston.ano, foston.valor)

foston2 = patinete("Preto", "foston S08-pro", 2019, 1800)
patinete.buzinar(foston2)
print(foston2)