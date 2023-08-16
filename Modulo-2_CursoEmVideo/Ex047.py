from time import sleep

for i in range(1, 50+2, 1):
    if i % 2 == 0:
        sleep(0.500)
        print(i, "É PAR")

