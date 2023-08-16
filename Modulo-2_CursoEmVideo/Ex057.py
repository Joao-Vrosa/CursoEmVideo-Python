c = 0

while c == 0:
    sexo = str(input("Digite seu sexo[F/M]: ")).upper().strip()[0]
    # UPPER vai deixar a letra em maiusculo, STRIP retira os espaços
    # e [0] para pegar somente a primeira letra 
    # caso o usuário coloque a palavra inteira "Masculino" ou "Feminino".
    
    if sexo != 'F' and sexo != 'M':
        print("[ERRO] Tente novamente!")
    else:
        print("Sexo cadastrado com sucesso!")
        c += 1

