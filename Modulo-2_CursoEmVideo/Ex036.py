vCasa = float(input("Qual o valor da casa? "))
vSalario = float(input("Qual o valor do seu salario? "))
qtdAnos = int(input("Em quantos anos você vai pagar? "))
print("\n")

meses = qtdAnos * 12
valorParcela = vCasa / meses
s = vSalario + (30/100 * vSalario) - vSalario

if valorParcela > s:
    print("-=-=-=-=-=-=-=-=-=-")
    print("Empréstimo NEGADO!")
    print("-=-=-=-=-=-=-=-=-=-")
    print("O valor da Parcela é 30% ou mais do seu salário")
    
else:
    print("-=-=-=-=-=-=-=-=-=-")
    print("Empréstimo ACEITO!")
    print("-=-=-=-=-=-=-=-=-=-")
    print("Valor da parcela mensal: {:.2f}".format(valorParcela))
    print("Este valor foi dividido em {} meses.".format(meses))

