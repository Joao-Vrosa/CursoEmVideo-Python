'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''

mult = 0

while True:
    print("=" * 41)
    num = int(input("Digite um número para ver a seua tabuada: "))
    print("=" * 41)
    
    if num < 0:
        break
        
    for i in range(1, 11):
        mult = i * num
        saida = "{} X {} = {}".format(i, num, mult)
        print(saida)

