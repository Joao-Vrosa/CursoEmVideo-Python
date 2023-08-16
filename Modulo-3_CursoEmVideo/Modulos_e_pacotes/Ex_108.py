"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
mostrar os números como um valor monetário formatado.
"""

import moeda


num = float(input('Digite um valor R$'))

print(f'O valor aumentado em 10%: {moeda.moeda(moeda.aumentar(num))}')
print(f'O valor diminuindo 10%: {moeda.moeda(moeda.diminuir(num))}')
print(f'O valor dobrado: {moeda.moeda(moeda.dobro(num))}')
print(f'O valor pela metade: {moeda.moeda(moeda.metade(num))}')
