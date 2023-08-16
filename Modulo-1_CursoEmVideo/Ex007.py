nome = input("Digite o seu nome: ")

n1 = int(input("Digite a sua primeira nota: "))
n2 = int(input("Digite a sua segunda note: "))

media = (n1 + n2) / 2

print("Olá, {}".format(nome))
print("A sua média é {}".format(media))

if media >= 6:
    print("Aprovado!")

else:
    print("Reprovado!")

