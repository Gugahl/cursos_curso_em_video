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

desafio = 'Desafio #069'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

frase = 'CADASTRE UMA PESSOA'
print(f'-' * 25 + f'\n' + f'{frase:^25}' + f'\n' + f'-' * 25)

bandeira = True
pessoas = maiores_de_idade = homens = mulheres_menores_de_20 = 0
while bandeira:
   print(f'-' * 25)
   idade = int(input('Idade: '))
   sexo = ' '
   while sexo not in 'MF':
      sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
   pessoas += 1
   if idade >= 18:
      maiores_de_idade += 1
   if sexo == 'M':
      homens += 1
   if sexo == 'F' and idade < 20:
      mulheres_menores_de_20 += 1
   print(f'-' * 25)
   continuar = ' '
   while continuar not in 'SN':
      continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
   if continuar == 'N':
      bandeira = False
fim = ' FIM DO PROGRAMA '
print(f'{fim:=^30}' + f'\n')
print(f'Total de {pessoas} pessoas' if pessoas > 1 else f'Total de {pessoas} pessoa'
      + f'\n' + f'Total de pessoas com mais de 18 anos: {maiores_de_idade}')
if homens == 0:
   print(f'Não tem homens cadastrados')
elif homens == 1:
   print(f'Tem somente {homens} homem cadastrado')
elif homens > 1:
   print(f'Ao todo temos {homens} homens cadastrados')
if mulheres_menores_de_20 == 0:
   print(f'E não tem mulheres com menos de 20 anos cadastradas')
elif mulheres_menores_de_20 == 1:
   print(f'E temos {mulheres_menores_de_20} mulher com menos de 20 anos cadastrada')
elif mulheres_menores_de_20 > 1:
   print(f'E temos {mulheres_menores_de_20} mulheres com menos de 20 anos')
