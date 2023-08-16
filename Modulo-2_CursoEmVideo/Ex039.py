from datetime import date

sexo = str(input("Qual o seu sexo(M/F): ")).upper().strip()

if sexo == 'F':
    print("Você é mulhur, o alistamento não é obrigatório.")
    exit()

anoNascimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = date.today().year # Verifica o ano atual
idade = anoAtual - anoNascimento

if sexo == 'M':
    if idade == 18:
        print("Você tem {} anos, está na hora de se alisatar.".format(idade))
        
    elif idade < 18:
        print("Você ainda não precisa se alistar.")
        
        c = idade
        f = 0
        while c < 18:
            f = f + 1
            c = c + 1
        print("Faltam {} anos para você poder se alistar".format(f))
        
    else:
        print("Opa! Já passou da hora de se alistar, você tem {} anos".format(idade))

