"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

dados = dict()
golsPartida = 0
golsCampeonato = list()


dados['nome'] = str(input('Nome: '))
dados['partidas'] = int(input('Quantidade de partidas: '))

for i in range(0, dados['partidas']):
    golsPartida = int(input(f'Quantidade de gols na {i+1}º partida: '))
    golsCampeonato.append(golsPartida)

dados['gols_por_partida'] = golsCampeonato
dados['gols_totais'] = sum(golsCampeonato)

print('=-' * 25)
for chave, valor in dados.items():
    print(f'>>> {chave.capitalize()}: {valor}')
