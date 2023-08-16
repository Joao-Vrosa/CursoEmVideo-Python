'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
par = []
valores = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))

# Verifica se ha numero 9.
print(f'\nO numero 9 apareceu {valores.count(9)} vezes. ')
    
# Verifica se ha numero 3.
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posicao {valores.index(3)}.')
else:
    print('Nao foi digitado o numero 3')

# Verifica se ha numeros pares.
for i in valores:
    if i % 2 == 0:
        par.append(i)

print(f'Numeros pares: {par}')

