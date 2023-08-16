a = input("Digite algo: ")

print("O tipo primitivo deste valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print("É número? ", a.isalpha())
print("É alfa númerico? ", a.isalnum())
print("Está em maiúsculas?, ", a.isupper())
print("Está em minúsculas?, ", a.islower())
print("Está capitalizada? ", a.istitle()) # Se possui letras minusculas e maiusculas.
