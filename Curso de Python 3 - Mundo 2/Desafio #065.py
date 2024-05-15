"""Desafio #065"""
"""
Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O
programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""

desafio = 'Desafio #065'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

usuario = int(input('Digite um valor inteiro: '))
quantidade_de_valores = 1
soma_de_valores = usuario
maior_valor = usuario
menor_valor = usuario
media = soma_de_valores / quantidade_de_valores
continuar = str(input('Você deseja continuar?(S/N) ')).upper()
while continuar == 'S':
    usuario = int(input('Digite um valor inteiro: '))
    quantidade_de_valores += 1
    soma_de_valores += usuario
    if maior_valor < usuario:
        maior_valor = usuario
    if menor_valor > usuario:
        menor_valor = usuario
    media = soma_de_valores / quantidade_de_valores
    continuar = str(input('Você deseja continuar?(S/N) ')).upper()
if continuar == 'N':
    if quantidade_de_valores == 1:
        print(f'Você digitou {quantidade_de_valores} valor, sendo ele o maior e menor valor, por não ter outra referência.'
            f'\nA média foi: {media}.')
    if quantidade_de_valores > 1:
        print(f'Você digitou {quantidade_de_valores} valores, sendo o maior valor {maior_valor} e o menor valor {menor_valor}.'
            f'\nA média entre esses {quantidade_de_valores} valores foi: {media}.')
