"""Desafio #083"""
"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

desafio = f'Desafio #083'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15)

expressao = input('Digite a expressão: ')
parenteses = []
for char in expressao:
    if char == '(':
        parenteses.append(char)
    elif char == ')':
        if len(parenteses) == 0:
            False
        parenteses.pop()

if len(parenteses) == 0:
    print(f'A expressão {expressao} está correta!')
else:
    print(f'A expressão {expressao} está faltando parênteses, revise ela.')
