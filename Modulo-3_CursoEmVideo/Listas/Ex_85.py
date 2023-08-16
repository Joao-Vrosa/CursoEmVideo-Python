'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

num = 0
valores = [[], []]

for i in range(0, 7):
    num = (int(input('Valor: ')))
    
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)


valores[0].sort()
valores[1].sort()

print(f'Valores pares: {valores[0]}')
print(f'Valores impares: {valores[1]}')

