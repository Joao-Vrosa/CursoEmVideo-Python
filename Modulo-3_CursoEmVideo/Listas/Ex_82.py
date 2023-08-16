'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

valores = []
valoresPares = []
valoresImpares = []

while True:
    valores.append(int(input('Valor: ')))
    
    opcao = str(input('Quer continuar [S/N]? '))
    
    if opcao in 'Nn':
        break
    
for i in valores:
    if i % 2 == 0:
        valoresPares.append(i)
    else:
        valoresImpares.append(i)
        
print(f'\nValores digitados: {valores}\nValores pares: {valoresPares}\nValores impares: {valoresImpares}')

