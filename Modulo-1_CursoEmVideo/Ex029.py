vel = float(input("Digite a velocidade do carro: "))

vMax = 80
vMin = 50
multa = 7

if vel > vMax:
    print("Você ultrapassou a velocidade maxima e foi multado!")
    multado = (vel - 80) * multa
    print("Sua multa é de R${}".format(multado))
else:
    print("Dentro da velocidade permitida! Continue sua viagem.")