from curses.ascii import alt


peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso / altura ** 2


if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25:
    print("PESO IDEAL")
elif imc >= 25 and imc < 30:
    print("SOBREPESO")
elif imc >= 30 and imc < 40:
    print("OBESIDADE")
elif imc > 40:
    print("OBESIDADE MÓRBIDA")

print("O seu IMC é de {:.2f}".format(imc))

