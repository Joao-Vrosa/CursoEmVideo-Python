n = int(input("Digite um número: "))

for i in range(1, 11):
    calc = n * i
    print("{} x {:2} = {}".format(n, i, calc))

