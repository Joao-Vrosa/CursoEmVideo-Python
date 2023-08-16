"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n, show):
    """
    -> Calcula o fatorial de um número.
    :param n: Numero a ser calculado.
    :param show: (Opcional) Mostrar ou nao a conta.
    :return: Retorna o valor do fatorial, valor n.
    """
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


# Programa principal
valor = int(input('Digite o valor: '))

mostrar_conta = input('Deseja mostrar a conta[S/N]? ').upper()
if mostrar_conta in 'S':
    param = True
else:
    param = False

print(fatorial(valor, show=param))
