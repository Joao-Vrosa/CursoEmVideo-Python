num = int(input("Digite um número: "))

if num % 2 != 0:
    if num % num == 0 and num % 1 == 0:
        print("O numero {} é um número primo!".format(num))
else:
    print("O número {} não é um numero primo!".format(num))

