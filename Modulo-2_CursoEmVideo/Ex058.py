import random

print('-=-' * 18)
print("Vou pensar em um número de 0 a 10, tente adivinhar...")
print('-=-' * 18)

c = 0
QtdJogadas = 0

while c == 0:
    QtdJogadas += 1 # Contador de jogadas
    nUsuario = int(input("Digite um número entre 0 e 10: "))
    
    num = random.randint(0, 10) # Vai sortear um número de 0 a 10(ou conforme parametro)
    
    if nUsuario > 10 or nUsuario < 0:
        print("Número invalido, tente novamente!")
        print("-=-" * 10)

    elif nUsuario == num:
        print("Parabens, você ganhou!")
        c += 1
    else:
        print("Você errou, tente novamente!")
        print("-=-" * 10)

print("Foram {} rodas necessárias para finalizar o jogo!".format(QtdJogadas))

