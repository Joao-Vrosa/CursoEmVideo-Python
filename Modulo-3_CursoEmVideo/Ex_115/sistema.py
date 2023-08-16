"""
Exercício Python 115a: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples.
O sistema só vai ter 2 poções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from Ex_115.lib.interface import *
from Ex_115.lib.arquivo import *
from time import sleep

# Verificando se o arquivo existe
arq = 'arquivo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)
##

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('\033[94mNome: \033[0m'))
        idade = leiaInt('\033[94mIdade: \033[0m')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[93mSaindo do Sistema...\033[0m')
        break
    else:
        print('\033[91m[ERRO] Digite uma opção valida!\033[0m')
    sleep(2)
