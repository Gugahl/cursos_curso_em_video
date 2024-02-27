"""Desafio #036"""
"""
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder 
30% do salário ou então o empréstimo será negado.
"""

exercicio = 'Exercício #036'

print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

valor_da_casa = float(input('Qual é o valor da casa? R$'))
salario_do_comprador = float(input('Qual é o valor do seu salário atualmente? R$'))
anos_do_financiamento = int(input('Em quantos anos você deseja pagar esse financiamento? (número inteiro):'))

meses_do_financiamento = anos_do_financiamento * 12
prestacao_mensal_do_financiamento = valor_da_casa / meses_do_financiamento

if prestacao_mensal_do_financiamento > (0.3 * salario_do_comprador):
    print(f'Para pagar uma casa de R${valor_da_casa:.2f} em {anos_do_financiamento} anos, a prestação ficará no valor '
          f'de R${prestacao_mensal_do_financiamento:.2f}, que é mais do que 30% do seu salário.\n'
          f'\033[31mEmpréstimo NEGADO!\033[m')

elif prestacao_mensal_do_financiamento <= (0.3 * salario_do_comprador):
    print(f'Para pagar uma casa de R${valor_da_casa:.2f} em {anos_do_financiamento} anos, a prestação ficará no valor '
          f'de R${prestacao_mensal_do_financiamento:.2f}, que é menos de 30% do seu salário.\n'
          f'\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
