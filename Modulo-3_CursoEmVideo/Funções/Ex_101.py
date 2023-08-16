"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(nascimento):
    from datetime import date  # Importando a biblioteca dentro da def para economizar memoria

    ano_atual = date.today().year  # Pegando o ano atual
    idade = ano_atual - nascimento  # Verificando a idade

    print(f'A sua idade e de {idade} anos.', end=' ')

    if idade >= 16 and idade < 18 or idade >= 65:
        print('O seu voto e OPCIONAL')
    elif idade >= 18:
        print('O seu voto e OBRIGATÓRIO')
    else:
        print('Voce nao pode votar')


# Programa principal
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
voto(ano_nascimento)
