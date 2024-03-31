"""Desafio #065"""
"""
Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O
programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""

exercicio = 'Exercício #065'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
