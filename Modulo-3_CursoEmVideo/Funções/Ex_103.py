"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


# Programa principal
nome_jogador = str(input('Qual o seu nome: '))
qtdGols = str(input('Quantos gols voce fez? '))

if qtdGols.isnumeric():
    qtdGols = int(qtdGols)
else:
    qtdGols = 0

if nome_jogador.strip() == '':
    ficha(gols=qtdGols)
else:
    ficha(nome_jogador, qtdGols)
