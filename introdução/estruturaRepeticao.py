#Estrutura de repetição
vendidos = 0
parada = 1

while parada != 0:
    nome = input("Digite seu nome:\n")
    idade = int(input("Digite sua idade:\n"))
    
    if idade >= 16:
        vendidos +=1
    else:
        print(f"{nome} não pode comprar o jogo, pois não atingiu a idade minima")
    parada = int(input("Digite 1 para continuar ou 0 para finalizar\n"))
print(f"{vendidos} jogos foram vendidos hoje!")

#range(start, stop, step) é uma função que gera uma sequência de números começando em start e terminando antes de stop, com um passo opcional step.
for i in range(8):
    print(i)
for i in range(2,6):
    print(i)
for i in range(0,10,2):
    print(i)