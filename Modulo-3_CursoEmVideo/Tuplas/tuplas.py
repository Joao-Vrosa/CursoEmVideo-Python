'''
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

lanches = ('Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Maneira simples de percorrer os valores de uma tupla
for comida in lanches:
    print(f'Eu vou comer {comida}')
    
for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]}, que esta na posição {cont}')
    
for posicao, comida in enumerate(lanches):
    print(f'Eu vou comer {comida}, que esta na posição {posicao}')

