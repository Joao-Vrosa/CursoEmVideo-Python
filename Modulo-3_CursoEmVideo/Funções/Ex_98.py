"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep


def contador(i, f, p):
    for k in range(i, f, p):
        sleep(0.5)
        print(k)
    print('=' * 20)


# Programa principal
contador(1, 11, 1)
contador(10, -1, -2)

print('<<< Contagem personalizada! >>>')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('=' * 20)

contador(inicio, fim, passo)
