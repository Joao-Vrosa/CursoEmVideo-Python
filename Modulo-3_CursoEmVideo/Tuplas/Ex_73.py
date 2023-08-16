'''
Exercício Python 73: 
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

tuplaTimes = ('Atime1','Btime2','Dtime3','Etime4','Ftime5','Gtime6','Htime7','Itime8','Chapecoense','Jtime10','Ktime11','Ltime12','Mtime13','Ntime14','Otime15','Ptime16','Qtime17','Rtime18','Stime19','Ttime20')

cincoPrimeiros = tuplaTimes[0:5]
ultimosQuatro = tuplaTimes[-4:]
ordemAlfabetica = sorted(tuplaTimes)
posicaoChape = tuplaTimes.index('Chapecoense') + 1

print(cincoPrimeiros)
print(ultimosQuatro)
print(ordemAlfabetica)
print(posicaoChape)

