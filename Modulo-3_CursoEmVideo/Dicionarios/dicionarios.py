"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.
"""

filme = {  # Sintaxe de dicionários em Python. Lembrando que poderia ser desta forma: filme = {'titulo': 'Star Wars',
    # 'ano': 1977, 'diretor': 'George Lucas'} ou podemos declarar dicionários desta forma: filme = dict()
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas',
}

print(filme.values())  # Retorna os valores do dicionario
print(filme.keys())  # Retorna as chaves
print(filme.items())  # Retorna os valores e as chaves

for chave, valor in filme.items():
    print(f'O {chave} e {valor}')

print('-=' * 35)

listaDeFilmes = [  # Podemos colocar dicionários dentro de listas
    {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
    {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
]

print(listaDeFilmes[0]['titulo'])
print(listaDeFilmes[1]['titulo'])

print('-=' * 35)

estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # Fazendo uma cópia para que nao sobreponha os valores adicionados

print(brasil)
