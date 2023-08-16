"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

dados = dict()
cadastros = list()
soma = 0

while True:
    dados['nome'] = str(input('Nome: '))

    # Validando Entrada 'sexo'
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while dados['sexo'] not in 'MF':
        print('[ERRO] Valor Invalido! Responda com M ou F.', end=' ')
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    ##

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']

    cadastros.append(dados.copy())  # Fazendo uma cópia, para os dados nao se sobreporem.

    # Validando Entrada continuar
    continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    while continuar not in 'SN':
        print('[ERRO] Valor Invalido! Responda com S ou N.', end=' ')
        continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]

    if continuar in 'Nn':
        break
    ##

media = soma / len(cadastros)

print('=-' * 30)

print(f'A) Foi cadastrado {len(cadastros)} pessoa(s)')
print(f'B) A média de idades e {media}')

# Verificando todas as mulheres cadastradas
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoas in cadastros:
    if pessoas['sexo'] == 'F':
        print(f'{pessoas["nome"]} ', end='')
##

# Verificando todas as pessoas a cima da média
print(f'\nD) As pessoas com a idade a cima da média foram: ', end='')
for pessoas in cadastros:
    if pessoas['idade'] > media:
        print(f'{pessoas["nome"]} ', end='')
##
