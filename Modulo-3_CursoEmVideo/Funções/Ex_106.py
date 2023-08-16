"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
cores = ('\033[m',         # 0 - Sem cor
         '\033[0;30;41m',  # 1 - Vermelho
         '\033[0;30;42m',  # 2 - Verde
         '\033[0;30;43m',  # 3 - Amarelo
         '\033[0;30;44m',  # 4 - Azul
         '\033[0;30;45m',  # 5 - Roxo
         '\033[7;30m'      # 6 - Branco
)


def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO \'{com}\'', 4)
    print(cores[3], end='')
    help(com)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)
    print(cores[0], end='')


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)
