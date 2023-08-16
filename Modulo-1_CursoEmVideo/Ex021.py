import random

lista = []
for i in range(4):
    aluno = input("Aluno: ")
    lista.append(aluno)

    random.shuffle(lista) # SHUFFLE altera a ordem da lista.

print("A ordem da lista será ")
print(lista)

