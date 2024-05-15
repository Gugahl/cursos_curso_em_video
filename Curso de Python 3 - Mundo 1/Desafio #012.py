"""DESAFIO 012"""
"""
Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

desafio = ' DESAFIO 012 '
print(f'{desafio:=^30}')
print('\n+55 82 4002-8922: Bom dia amigo!\n'
      '+55 82 4002-8922: Sou um empreendedor e estou para colocar uma promoção em toda a loja, preciso de um algorítmo '
      'em que eu forneça \no preço atual do produto, a margem de desconto e ele devolva já com o preço promocional '
      'com o desconto.\n'
      '+55 82 4002-8922: Você consegue fazer isso(Sim ou Não)?')
print(' ')

r = input('Você: ').lower()

if r == 'sim':
    print('Você: Consigo sim!\n'
          'Você: Só um momento\n'
          'Você: Aqui desconto.exe\n'
          ' \n')

    promo = 'Promoção'
    print(f'{promo:=^26}')

    nome = input('Qual é o nome do produto? ').title()
    di = float(input('Quanto será a porcentagem de desconto dada (0 a 100)? '))
    vi = float(input('Qual o valor do produto? R$'))
    df = di / 100
    vf = vi - (vi * df)
    igual = '=' * 25

    print(f' \n'
          f'{igual}\n'
          f'{nome:^25}\n'
          f'{igual}\n'
          f'A porcentagem de desconto foi de {di}%\n'
          f'O preço original foi: R${vi}\n'
          f'O preço na promoção será: R${vf:.2f}')

elif r == 'não':
    print('+55 82 4002-8922: Tudo bem amigo eu entendo, vou procurar outra pessoa, valeu!')
# Desculpa eu precisava fazer isso HAHAHA!
else:
    print('+55 82 4002-8922: 4002, 8922, É O FUNK DO YUDI QUE VAI DAR PLAYSTATION DOIS!!')
