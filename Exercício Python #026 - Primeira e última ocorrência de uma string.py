"""Desafio 026"""
"""
Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra A;
> Em que posição ela aparece pela primeira vez;
> Em que posição ela aparece pela última vez;
"""

exercicio = 'Exercício #026'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

frase = input('Me forneça uma frase: ').lower()
print(f'A letra "A" aparece {frase.count("a")} vezes.')
print(f'A primeira vez que a letra "a" aparece é na {frase.find("a") + 1}ª posição.')
print(f'A última vez que a letra "a" aparece é na {frase.rfind("a") + 1}ª posição.')
