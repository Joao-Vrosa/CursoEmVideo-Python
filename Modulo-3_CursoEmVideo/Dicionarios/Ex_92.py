"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS diferir de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime


dados = dict()

dados['nome'] = str(input('Nome: '))
# Verificando idade:
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento  # Verificando a idade, ano atual menos o ano de nascimento.
dados['carteira'] = int(input('Carteira de Trabalho (0 se nao tem): '))

if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Ano de Contratacao: '))
    dados['salario'] = float(input('Salario: R$'))
    # Verificando com quantos anos ira se aposentar:
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('\n>>> Dados:')

for chave, valor in dados.items():
    print(f'{chave.capitalize()}: {valor}')
