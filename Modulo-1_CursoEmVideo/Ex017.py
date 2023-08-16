import math

cOposto = float(input("Quanto mede o cateto oposto? "))
cAdjacente = float(input("Quanto mede o cateto adjacente? "))

# Como fazer sem a biblioteca MATH
hipotenusa = (cOposto ** 2 + cAdjacente ** 2) ** (1 / 2)

# Como fazer com a biblioteca MATH
hipotenusa_2 = math.hypot(cOposto, cAdjacente)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))

print("A hipotenusa vai medir {:.2f}".format(hipotenusa_2))

