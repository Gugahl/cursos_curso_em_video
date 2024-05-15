"""Desafio #034"""
"""
Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00 calcule um aumento de 10%.

Para salários inferiores ou iguais o aumento é de 15%.
"""

desafio = ' Desafio #034 '
print(f'{desafio:=^30}', '\n')

sal = 'Aumento'

print('=' * 30)
print(f'{sal:^30}')
print('=' * 30)

print('Gerente Jeff: Bom dia Lucas!')
print('Gerente Jeff: O patrão pediu para falar com você sobre o aumento')
print('Gerente Jeff: Qual é o seu salário mesmo para eu calcular o seu aumento?')
print(' ')
salario = float(input('Lucas: Bom dia Jeff! Meu salário é R$'))

print(f'Gerente Jeff: Ótimo Lucas, seu salário é R${salario}, a partir desse mês terá um acréscimo de R${salario/10}\n'
      f'correspondente a 10% do seu salário atual e ficará no valor de R${salario+(salario/10)}'
      if salario > 1250.0 else f'Gerente Jeff: Ótimo Lucas, seu salário é R${salario}, a partir desse mês terá um '
                               f'acréscimo de R${(salario/100)*15}\ncorrespondente a 15% do seu salário atual e ficará'
                               f' no valor de R${salario+((salario/100)*15)}')
