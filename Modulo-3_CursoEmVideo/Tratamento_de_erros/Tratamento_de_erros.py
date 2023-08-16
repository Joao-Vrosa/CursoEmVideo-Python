"""
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
Aprenda como usar a estrutura try except no Python de uma forma simples.
"""

"""
--> Estrutura padrão:

try:
    Operação
except:
    Falhou
else:
    Deu certo
finally:
    Certo/Falha (Vai aparecer de qualquer forma.)

"""
# --> Exemplo pratico <--

try:
    a = int(input('Numero: '))
    b = int(input('Numero: '))
    r = a / b
except Exception as erro:
    print('Ops... Algo deu errado :(')
    print(f'O problema foi: {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que voce digitou.')
except ZeroDivisionError:
    print('Não e possível dividir um número por ZERO.')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte Sempre!')
