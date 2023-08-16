from Ex_115.lib.interface import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[91m[ERRO] Houve um erro ao criar o arquivo {nome}\033[0m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[91mErro ao ler arquivo {nome}\033[0m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linhas in a:
            dados = linhas.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'\033[91m[ERRO] Houve um erro na abertura o arquivo {nome}\033[0m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[91m[ERRO] Houve um erro ao escrever os dados no arquivo {nome}\033[0m')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()
