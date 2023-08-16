import random

l = []

for i in range(4):
    nome = input("Digite os nomes: ")
    l.append(nome)
    escolhido = random.choice(l)
    # CHOICE vai escolher um valor dentro da lista

print(escolhido)

