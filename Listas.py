#Listas: Em Python, a lista é um objeto do tipo list.
lista1 = [2, 3.2, "Matheus"]
print(lista1[2])
print(lista1[-2])

lista2 = [5, 8.2, 75, 14, 55]
print(lista2[1:4])
print(lista2[-2:])

lista3 = [4, 3.6, 84, 21]
lista3[1] = 26
print(lista3)

#Operações com lista
#.append() é a maneira utilizada para inserir um valor no final da lista.
lista4 = [1, 2, 3, 4, 5]
lista5 = lista4[:]
lista5[0] = 485
lista5.append(34)
print(lista4)
print(lista5)

#.insert(pos,elemento), basicamente sua função é inserir o elemento na posição pos.
lista4.insert(0,78)
print(lista4)

#.pop() retira o último elemento da lista
#.pop(index) retira o elemento no index indicado.
lista6 = [5, 4, 3, 2, 1]
a = lista6.pop(0)
print(a)
b = lista6.pop()
print(b)
print(lista6)

#.sort() ordena os valores em ordem crescente ou alfabética, variando de acordo com o tipo de dados da lista.
lista7 = [12, 47, 1, 3, 9]
lista7.sort()
print(lista7)

#.reverse() ou .sort(reverse=True) fazem o oposto do .sort() e ordenam a lista de forma decrescente.
lista7.reverse()
print(lista7)

#.count(elemento) mostra quantas vezes elemento aparece na lista.
lista8 = [1,2,1,1,4,5,1]
print(f'.count(elemento): {lista8.count(1)}')