"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""


def notas(*n, sit=False):
    notas_alunos = dict()
    notas_alunos['total'] = len(n)
    notas_alunos['maior'] = max(n)
    notas_alunos['menor'] = min(n)
    notas_alunos['media'] = sum(n) / len(n)
    if sit:
        if notas_alunos['media'] >= 7:
            notas_alunos['situacao'] = 'BOA'
        elif notas_alunos['media'] >= 5:
            notas_alunos['situacao'] = 'RAZOAVEL'
        else:
            notas_alunos['situacao'] = 'RUIM'

    return notas_alunos


# Programa principal
resp = notas(5.5, 10, 3.5, 8.5, sit=True)
print(resp)
