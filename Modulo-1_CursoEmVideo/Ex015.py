km = float(input("Digite a quantidade de KM percorrido: "))
dia = int(input("Quantos dias ele ficou alugado? "))

vDia = dia * 60
vKm = km * 0.15
total = vDia + vKm

print("O carro foi alugado por {} dia(s) e rodou {}KM, sendo assim o valor total é de R${:.2f}".format(dia, km, total))

