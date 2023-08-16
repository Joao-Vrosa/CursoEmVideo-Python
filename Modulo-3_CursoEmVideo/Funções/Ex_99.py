"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

numeros = list()


def maior(num):
    print('=-' * 25)

    print(f'Os valores passados foram: ', end='')
    for i in num:
        print(f'{i}', end=' ')

    print()
    print(f'Foram ao todo {len(num)} numeros.')
    print(f'O maior valor foi: {max(num)}')

    print('=-' * 25)


# Programa principal
while True:
    numeros.append(int(input('Digite um numero? ')))

    continuar = str(input('>>> Deseja continuar? ')).upper()
    if continuar in 'N':
        break

maior(numeros)
