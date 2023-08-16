somaIdade = 0
mediaIdade = 0
maiorIdadeH = 0
nomeVelho = ''

tMulher20 = 0

for i in range(1, 5):
    print("---- {}° PESSOA ----".format(i))
    nome = str(input("Digite o seu nome: "))
    idade =  int(input("Digite a sua idade: "))
    sexo = str(input("Digite o seu sexo(M/F): "))
    
    somaIdade += idade
    
    if i == 1 and sexo in 'Mm':
        maiorIdadeH = idade
        nomeVelho = nome
    elif sexo in 'Mn' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeVelho = nome
        
    elif sexo in 'Ff' and idade < 20:
        tMulher20 += 1
        
mediaIdade = somaIdade / 4

print("A média de idade do grupo é de {} anos.".format(mediaIdade))
print("O homem mais velho se chama {} e tem {} anos.".format(nomeVelho, maiorIdadeH))
print("São {} mulheres com menos de 20 anos". format(tMulher20))

