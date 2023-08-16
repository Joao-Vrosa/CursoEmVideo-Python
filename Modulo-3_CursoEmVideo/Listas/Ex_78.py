'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

valores = []

for i in range(0, 5):
    numeros = int(input("Digite um valor: "))
    valores.append(numeros)
    
    
print(f'\nMaior valor digitado foi {max(valores)}, na posicao {valores.index(max(valores))}\nMenor valor digitado foi {min(valores)}, na posicao {valores.index(min(valores))}')

