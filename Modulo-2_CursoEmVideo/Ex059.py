from time import sleep

## FUNÇÕES ##
def Soma(N1, N2):
    soma = N1 + N2
    resul = '\nA soma de {} e {} é {}'.format(N1, N2, soma)
    return resul
    
def Multiplicar(N1, N2):
    mult = N1 * N2
    resul = '\nA multiplicação de {} e {} é {}'.format(N1, N2, mult)
    return resul
    
def Maior(N1, N2):
    if N1 > N2:
        maior = '\nO valor {} é maior!'.format(N1)
        return maior
    elif N1 < N2:
        maior = '\nO valor {} é maior!'.format(N2)
        return maior
## FIM - FUNÇÕES ##

## VALORES INICIAIS ##
print("\n     --- VALORES ---")
N1 = float(input("Digite o primeiro valor: "))
N2 = float(input("Digite o segundo valor: "))

opcao = 0
while opcao != 5:
    ## MENU ##
    sleep(2)
    print("\nEscolha uma da opções abaixo:\n \n[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa \n")

    opcao = int(input("Digite a opção desejada: "))
    ## FIM - MENU ##

    if opcao == 1:       
        somar = Soma(N1, N2) # CHAMANDO FUNÇÃO
        print(somar)
        
    elif opcao == 2:
        mult = Multiplicar(N1, N2) # CHAMANDO FUNÇÃO
        print(mult)
        
    elif opcao == 3:
        maior = Maior(N1, N2) # CHAMANDO FUNÇÃO
        print(maior)
        
    elif opcao == 4:
        print("\n--- NOVOS VALORES ---")
        N1 = float(input("Digite o primeiro valor: "))
        N2 = float(input("Digite o segundo valor: "))
        
    elif opcao == 5:
        print("\nSaindo do programa...")
        sleep(3)

