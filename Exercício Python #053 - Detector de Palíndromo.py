"""Desafio #053"""
"""
Crie um programa que leia uma frase qualquer e diga se ela é um 
palíndromo, desconsidere os espaços.
"""

exercicio = ' Exercício #053 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

frase = str(input('Digite uma frase: ')).lower().strip()
print(' ')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

"""
Macete do fatiamento
frase = str(input('Digite uma frase: ')).lower().strip()
print(' ')
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
"""