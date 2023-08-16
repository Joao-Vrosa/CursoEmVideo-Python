nome = str(input("Digite o seu nome completo: ")).strip().title() # TITLE deixa a primeira letra das palavras maiusculas.
print("Muito prazer em te conhecer {}".format(nome))

n = nome.split() # SPLIT vai dividir as palavras

print("Seu primeiro nome é {}".format(n[0]))
print("Seu último nome é {}".format(n[len(n) - 1]))

