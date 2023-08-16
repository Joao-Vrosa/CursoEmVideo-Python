num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
""")

opcao = int(input("Sua opção: "))

## BIN - Converte para BINÁRIO
if opcao == 1:
    print("O número {} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
## OCT - Converte para OCTAL
elif opcao == 2:
    print("O número {} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
## HEX - Converte para HEXADECIMAL
elif opcao == 3:
    print("O número {} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida!")

