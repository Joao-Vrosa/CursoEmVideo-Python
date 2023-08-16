## UTILIZANDO MODULOS ##

import math # Biblioteca de matematica.

num = int(input("Digite um número: "))
raiz = math.sqrt(num) # SQRT verifica a RAIZ.

print("A raiz de {} é igual a {:.2}".format(num, raiz)) # Normal
print("A raiz de {} é igual a {}".format(num, math.ceil(raiz))) # CEIL arredonda um número para cima.
print("A raiz de {} é igual a {}".format(num, math.floor(raiz))) # FLOOR arrenda para baixo.

