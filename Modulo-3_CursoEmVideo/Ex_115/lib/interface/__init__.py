"""
Exercício Python 115a: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples.
O sistema só vai ter 2 poções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""


def linha(tam=42):
    return '\033[92m~\033[0m' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0:31m[ERRO] Digite um numero valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('[0:31mUsuário preferiu nao digitar este campo!\033[m')
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[93m{cont}\033[0m - \033[94m{item}\033[0m')
        cont += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao

