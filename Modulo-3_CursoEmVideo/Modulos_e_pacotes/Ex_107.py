"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from moeda import aumentar, diminuir, dobro, metade


num = float(input('Digite um valor R$'))

print(aumentar(num))
print(diminuir(num, 20))
print(dobro(num))
print(metade(num))
