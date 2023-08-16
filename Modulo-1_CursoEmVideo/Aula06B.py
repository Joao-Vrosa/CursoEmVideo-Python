from __future__ import print_function



# Converte o número digitado para FLOAT
n = float(input("Digite um valor inteiro para ele ser convertido para float: "))
print(n)


print("====================")
# Verifica se o que foi digitado é númerico ou não
n = input("Digite algo para verificar se ele é númerico: ")
print(n.isnumeric())

print("====================")
# Verifica se o que foi digitado é letra ou não
n = input("Digite algo ara verificar se ele é letra: ")
print(n.isalpha())

print("====================")
# Verifica se o que foi digitado é alfa númerico ou não
n = input("Digite algo para verificar se ele é alfa númerico: ")
print(n.isalnum())

