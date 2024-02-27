"""Desafio #040"""
"""
Crie um programa que leia duas notas de um aluno e calcule sua média mostrando
uma mensagem no final de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO
"""

desafio = ' Desafio #040 '
print(f'{desafio:=^30}')
print(' ')

primeiro_bimestre = float(input('Qual foi sua nota no primeiro bimestre? '))
segundo_bimestre = float(input('Qual foi sua nota no segundo bimestre? '))
media = (primeiro_bimestre + segundo_bimestre) / 2

print(' ')
print(f'Sua média foi {media}.')
if media >= 7:
    print('\033[32mParabéns!\033[m Você foi aprovado!')

elif media > 5 < 7:
    print('\033[33mAlerta!\033[m Você ainda não foi aprovado, mas poderá ter uma chance na recuperação.')

elif media < 5:
    print('\033[31mÉ uma pena!\033[m Você não conseguiu nota o suficiente para poder ir para a recuperação\n'
          'e irá ser reprovado.')
