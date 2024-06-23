# C = int(input("Digite o número de casos: "))
# for i in range(C):
#     nivel_energia = int(input("Digite o nível de energia: "))
#     if nivel_energia <= 8000:
#         print("Inseto!")
#     else:
#         print("Mais de 8000!")

# T = int(input())
# for i in range(T):
#    i = input()
#    i = i.split()
#    N = int(i[0])
#    K = int(i[1])
#    garrafas_cheias = N // K
#    garrafas_vazias = N % K
#    total = garrafas_vazias + garrafas_cheias
#    print(total)

a = input()
b = input()
c = input()

animais = {
    ('vertebrado', 'ave', 'carnivoro'): 'aguia',
    ('vertebrado', 'ave', 'onivoro'): 'pomba',
    ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
    ('vertebrado', 'mamifero', 'onivoro'): 'homem',
    ('invertebrado', 'inseto', 'hematofago'): 'pulga',
    ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
    ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
    ('invertebrado', 'anelideo', 'onivoro'): 'minhoca'
}

print(animais[(a, b, c)])