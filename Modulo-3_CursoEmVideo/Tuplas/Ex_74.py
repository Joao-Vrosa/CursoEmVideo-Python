'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint


# Gerando numeros aleatorios dentro de uma tupla.
NumAleatorio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Numeros gerados: ', end='')

for i in NumAleatorio:
    print(f'{i} ', end='')

print(f'\nMaior valor: {max(NumAleatorio)}')
print(f'Menor valor: {min(NumAleatorio)}')

