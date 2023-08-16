nome = input("Qual é o seu nome? ")

if nome == 'Joao':
    print("Que nome bonito!")
elif nome == 'Emilly' or 'Arthur':
    print("Top")
elif nome in 'Ricardo Ju Adriano':
    print('Lindoo')
else:
    print('Massa!')

print("Tenha um bom dia {}!".format(nome))