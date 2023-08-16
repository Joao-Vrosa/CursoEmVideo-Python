'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
import os
from time import sleep

vitorias = calc = 0

while True:
    print("=" * 22)
    opcao = str(input("Par ou Impar [P/I]? ")).upper()[0]
    num = int(input("Digite um número: "))
    print("=" * 22)
    
    if num < 0:
        break
    
    # Gerando um número aleatório entre 0 e 10
    valorMaquina = randint(0, 10)
    
    if opcao == "P":
        calc = num + valorMaquina
        
        if calc % 2 == 0:
            vitorias += 1
            print("Vitória! Você jogou {} e seu oponente {}, somando {}. PAR!\nVitórias consecutivas: {}".format(num, valorMaquina, calc, vitorias))
            print("=-" * 30)
            sleep(5)
            os.system('cls') or None # Limpa a tela
            
        else:
            print("Derrota! Você jogou {} e seu oponente {}, somando {}. IMPAR!\nVitórias consecutivas: {}".format(num, valorMaquina, calc, vitorias))
            print("=-" * 30)
            break
            
    if opcao == "I":
        calc = num + valorMaquina
        
        if calc % 2 != 0:
            vitorias += 1
            print("Vitória! Você jogou {} e seu oponente {}, somando {}. IMPAR!\nVitórias consecutivas: {}".format(num, valorMaquina, calc, vitorias))
            print("=-" * 30)
            time.sleep(5)
            os.system('cls') or None # Limpa a tela
            
        else:
            print("Derrota! Você jogou {} e seu oponente {}, somando {}. PAR!\nVitórias consecutivas: {}".format(num, valorMaquina, calc, vitorias))
            print("=-" * 30)
            break

