"""
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando DEF em Python e como utilizá-lo com parâmetros simples e múltiplos.
"""


def mostrar_linha():  # DEF sem parâmetros
    print('-' * 25)


# Programa principal
mostrar_linha()
print('Ola, Mundo!')
mostrar_linha()
##


def mensagem(msg):  # DEF com parâmetros
    print('-' * 25)
    print(msg)
    print('-' * 25)


# Programa principal
mensagem('Hello, Word!')
##


def soma(x, y):   # DEF com parâmetros numericos
    calc = x + y
    print(f'A soma de {x} + {y} e {calc}')


# Programa principal
soma(5, 5)
soma(x=2, y=3)
soma(y=5, x=2)

mostrar_linha()


def contador(*num):  # Empacotamento de parâmetros
    tamanho = len(num)
    print(f'Recebi os valores {num} que sao ao todo {tamanho} numeros')


# Programa principal
contador(1, 2, 3)
contador(1, 2)
contador(1, 2, 3, 4, 5)

mostrar_linha()


def dobra(lista):   # DEF com parâmetros listas | Lista dois
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
    print(lista)


# Programa principal
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Lista um
dobra(valores)
print(valores)
##

mostrar_linha()
