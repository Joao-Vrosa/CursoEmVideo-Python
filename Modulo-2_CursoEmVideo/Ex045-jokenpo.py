import random
from time import sleep

def Jogo(num, jogada):
    # VALORES IGUAIS #
    if num == 1 and jogada == 1:
        resultado = "\n>>> EMPATE!! Os dois jogaram PEDRA <<<"
        return resultado
    elif num == 2 and jogada == 2:
        resultado = "\n>>> EMPATE!! Os dois jogaram PAPEL <<<"
        return resultado
    elif num == 3 and jogada == 3:
        resultado = "\n>>> EMPATE!! Os dois jogaram TESOURA <<<"
        return resultado
    
    # COMPARANDO PEDRA COM PAPEL #
    if num == 1 and jogada == 2:
        resultado = ">>> VOCÊ GANHOU! Você jogou PAPEL e o seu oponete PEDRA <<<"
        return resultado
    
    # COMPARANDO PAPEL COM PEDRA #
    elif num == 2 and jogada == 1:
        resultado = "\n>>> VOCÊ PERDEU! Você jogou PEDRA e o seu oponete PAPEL <<<"
        return resultado
    
    # COMPARANDO PEDRA COM TESOURA #
    elif num == 1 and jogada == 3:
        resultado = "\n>>> VOCÊ PERDEU! Você jogou TESOURA e o seu oponete PEDRA <<<"
        return resultado
    
    # COMPARANDO TESOURA COM PEDRA #
    elif num == 3 and jogada == 1:
        resultado = "\n>>> VOCÊ GANHOU! Você jogou PEDRA e o seu oponete TESOURA <<<"
        return resultado
    
    # COMPARANDO PAPEL COM TESOURA #
    elif num == 2 and jogada == 3:
        resultado = "\n>>> VOCÊ GANHOU! Você jogou TESOURA e o seu oponete PAPEL <<<"
        return resultado
    
    # COMPARANDO TESOURA COM PAPEL #
    elif num == 3 and jogada == 2:
        resultado = "\n>>> VOCÊ PERDEU! Você jogou PAPEL e o seu oponete TESOURA <<<"
        return resultado
    
## MENU ENTRADA ##
print("➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢")
print("BEM-VINDO(A) AO JOKENPÔ")
print("➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢\n")

print("Digite um dos números a seguir para escolher entre PEDRA, PAPEL ou TESOURA: \n1 ⇝ PEDRA 🤜\n2 ⇝ PAPEL ✋\n3 ⇝ TESOURA 🤞\n\n--- BOA SORTE ---")
## FIM MENU ENTRADA ##

## DADOS INICIAIS ##
jogada = int(input("Digite o número: "))
num = random.randint(1, 3) # Gera um número entre 1 e 3 ou conforme o paramerto adicionado.
## FIM DADOS INICIAIS ##

sleep(1)
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ\n")

## CHAMANDO A FUNÇÃO ##
jogar = Jogo(num, jogada)
print(jogar)

