"""DESAFIO 013"""
from time import sleep
"""
Faça um algorítmo que leio o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

desafio = ' DESAFIO 013 '
print(f'{desafio:=^30}\n')

e = 'EMPRESÁRIO'
o = 'online'
d = 'digitando...'

print(f'{e:^30}')
sleep(1)
print(f'{o:^30}')
sleep(1)
print(f'{d:^34}\n')
sleep(2)
print(f'Empresário: Bom dia amigo!')
sleep(2)
print(f'Empresário: Vou precisar de mais um trabalho seu hehe!')
sleep(4)
print(f'Empresário: Dessa vez vou precisar de um algorítmo em que eu forneça o salário de um funcionário\n'
      'e uma porcentagem para um aumento salarial, preciso que o algorítmo leia o salário original a\n'
      'porcentagem de aumento e o salário pós aumento.')
sleep(2)
print('Empresário: E então, você acha que consegue?(Sim ou Não)\n')
sleep(2)
r = (input('Você: ')).lower()

if r == 'sim':
    print('Você: Bom dia!')
    sleep(1)
    print('Você: Eu vou tentar')
    sleep(1)
    print('Você: Só um momento.')
    sleep(1)
    print('Você: Aqui está amigo!')
    sleep(1)
    print('Você: Abrir salario.exe\n')
    sleep(1)
    salario = ' Reajuste Salarial da Empresa '
    print(f'{salario:=^44}\n')
    sleep(1)
    n = input('Qual o nome do funcionário? ').title()
    si = float(input('Quanto esse funcionário ganha atualmente? R$'))
    pori = float(input('Quantos % de aumento você deseja dar ao funcionário? '))

    porf = pori/100
    sf = si + (si * porf)

    print(' ')
    print(f'O salário de {n} era de R${si}, depois de um aumento de {pori}% o salário passou a ser R${sf:.2f}')

elif r == 'não':
    print('Empresário: Tudo bem então, vou procurar outra pessoa, bom dia!')

else:
    print('Empresário: Irrelevante, responda minha pergunta.')
