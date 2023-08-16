num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

lista = []

lista.append(num1)
lista.append(num2)
lista.append(num3)

lista.sort()

print("O maior número é {} e o menor é {}".format(lista[2], lista[0]))

