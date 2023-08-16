"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno 
individualmente.
"""

ficha = []

while True:
    nomeAluno = str(input('Nome: '))
    notaUm = float(input('Nota 1: '))
    notaDois = float(input('Nota 2: '))

    media = (notaUm + notaDois) / 2

    ficha.append([nomeAluno, [notaUm, notaDois], media])  # Lista composta

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-=' * 30)

print(f'{"ID.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 25)

for indice, aluno in enumerate(ficha):  # Montando tabela com os alunos e media
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:  # Verificando as notas por aluno, individualmente
    opcao = int(input('Digite o ID do aluno para ver as suas notas: [999 para sair] '))

    if opcao == 999:
        print('FINALIZANDO...')
        break

    if opcao < len(ficha):
        print('-' * 15)
        print(f'>>> As notas de {ficha[opcao][0]} sao {ficha[opcao][1]}')
    else:
        print('[ERRO] ID de aluno nao encontrado')
