'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

listaProdutos = ("Banana", 2.50, "Maça", 2.00, "Pera", 3.00, "Uva", 4.00, "Morando", 5.50)

print(36 * '-')
print(f'{"LISTAGEM DE PREÇOS":^36}') # Centralizando o texto (^36).
print(36 * '-')

for posicao in range(0, len(listaProdutos)):
    if posicao % 2 == 0: # Itens nas posições pares.
        print(f'{listaProdutos[posicao]:.<30}', end='') # Alinhando o texto a esquerda com os pontos (:.<30).
    else: # Valores nas posições impares.
        print(f'R${listaProdutos[posicao]:>.2f}') # Alinhando o texto a direita com os pontos (:>) e colocando dois digitos apos a virgula (.2f).

print(36 * '-')

