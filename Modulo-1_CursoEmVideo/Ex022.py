nome = input("Digite seu nome: ").strip() # Retira os espaços do começo e do final.

print("Analisando o seu nome...")

print("Seu nome em maiusculo é {}".format(nome.upper()))
print("Seu nome em minusculo é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))

