n = []

for i in range(6):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        n.append(numero)
        num = sum(n)

print("\nA soma de todos os números pares é: {}".format(num))

