'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

lista = []
opcao = "S"

media = soma = menorNum = maiorNum = 0

while opcao == "S":
    num = int(input("Digite um numero: "))
    opcao = str(input("Quer continuar S/N? ")).upper() # upper - Transforma as letras digitadas em maiuscula
    
    lista.append(num) # append - Adiciona o valor de num na lista
    
    
soma = sum(lista) # sum - Soma todas as posições da lista
media = soma / len(lista) # len - Quantidade de posições da lista
menorNum = min(lista) # min - Menor valor da lista
maiorNum = max(lista) # max - Maior valora da lista

print("\nSoma dos numeros digitados: {}\nMedia: {:.2f}\nMenor numero: {}\nMaior numero: {}".format(soma, media, menorNum, maiorNum))

