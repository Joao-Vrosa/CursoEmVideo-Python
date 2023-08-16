'''
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''


tupla = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')

while True:
    num = int(input("Digite um numero: "))
    
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end='') ## end= | Nao pula de linha
    
print(f'Voce digitou o numero {tupla[num]}')

