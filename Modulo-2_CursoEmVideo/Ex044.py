print("\n=== BEM-VINDO(A) AS LOJAS ROSA ===\n")

vProduto = int(input("Qual o valor do produto? R$"))

print("\n=== FORMAS DE PAGAMENTO ===")
print("[ 1 ] À VISTA - Dinheiro / Cheque - 10% de DESCONTO")
print("[ 2 ] À VISTA NO CARTÃO - 5% de DESCONTO")
print("[ 3 ] 2x CARTÃO - Preço Normal")
print("[ 4 ] 3x CARTÃO - 20% JUROS")
print("===========================\n")

pagamento = int(input(("Qual será a forma de pagamento? ")))

if pagamento == 1:
    vProduto = vProduto - (vProduto * 10/100)
    print("O valor total é {}".format(vProduto))

elif pagamento == 2:
    vProduto = - (vProduto * 5/100)
    print("O valor total é {}".format(vProduto))

elif pagamento == 3:
    print("O valor total é {}".format(vProduto))
    
elif pagamento == 4:
    vProduto = vProduto + (vProduto * 20/100)
    print("O valor total é {}".format(vProduto))

print("\n===========================")

