'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

somaPares = 0
somaColunaTres = 0
valoresLinhaDois = []
maiorValor = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Valor para [{linha},{coluna}]: '))

        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

        if coluna == 2:
            somaColunaTres += matriz[linha][coluna]
        if linha == 1:
            valoresLinhaDois.append(matriz[linha][coluna])
            maiorValor = max(valoresLinhaDois)

print()

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end="")
    print()

print()

# RESULTADO
print(f'A soma de todos os valores pares da matriz e: {somaPares}')
print(f'A soma dos valores da terceira coluna e: {somaColunaTres}')
print(f'O mair valor da segunda linha e {maiorValor}')
