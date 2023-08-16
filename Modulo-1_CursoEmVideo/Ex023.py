numero = int(input("Digite um número: "))

if numero < 0 or numero > 9999:
    print("Número invalido!")
    exit()

print("Analisando o número {}".format(numero))

n = str(numero)

print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar; {}".format(n[0]))

