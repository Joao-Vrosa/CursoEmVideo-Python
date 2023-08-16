reta1 = float(input("Digite o valor da reta: "))
reta2 = float(input("Digite o valor da reta: "))
reta3 = float(input("Digite o valor da reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Forma triangulo!")
else:
    print("Não forma triangulo!")