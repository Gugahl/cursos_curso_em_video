"""Desafio 024"""
"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""
desafio = ' Desafio #024 '
print(f'{desafio:=^30}', '\n')

cidade = input('Qual é o nome da cidade? ').title()
cid_splitada = cidade.split()
primeiro_cidade = cid_splitada[0]

if 'Santo' in cidade:

    if 'Santo' in primeiro_cidade:
        print(f'O nome da cidade é: {cidade}, ela tem Santo no nome e começa com Santo.')
    else:
        print(f'O nome da cidade é: {cidade}, ela tem Santo no nome, porém não começa com Santo.')

else:
    print(f'O nome da cidade é: {cidade}, e ela não tem Santo no nome.')
