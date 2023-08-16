'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('JOAO', 'EMILLY', 'ARTHUR', 'GABA', 'LENA')

vogais = ('A', 'E', 'I', 'O', 'U')

vogaisPorNome = []

for nome in palavras:
    for letra in nome:
        if letra in vogais:
            vogaisPorNome.append(letra)
    print(f'As vogais do nome {nome} são: {vogaisPorNome}')
    vogaisPorNome = []
