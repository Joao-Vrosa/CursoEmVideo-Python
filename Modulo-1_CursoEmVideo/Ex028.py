import random

print('-=-' * 20)
print("Vou pensar em um número de 0 a 5, tente adivinhar...")
print('-=-' * 20)

nUsuario = int(input("Digite um número entre 0 e 5: "))

num = random.randint(0, 5) # Vai sortear um número de 0 a 5(ou conforme parametro)

if nUsuario == num:
    print("Parabens, você ganhou!")
else:
    print("Você errou, tente novamente!")

