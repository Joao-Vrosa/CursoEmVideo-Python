'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

idade = 0
sexo = ''

opcao = ''

pessoasMaioresDeIdade = []
homens = []
mulheres = []
mulheresMenosVinte = []


while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    
    if idade >= 18:
        pessoasMaioresDeIdade.append(idade)
    
    if sexo == 'M':
        homens.append(sexo)
        
    if sexo == 'F' and idade < 20:
        mulheresMenosVinte.append(sexo)
        
    opcao = str(input("Quer continuar [S/N]? ")).upper()
    
    if opcao != 'S':
        break

print(f'\nSão {len(pessoasMaioresDeIdade)} pessoas maiores de idade\nForam cadastrados {len(homens)} homens\nSão {len(mulheresMenosVinte)} mulheres com menos de 20 anos')

