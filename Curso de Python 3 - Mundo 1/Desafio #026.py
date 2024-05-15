"""Desafio 026"""
"""
Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A";
> Em que posição ela aparece pela primeira vez;
> Em que posição ela aparece pela última vez.
"""

desafio = ' Desafio #026 '
print(f'{desafio:=^30}', '\n')

frase = input('Me forneça uma frase: ').strip()
frase1 = frase.lower()
print(f'A letra A aparece {frase1.count("a")} vezes na frase.')
print(f'A letra A aparece pela primeira vez na posição {frase1.find("a") + 1}.')
print(f'A letra A aparece pela última vez na posição {frase1.rfind("a") + 1}.')
