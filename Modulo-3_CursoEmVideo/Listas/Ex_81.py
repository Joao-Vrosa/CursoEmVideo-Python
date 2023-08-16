'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []
qtdNumCinco = 0

while True:
    valorAdd = int(input('Digitre um valor a ser adicionado: '))
    
    if valorAdd == 5:
        qtdNumCinco += 1
    
    valores.append(valorAdd)
    
    opcao = str(input('Quer ver o resultado [S/N]? '))
    
    if opcao in 'Nn':
        break
    

qtdValoresDigitados = len(valores)
valores.sort(reverse=True)

print(f'\nQuantidade de valores digitado: {qtdValoresDigitados}\nLista ordenada em forma decrescente: {valores}\nQuantidade de numeros cinco: {qtdNumCinco}')

