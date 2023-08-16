from time import sleep

soma = 0

for i in range(1, 500, 1):
    if i % 2 != 0:
        if i % 3 == 0:
            soma = soma + i
            sleep(0.100)
            print(i, "È IMPAR E DIVISIVÉL POR TRÊS")
            
print("\nA soma de todos os número é de {}".format(soma))

