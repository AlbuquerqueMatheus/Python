
## EXERCICIOS ##

'''
01-faça um programa que peça dois numeros inteiros e um numero float. Calcule e mostre:
a)O produto do dobro do primeiro com metade do segundo
b)A soma do triplo do primeiro com o terceiro
c)O terceiro elevado ao cubo
'''

numInt1 = int(input("DIgite um número interiro: \n"))
numInt2 = int(input("DIgite um número interiro: \n"))
numFloat3 = float(input("DIgite um número float: \n"))

a = (numInt1 * 2) * (numInt2 / 2)
b = (numInt1 * 3) + numFloat3
c = numFloat3 ** 3

print(f'a){a}\nb){b}\nc){c}')

'''
02-faça um programa para uma loja de tintas.O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada.Considere que a cobertura da tinta é de 1 litro para cada
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
'''
tamanho = float(input("Digite o tamanho em m² da área a ser pintada:"))
custo = float(80.00)

#ValoresConhecidos
litro = int(1)
metro = int(3)

quantidade = (litro * tamanho) / metro
preco = quantidade * custo
print(f'Para {tamanho}m² é necessario {quantidade:.2f} litros de Tinta! Que custam R${preco:.2f}')

'''
03-faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato.
'''

sapato = float(input("Qual o valor do sapato?"))
relogio = float(input("Qual o valor do relogio?"))
perfume = float(input("Qual o valor do perfume?"))

precos = [sapato, relogio, perfume]
menor_valor = precos[0]

for elemento in precos:
    elemento < menor_valor
    menor_valor = elemento
print(f'O produto mais barato custa: {menor_valor}')


'''
04-faça um programa que utilize um loop para ler números do usuario até que o número 0 
seja inserido, e então imprima a soma dos números inseridos
'''
soma = []
numero = 1

while numero != 0:
    numero = int(input("digite um número\n"))
    if numero != 0:
        soma.append(numero)
    else:
        add = sum(soma)
        print(f'a soma de todos os valores é: {add}')
    
'''
05-Escreva uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.
'''
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
pares = []

for numero in lista:
    if numero % 2 ==0:
        pares.append(numero)
print(f'numeros pares são: {pares}')

'''
06-Crie uma função que encontre o segundo maior número em uma lista de números.
'''
lista = [7,42,85,2,1,32]
print(lista)
maior = lista[0]
segundo_maior = float('-inf') #representa o valor negativo infinito, indicando o menor valor possível em um intervalo.

for numero in lista:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior: 
        segundo_maior = numero
print(segundo_maior)

'''
07-Faça um programa que receba uma string e responda se ela tem alguma vogal,
se sim quais são? e também diga se ela é uma frase ou não.
'''
texto = " s m strng"

if 'a' in texto or 'e' in texto or 'i' in texto or 'o' in texto or 'u' in texto:
    print("temos vogal no texto")
elif " " in texto:
    print("é um texto")
else:
    print("não tem vogal")

'''
08-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido
'''
while True:
    nota = int(input("Digite o valor da nota entre 0 e 10: \n"))
    if nota > 10 or nota < 0:
        print("valor invalido!")
        nota = int(input("Digite o valor da nota entre 0 e 10: \n"))
    else:
        print("Nota valida")
        break

'''
09-Faça um programa que leia 3 numeros e informe o maior valor:
'''
num1 = int(input("Numero1:\n"))
num2 = int(input("Numero2:\n"))
num3 = int(input("Numero3:\n"))
lista = [num1,num2,num3]
maior_valor = lista[0]

for numero in lista:
    if numero > maior_valor:
        maior_valor = numero
print(f'maior valor: {maior_valor}')

'''
10-Faça um programa que itera uma strig e toda vez que uma vogal
aparecer na sua string print o seu nome entre as letras:
'''
palavra = "canela"

for i in palavra:
    if i in "aeiou":
        print("matheus!")
    else:
        print(i)

'''
11-Faça um programa que receba uma string, com um número de ponto flutuante,
e imprima qual a parte dele que não é inteira:
'''
palavra = "25.569"
parte_fracionada = ""

for i in palavra:
    if i == ".":
        indice = palavra.index(".")
        parte_fracionada = palavra[indice+1:]
        print(parte_fracionada)

'''
12-Faça um programa que dada uma lista[], e um número inteiro,
imprima a tabuada desse número:
'''
lista = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Digite um número:\n"))

for i in lista:
    mult = num * i
    print(f"{num} x {i} = {mult}")

'''
13- Faça um programa que dada a entrada de uma lista o programa calcule 
a combinatória de dois elementos e nos retorne as combinações em uma nova lista:
'''
lista = [1,2,3,4]
lista_comb = []

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        lista_comb.append((lista[i],lista[j]))
print(lista_comb)

'''
14-Faça um programa que dada a entrada de uma lista ele faça o cálculo
acumulativo da mesma:
'''
lista = [1,2,3,4]
calc_comb = []
total = 0

for i in lista:
    total += i
    calc_comb.append(total)
print(calc_comb)

'''
15-Faça um programa, com uma função, que calcula a mediana de uma lista.
'''
def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista)

    if n % 2 == 0:
        meio_esquerdo = n // 2 - 1
        meio_direito = meio_esquerdo + 1
        mediana_par = (lista_ordenada[meio_esquerdo] + lista_ordenada[meio_direito]) / 2
        return mediana_par
    else:
        meio = n // 2
        mediana_impar = lista_ordenada[meio]
        return mediana_impar

teste = [3,5,7,1,4,8,9]
print(mediana(teste))

'''
16-faça um programa, com uma função que dado uma lista e uma posição da mesma
faça o quartil dessa posição.
'''
def P_quartil(lista):
    lista_ordenada = sorted(lista)
    meio = len(lista_ordenada) // 2
    q1 = mediana(lista_ordenada[:meio])
    return q1

teste1 = [1,2,3,4,5,6,7,8]
print(P_quartil(teste1))

'''
17-faça um programa, com uma função, que calcule a dispersão de uma lista:

a)Suponha que você tem uma lista das temperaturas diárias registradas em uma semana e deseja saber a variação da temperatura durante esse período.(Amplitude)
b)Avaliar a variabilidade dos níveis de colesterol em um grupo de pacientes.(Desvio Padrão / variância)
c)Calcule o IQR, para fazer uma análise de Desempenho do teste de matematica aplicado em uma sala de aula:
'''
#resposta item a:
def amplitude(lista):
    if not lista:
        return 0
    return max(lista) - min(lista)

temp = [25,31,28,15,35,-1]
print(amplitude(temp))
#resposta item b:
import math
def media(lista):
    return sum(lista) / len(lista)

def desvio_padrao(lista):
    med = media(lista)
    somatorio = 0

    for i in lista:
        somatorio += (i - med) ** 2

    var = somatorio / len(lista)
    dp = math.sqrt(var)
    return dp    

n = [3, 7, 6, 5, 4]
print(desvio_padrao(n))

#resposta item b:
def intervalo_interquartil(lista):
    lista_ordenada = sorted(lista)
    meio = len(lista_ordenada) // 2
    q3 = mediana(lista_ordenada[meio:])
    iqr = q3 - P_quartil(lista)
    return iqr

notas = [60,85,40,90,73,20] 
print(intervalo_interquartil(notas))

'''
18-Dada uma lista de palavras, conte a ocorrência de cada palavra usando um dicionário:
'''
palavra = ['oi', 'tudo', 'oi', 'bem', 'xau']
contagem = {}

for palavra in palavra:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

'''
19-Dado um dicionário, crie um novo dicionário invertido onde os valores se tornam as chaves e as chaves se tornam os valores:
'''
normal = {'nome':'muniz', 'numero': 19, 'posicao': 'armador'}
invertido = {valor: chave for chave, valor in normal.items()}
print(invertido)

'''
20-Dado dois dicionários, mescle-os em um único dicionário. Se houver chaves duplicadas, mantenha o valor do segundo dicionário.
'''
a = {'q': 2, 'w': 4, 'c': 9, 'e': 6, 'r': 3}
b = {'a': 1, 'b': 3, 'c': 5, 'd': 6, 'e': 2}
mesclado = {**a, **b}
print(mesclado)

'''
21-Escreva uma função que conte a ocorrência de cada caractere em uma string usando um dicionário.
'''
def contar(string):
    contagem = {}
    for i in string:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
    return contagem
s = 'cuccoio'
print(contar(s))

'''
Dado um dicionário onde as chaves são nomes de alunos e os valores são suas notas,
escreva uma função que agrupe os alunos por faixas de notas (ex: 90-100, 80-89, etc.).
'''
def agrupar_por_notas(dicionario):
    grupos = {
        "90-100": [],
        "80-89": [],
        "70-79": [],
        "60-69": [],
        "0-59": []
    }
    for aluno, nota in dicionario.items():
        if 90 <= nota <= 100:
            grupos["90-100"].append(aluno)
        elif 80 <= nota <= 89:
            grupos["80-89"].append(aluno)
        elif 70 <= nota <= 79:
            grupos["70-79"].append(aluno)
        elif 60 <= nota <= 69:
            grupos["60-69"].append(aluno)
        else:
            grupos["0-59"].append(aluno)
    return grupos
alunos = {"Alice": 85, "Bob": 92, "Carlos": 78, "Diana": 65, "Eva": 58}
print(agrupar_por_notas(alunos))

for i in range(100):
    if i % 2 == 0:
        continue
    print(i)