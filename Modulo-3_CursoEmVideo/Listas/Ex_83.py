'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

abre_parenteses = []
fecha_parenteses = []

expressao = str(input('Digite a sua expressao: '))

for i in expressao:
    if i == '(':
        abre_parenteses.append(i)
    elif i == ')':
        fecha_parenteses.append(i)
        
if len(abre_parenteses) == len(fecha_parenteses):
    print('Expressao valida!')
else:
    print('Expressao invalida!')

