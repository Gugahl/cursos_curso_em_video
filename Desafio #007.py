"""DESAFIO 007"""
"""
Desenvolva um programa que leia as notas de um aluno, calcule e mostre sua média.
"""

# Boletim eletrônico do CEC

desafio = ' DESAFIO 007 '
print(f'{desafio:=^30}')

print('Boletim eletrônico do CEC')
prova = float(input('Qual foi sua nota na prova? '))
atvdds = float(input('Quantas atividades você fez (0 a 5)? '))
simulado = float(input('Qual foi sua nota no simulado? '))

print(f'Ok, você tirou {prova} pontos na prova bimestral, fez {atvdds} das cinco atividades do bimestre'
      f' e tirou {simulado} pontos no simulado bimestral'
      f'\n Então sua média do primeiro bimestre vai ser: {(prova+(simulado+(atvdds*0.6)))/2}')

print(' ')

# Boletim eletrônico do IFAL

desafio = ' DESAFIO 007 '
print(f'{desafio:=^30}')

print('Boletim eletrônico do IFAL')
print('Nota do quarto bimestre')
p4 = float(input('Qual foi sua nota na prova bimestral? '))
comciencias = float(input('Qual foi sua nota no comciências? '))

print(f'Ok, você tirou {p4} pontos na prova bimestral e tirou {comciencias} pontos no evento comciências \n'
      f'Então sua média do quarto bimestre vai ser: {(p4+comciencias)/2}')
