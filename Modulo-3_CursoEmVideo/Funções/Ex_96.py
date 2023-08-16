"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(l, c):
    calc = l * c
    print(f'Area: {calc}')


# Programa principal
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area(largura, comprimento)
