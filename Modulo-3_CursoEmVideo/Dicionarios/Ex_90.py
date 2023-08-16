"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

dados = dict()

dados['nome'] = str(input('Nome do Aluno: '))
dados['media'] = float(input('Media do Aluno: '))

# Verificando situacao do aluno:
if dados['media'] >= 7:
    dados['situacao'] = str('APROVADO')
elif dados['media'] <= 5:
    dados['situacao'] = str('REPROVADO')
else:
    dados['situacao'] = str('RECUPERCAO')

print('\n>>> Dados do Aluno <<<')
for chave, valor in dados.items():
    print(f'{chave.capitalize()} do Aluno: {valor}')
