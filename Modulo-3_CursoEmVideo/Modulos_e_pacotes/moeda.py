
def aumentar(n=0):
    valor = n * (10/100)
    novo_valor = n + valor
    return novo_valor


def diminuir(n=0, taxa=0):
    valor = n * (taxa / 100)
    novo_valor = n - valor
    return novo_valor


def dobro(n=0):
    valor = n * 2
    return valor


def metade(n=0):
    valor = n / 2
    return valor


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.', ',')
