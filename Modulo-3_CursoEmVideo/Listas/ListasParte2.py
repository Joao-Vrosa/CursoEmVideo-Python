'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

# Listas soa mutáveis

dados = list()
dados.append('Joao')
dados.append(22)

pessoas = list()
pessoas.append(dados[:])  # Fazendo uma cópia
dados[0] = 'Emilly'
dados[1] = 19
pessoas.append(dados[:])
print(pessoas)

