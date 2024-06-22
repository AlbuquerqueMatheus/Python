def media (lista):
    return sum(lista) / len(lista)

lista = []
while len(lista) != 4:
    num = int(input("Digite um numero:\n"))
    lista.append(num)
print(media(lista))

'''
*args e **Kwargs
recebe uma tupla e um dicionarios respectivamente
''' 


