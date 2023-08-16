"""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.
"""

# Interactive Help - Funcao interna do Python - help() - Exibe a ducumentacao de outras funcoes

# DOCSTRINGS - E uma documentacao - Cada funcao interna do Python tem a sua DOCSTRING


def contador(inicio, fim, passo):  # Cirando uma DOCSTRING/documentacao para a funcao contador()
    """
    > Recebe 3 parametros e escreve na tela a contagem.
    :param inicio - Inicio da contagem;
    :param fim - Fim da contagem;
    :param passo - Passo da contagem;
    :return: sem retorno;
    Funcao criada por Joao V. Rosa
    """
    c = inicio
    while c <= fim:
        print(f'{c} ', end='')
        c += passo
    print('FIM!')


contador(2, 10, 2)
help(contador)
# ===============================================


def somar(a=0, b=0, c=0):  # Parametros opcionais
    """
    > Somar até 3 valores. Caso nao seja inserido um dos valores, ele sera ZERO, por padrão
    :param a: Valor A
    :param b: Valor B
    :param c: Valor C
    :return: Sem retorno
    Funcao criada por Joao V. Rosa
    """
    s = a + b + c
    # print(f'A soma vale {s}')
    return s


"""
somar(2, 4, 6)
somar(2, 4)
"""

respostaUm = somar(2, 4, 8)
respostaDois = somar(2, 6)

print(f'Os resultados foram {respostaUm} e {respostaDois}')
