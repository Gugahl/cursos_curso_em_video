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

exercicio = 'Exercício #040'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print(f'Você tirou {media} pontos de média, infelizmente você não tem nota para fazer\n'
          f'uma recuperação, com isso você foi \033[31mREPROVADO!\033[m')

elif 5 < media < 7:
    print(f'Você tirou {media} pontos de média, felizmente você tem nota para fazer a\n'
          f'\033[33mRECUPERAÇÃO!\033[m')

else:
    print(f'Você tirou {media} pontos de média, \033[32mPARABÉNS!\033[m Você foi \033[32mAPROVADO!\033[m')
