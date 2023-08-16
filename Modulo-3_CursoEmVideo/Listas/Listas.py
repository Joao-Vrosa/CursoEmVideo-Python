'''
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

lista = ['PAO', 'MANTEIGA', 'MORTANDELA', 'QUEJINHUNN']
print(f'Lista inicial: {lista}')

# Adicionando itens a lista:
lista.append('CARNINHA')
lista.append('SUCO DE MURUCUJA')
lista.append('PICOLE DE MAMAO')
print(f'Lista apos o append: {lista}')

# Adicionando item em posicoes especificas da lista:
lista.insert(0, 'OVO')
lista.insert(2, 'BANANA')
lista.insert(5, 'PAO')
print(f'Lista apos o insert: {lista}')

# Deletando item de posicao especifica da lista:
del lista[4]
print(f'Lista apos o del: {lista}')

# Deletando o ultimo item da lista:
lista.pop()
lista.pop(2) # O pop pode ser usado para deletar em posicoes especificas tambem.
print(f'Lista apos o pop: {lista}')

# Deletadno pelo valor e nao pelo indice(posicao). Como podemso observar ele remove apenas o primeiro item "PAO".
lista.remove('PAO')
print(f'Lista apos o remove: {lista}')

print(30 * '=-')

listaNumerica = list(range(0, 11)) # Cirado uma lista com valores de 0 a 10 com o metodo list.
print(f'Lista numerica: {listaNumerica}')

# Invertendo a ordem dos numeros da lista:
listaNumerica.sort(reverse=True)
print(f'Lista numerica apos o sort(reverse): {listaNumerica}')

# Ordenadno valores:
listaNumerica.sort()
print(f'Lista numerica apos o sort: {listaNumerica}')

# Obtendo o tamanho da lista:
print(f'Lista numerica apos o len: {len(listaNumerica)}')

print(30 * '=-')

valores = []

for i in range(0, 3):
    valores.append(int(input("Valor: ")))
    
for posicao, valor in enumerate(valores):
    print(f'Valor {valor} na posicao {posicao}')
    
print(30 * '=-')