p = []

for i in range(5):
    peso = float(input("Digite o seu peso: "))
    
    p.append(peso)
    
print("\nO maior peso lido foi de {}Kg".format(max(p)))
print("O menor peso lido foi de {}Kg".format(min(p)))

