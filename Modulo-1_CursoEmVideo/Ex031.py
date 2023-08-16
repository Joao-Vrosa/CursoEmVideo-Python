viagem = float(input("Digite a distancia da viagem em KM: "))

if viagem > 200:
    total = viagem * 0.45
else:
    total = viagem * 0.50

print("Valor total da viagem: R${:.2f}".format(total))