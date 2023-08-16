'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

nomeProduto = ''
valorProduto = 0

totalCompra = 0
produtoMaisMil = []
valores = []

opcao = ''

while True:
    nomeProduto = str(input("Nome do produto: "))
    valorProduto = float(input("Valor do produto: "))
    
    valores.append(valorProduto)
    
    totalCompra = totalCompra + valorProduto
    
    if valorProduto > 1000:
        produtoMaisMil.append(valorProduto)
        
    opcao = str(input("Quer continuar [S/N]? ")).upper()
    
    if opcao != 'S':
        break
    
print(f'\nTotal: R${totalCompra:.2f}\nProdutos custando mais de mil: {len(produtoMaisMil)}\nProduto mais barato: R${min(valores):.2f}\n')

