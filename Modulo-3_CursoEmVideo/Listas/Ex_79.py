'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

valores = []

for i in range(0, 5):
    numerosDigitados = int(input("Digite um valor: "))
    
    while numerosDigitados in valores:
        print("O número", numerosDigitados, "ja foi cadastrado, Tente novamente! ", end='')
        numerosDigitados = int(input("Digite um valor: "))
        
    if numerosDigitados not in valores:
        valores.append(numerosDigitados)
        print("Novo número cadastrado com sucesso!")
        

print(f'\nValores digitados: {sorted(valores)}')

