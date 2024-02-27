"""Desafio #036"""
from time import sleep
"""
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder 
30% do salário ou então o empréstimo será negado.
"""

desafio = ' Desafio #036 '
mcmv = 'CAIXA - Minha casa minha vida'
emprestimo = 'Adquira seu empréstimo e realize o sonho da casa nova!'
vazio = ' '

print(f'{vazio:^15}{desafio:=^30}{vazio:^15}')
sleep(3)

print(f'{mcmv:^60}')
print(f'{emprestimo:^60}')
sleep(3)

print(' ')
print(f'Consultor Caixa: Bom dia!')
sleep(1)
print(f'Consultor Caixa: Como eu te falei mais cedo na agência eu vou te ajudar a tirar o empréstimo.')
sleep(1)
print(f'Você: Bom dia. Muito obrigado!')
sleep(1)
print(f'Consultor Caixa: Primeiro vou precisar de alguns dados.')
sleep(1)
print(f'Consultor Caixa: Em primeiro momento preciso saber o valor da casa que você deseja tirar.')
valor = float(input(f'Você: Eu desejo tirar uma casa de R$'))
sleep(1)
print(f'Consultor Caixa: Ok, o valor do empréstimo será de R${valor}.')
sleep(1)
print(f'Consultor Caixa: Seguindo, qual o seu salário atual?\n'
      f'O sistema só aprova pessoas que ganham mais do que R$1420,00, salário mínimo.')
salario = float(input(f'Você: Meu salário atual está no valor de R$'))
sleep(1)
print(f'Consultor Caixa: Ok, seu salário é de R${salario}.')
sleep(1)
print(f'Consultor Caixa: E por último, gostaria de perguntar em quantos anos você deseja\n'
      f'estar efetuando o pagamento do empréstimo.')
anos = int(input(f'Você: '))
sleep(1)
print(f'Consultor Caixa: Pronto! Vou fazer a simulação aqui e já te falo se deu certo.')
sleep(3)

meses = anos * 12
prestacao_mensal = valor / meses


if salario < 1420:
    print(f'Consultor Caixa: \033[31mÉ uma pena!\033[m Não consegui aprovar, pois o sistema\n'
          f'só aprova para pessoas que ganham de um salário mínimo para cima.')

elif meses > 360:
    print(f'Consultor Caixa: \033[31mÉ uma pena!\033[m Não consegui, pois o sistema não\n'
          f'aprova empréstimos para mais de 30 anos.')

else:
    if prestacao_mensal <= (0.3 * salario):
        print(f'Consultor Caixa: \033[32mConseguimos!\033[m A prestação ficará no valor de R${prestacao_mensal:.2f}.\n'
              f'mensal, no período de {meses} meses, ou seja, {anos} anos.')

    elif prestacao_mensal > (0.3 * salario):
        print(f'Consultor Caixa: \033[31mÉ uma pena!\033[m Não consegui aprovar, pois a prestação mensal\n'
              f'excedeu 30% do seu salário, e o sistema não aceita.')
