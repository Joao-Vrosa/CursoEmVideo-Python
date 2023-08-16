'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

temp = list() # Lista temporaria para armazenar os dados iniciais
dados_pessoas = list()

maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    
    if len(dados_pessoas) == 0: # Verificando menor e maior idade
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    
    dados_pessoas.append(temp[:]) # Fazendo uma copia dos dados iniciais
    temp.clear()
    
    continuar = str(input('Quer continuar [S/N]? '))
    if continuar in 'Nn':
        break


print(f'Dados {dados_pessoas}')
print(f'Foram cadastradas {len(dados_pessoas)} pessoas')

# Maior peso:
print(f'Maior peso: {maior}, de ', end='')

for peso_pessoas in dados_pessoas:
    if peso_pessoas[1] == maior:
        print(f'[{peso_pessoas[0]}] ', end='')

# Menor peso:
print(f'\nMenor peso: {menor}, de ', end='')

for peso_pessoas in dados_pessoas:
    if peso_pessoas[1] == menor:
        print(f'[{peso_pessoas[0]}] ', end='')

