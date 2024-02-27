"""Desafio #034"""
"""
Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00 calcule um aumento de 10%.

Para salários inferiores ou iguais o aumento é de 15%.
"""

exercicio = ' Exercício #034 '
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 10 / 100)

print(f'Quem ganhava R${salario} agora esta ganhando R${novo:.2f}.')
