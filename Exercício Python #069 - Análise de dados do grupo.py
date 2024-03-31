"""Exercício Python #069 - Análise de dados do grupo"""
"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
"""
-------------------------
   CADASTRE UMA PESSOA
-------------------------
Idade: 20
Sexo: [M/F] M
-------------------------
Quer continuar? [S/N] N
====== FIM DO PROGRAMA =======
Total de pessoas com mais de 18 anos: 1
Ao todo temos 1 homens cadastrados
E temos 0 mulheres com menos de 20 anos
"""

exercicio = 'Exercício #069'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

frase = 'CADASTRE UMA PESSOA'
print(f'-' * 25 + f'\n' + f'{frase:^25}' + f'\n' + f'-' * 25)

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
