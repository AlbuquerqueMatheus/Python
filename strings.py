'''
METODOS UTEIS DA CLASSE STRING
'''

# MAIÚSCULAS, minúsculas e Título:
nome = "MaTheuS"

print(nome.upper())
print(nome.lower())
print(nome.title())

#Eliminando espaços em branco
nome = " Muniz"

print(nome.strip())
print(nome.lstrip())
print(nome.rsplit())

#Centralização e Junções
curso = "python"

print(curso.center(10, "*"))
print(".".join(curso))

