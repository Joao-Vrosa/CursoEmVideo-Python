import math

angulo = float(input("Digite o valor do ângulo: "))

# É necessario converter o valor para RADIANOS utilizando o método RADIANS
seno = math.sin(math.radians(angulo)) # SIN = calcula o SENO
cosseno = math.cos(math.radians(angulo)) # COS = calcula o COSSENO
tangente = math.tan(math.radians(angulo)) # TAN = calcula a TANGENTE

print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))

