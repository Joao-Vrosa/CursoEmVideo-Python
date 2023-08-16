"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31m[ERRO] Digite um numero valido!\033[m')
        if ok:
            break
    return valor


numero = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {numero}')

"""


def leiaInt(num):
    while True:
        try:
            n = int(input('Digite um numero Inteiro: '))
        except (ValueError, TypeError):
            print('\033[0:31m[ERRO] Digite um numero valido!\033[m')
            continue
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input('Digite um numero Real: '))
        except (ValueError, TypeError):
            print('\033[0:31m[ERRO] Digite um numero valido!\033[m')
            continue
        else:
            return n


n1 = leiaInt('Digite um numero Inteiro: ')
n2 = leiaFloat('Digite um numero Real: ')
print(f'O valor digitado foi {n1} e {n2}')
