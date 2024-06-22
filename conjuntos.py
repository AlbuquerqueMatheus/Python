#ESTRUTURA SET

"""
Não tem duplicação, elementos unicos de tro de um objeto
"""
numeros = set([1,1,1,5,5,5,6,8,9])
print(numeros)

teste = {1,2,2,3,3,4,4,4,4}
print(teste)

#convertendo set -> lista, para Acessar dados
num = {6,3,3,5,6}
num = list(num)
print(num[0])

#Função enumerate
carros = {"gol", "celta", "palio"}
for i, carro in enumerate(carros):
    print(f"{i}: {carro}")

#metodos set {}.union, {}.intersection, {}.difference
#{}.union
conj_a = {1,2}
conj_b = {3,4}

print(conj_a.union(conj_b))

#{}.intersection : tudo que tem em comum entre os conjuntos
conj_a = {1,2,3}
conj_b = {3,4,5}

print(conj_a.intersection(conj_b))

#{}.difference: tudo que esta em um conjunto e não esta no outro
conj_a = {1,2,3}
conj_b = {3,4,5}

print(conj_a.difference(conj_b))

#{}.symmetric_difference: tudo que esta em um conjunto e não esta no outro, porem retorna de ambos os conjuntos
conj_a = {1,2,3}
conj_b = {3,4,5}

print(conj_a.symmetric_difference(conj_b))

#{}.issubset e {}.issuperset
conj_a = {1,2,3}
conj_b = {4,1,2,5,6,3}

print(conj_a.issubset(conj_b))
print(conj_b.issubset(conj_a))

print(conj_a.issuperset(conj_b))
print(conj_b.issuperset(conj_a))

#{}.isdisjoint todos o elementos de um conjunto n estão presentes no outro conjunto
conj_a = {1,2,3,4,5}
conj_b = {6,7,8,9}
conj_c = {1,0}

print(conj_a.isdisjoint(conj_b))
print(conj_a.isdisjoint(conj_c))

#{}.add
sorteio = {1,23}

sorteio.add(45)
sorteio.add(32)
sorteio.add(18)
print(sorteio)

#{}.clear
sorteio = {1,23}
sorteio.clear()

#{}.copy
sorteio = {1,23}
sorteio.copy()

#{}.discard / {}.remove se o elemento não existe retorna erro
numeros = {1,4,7,12,34,2,9,7,6}
numeros.discard(7)

#{}.pop sempre tira valores da frente
numeros = {1,4,7,12,34,2,9,7,6}
numeros.pop()

#len: tamanho do conjunto
numeros = {1,4,7,12,34,2,9,7,6}
len(numeros)

# in: verifica se um elemento está dentro do conjunto
numeros = {1,4,7,12,34,2,9,7,6}
1 in numeros