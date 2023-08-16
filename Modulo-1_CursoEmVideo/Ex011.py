from curses.ascii import alt


largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altua da parede: "))

area = largura * altura
tinta = area / 2
 
print("Para uma parede de {}x{} a sua área é de {}.".format(largura, altura, area))
print("Para pintar a parede, você precisará de {} litros de tinta".format(tinta))

