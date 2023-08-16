"""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar
nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote,
ampliando ainda mais a modularização em grandes projetos em Python.
"""

# Foco Modularizacao: Dividir um programa grande, aumentar a legibilidade, facilitar a manutenção

""" Vantagens da Modularizacao:
- Organizacao do código
- Facilita manutenção do código
- Ocultação do código detalhado
- Reutilização em outros projetos
"""

# import uteis as ut  # Importando as funcoes de outro arquivo
# O modulo e UTEIS e as funcoes sao FATORIAL, DOBRO e TRIPLO
from uteis import numeros  # Importando pacotes


# Programa principal ->
num = int(input('Digite um numero: '))

# Fatorial
fat = numeros.fatorial(num)
print(f'O fatorial de {num} e {fat}')

# Dobro
dob = numeros.dobro(num)
print(f'O dobro de {num} e {dob}')

# Triplo
tri = numeros.triplo(num)
print(f'O triplo de {num} e {tri}')
