"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

lista = []
jogos = []

QtdJogadas = int(input("Quantos jogos? "))
total = 1

while total <= QtdJogadas:
    cont = 0
    while True:
        gerarNum = randint(1, 60)
        if gerarNum not in lista:
            lista.append(gerarNum)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f'SORTEANDO {QtdJogadas} JOGOS', '=-' * 3)
for i, l in enumerate(jogos):
    sleep(0.7)
    print(f'Jogo {i+1}: {l}')

print('-=' * 3, f'SORTEIO FINALIZADO', '=-' * 3)
