from datetime import date

maior = []
menor = []

for i in range(7):
    anoNascimento = int(input("Digite o ano do seu nascimento: "))
    
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    
    if idade < 18:
        menor.append(idade)
    elif idade >= 18:
        maior.append(idade)

print("\n{} pessoas são menores de idade!".format(len(menor)))
print("{} pessoas são maiores de idade!".format(len(maior)))

