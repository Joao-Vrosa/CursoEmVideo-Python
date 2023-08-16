"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogador = dict()
golsCampeonato = list()
time = list()
partidas = list()
qtdPartidas = 0

while True:
    jogador.clear()  # Para nao repetir os valores
    partidas.clear()  # Para nao repetir os valores
    jogador['nome'] = str(input('Nome: '))
    qtdPartidas = int(input(f'Quantidade de partidas que {jogador["nome"].capitalize()} jogou: '))

    # Verificando a quantidade de gols por partida
    for i in range(0, qtdPartidas):
        partidas.append(int(input(f'Quantidade de gols na {i + 1}º partida: ')))

    jogador['gols_por_partida'] = partidas[:]
    jogador['gols_totais'] = sum(partidas)
    # Fim

    time.append(jogador.copy())

    # Verificando se deseja continuar
    while True:
        continuar = str(input('Deseja continuar? ')).upper()[0]
        if continuar in 'SN':
            break
        print('[ERRO] Responda somente com S ou N!')
    if continuar in 'N':
        break
    # Fim


# Resultado:
print('=-' * 30)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for chave, valor in enumerate(time):
    print(f'{chave:>3} ', end='')
    for d in valor.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
# Fim

# Verificando detalhes por jogador
while True:
    detalhes_jogador = int(input('Voce deseja ver os detalhes de qual jogador? (999 para parar) '))

    # Saindo do programa
    if detalhes_jogador == 999:
        print('<<< Fechando programa >>>')
        break
    # FIm

    # Verificando se o código do jogador existe
    if detalhes_jogador > len(time):
        print(f'[ERRO] Nao existe jogador com código {detalhes_jogador}')
    # Fim

    # Resultado, demonstrando detalhes do jogador selecionado
    else:
        print(f'>>> Levantamento do jogador {time[detalhes_jogador]["nome"]} <<<')
        for i, g in enumerate(time[detalhes_jogador]['gols_por_partida']):
            print(f'{i + 1}º partida -> {g} gols')
    print('-' * 40)
    # Fim
# Fim
