"""Desafio #084"""
"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista.
No final mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com a(s) pessoa(s) mais pesada(s).

C) Uma listagem com as pessoas mais leves.
"""

desafio = f'Desafio #084'
print(f'=~' * 15 + f'\n' + f'{desafio:^30}' + f'\n' + f'~=' * 15 + f'\n')

pessoas = list()
auxiliar = list()
pesopesado = pesoleve = 0
nomepesado = nomeleve = f' '
total = contador = 0
while True:
    contador += 1
    if contador > 1:
        print(f' ')
    
    auxiliar.append(str(input(f'Qual é o seu nome? ')).capitalize())
    auxiliar.append(float(input(f'Quantos quilos você tem? ')))
    
    total += 1
    if contador == 1:
        nomepesado = auxiliar[0]
        pesopesado = auxiliar[1]
        nomeleve = auxiliar[0]
        pesoleve = auxiliar[1]
    
    elif auxiliar[1] > pesopesado:
        nomepesado = auxiliar[0]
        pesopesado = auxiliar[1]
    
    elif auxiliar[1] == pesopesado:
        nomepesado += f', {auxiliar[0]}'
    
    elif auxiliar[1] < pesoleve:
        nomeleve = auxiliar[0]
        pesoleve = auxiliar[1]
    
    elif auxiliar[1] == pesoleve:
        nomeleve += f', {auxiliar[0]}'
    
    pessoas.append(auxiliar[:])
    auxiliar.clear()
    
    pergunta = input(f'\nDeseja continuar? [S/N] ')[0].upper()
    while pergunta != 'S' and pergunta != 'N':
        print(f'\nERRO! Digite S ou N para escolher se deseja continuar!')
        pergunta = input(f'Deseja continuar? [S/N] ')[0].upper()
    if pergunta == 'N':
        break

print(f'\n{pessoas}')
print(f'Ao total foram computadas {total} pessoas.')
print(f'As pessoas mais pesadas foram {nomepesado} que pesam ambas {pesopesado} quilos.')
print(f'As pessoas mais leves foram {nomeleve} que pesam ambas {pesoleve} quilos.')
