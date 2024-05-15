"""DESAFIO 020"""
from random import sample
from time import sleep
from random import shuffle
"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

# Truque do sample

desafio = ' Desafio #020 '
print(f'{desafio:=^30}\n')

prof = 'Professor Thiago'
on = 'online'
digi = 'digitando...'
print(f'{prof:^30}')
sleep(1)
print(f'{on:^30}')
sleep(1)
print(f'{digi:^30}', '\n')

sleep(1)
print('Professor Thiago: Olha eu de novo!')
sleep(2)
print('Professor Thiago: Agora preciso de um programa em que eu insira o nome de quatro alunos e ele embaralhe\n'
      'esses quatro, me fornecendo uma sequência.')
sleep(1)
res = input('Professor Thiago: Você acha que consegue(sim ou não)?\n'
            '\n'
            'Dev: ').lower()

if res == 'sim':
    sleep(1)
    print('Dev: Consigo sim! Só um momento...')
    sleep(1)
    print('Dev: Aqui está professor (abrir sequência.exe)\n')
    sleep(2)

    programa = 'Gerador de Sequências'
    print('=' * 30, f'\n{programa:^30}')
    print('=' * 30, '\n')
    print('Ok, me forneça o nome de quatro alunos.')
    aluno1 = input('Qual é o nome do primeiro aluno? ').title()
    aluno2 = input('Qual é o nome do segundo aluno? ').title()
    aluno3 = input('Qual é o nome do terceiro aluno? ').title()
    aluno4 = input('Qual é o nome do quarto aluno? ').title()
    lista = [aluno1, aluno2, aluno3, aluno4]
    sequencia = sample(lista, k=len(lista))
    sleep(2)
    print(f'Ok, a ordem de apresentação se dará por {sequencia}.')

elif res == 'não':
    sleep(1)
    print('Dev: Infelizmente não vai dar professor.')
    sleep(1)
    print('Professor Thiago: Tudo bem, fica para a próxima então, muito obrigado.')
    sleep(2)
    print('Bad Ending')

else:
    sleep(1)
    print('Professor Thiago: Irrelevante, responda da maneira solicitada.')

# Com o shuffle

desafio = 'DESAFIO 020'
print('=' * 30, '\n', f'{desafio:^30}')
print('=' * 30, '\n')

prof = 'Professor Thiago'
on = 'online'
digi = 'digitando...'
print(f'{prof:^20}')
print(f'{on:^20}')
print(f'{digi:^20}', '\n')

print('Professor Thiago: Bom dia Dev!')
sleep(2)
print('Professor Thiago: Vou precisar dos seus serviços novamente')
sleep(2)
print('Professor Thiago: Você consegue criar um aplicativo em que eu insira o nome de quatro alunos\n'
      'e ele crie uma lista com esses nomes em ordem aleatória(sim ou não)?', '\n')
sleep(1)
res = input('Dev: ').lower()
sleep(1)

if res == 'sim':
    print('Dev: Consigo sim professor!')
    sleep(1)
    print('Dev: Só um momentinho...')
    sleep(3)
    print('Dev: Aqui está abrir lista_sorteada.exe', '\n')
    sleep(2)

    app = 'SORTEIO'
    print('=' * 20, '\n', f'{app:^20}')
    print('=' * 20, '\n')
    primeiro_aluno = input('Qual é o nome do primeiro aluno? ').title()
    segundo_aluno = input('Qual é o nome do segundo aluno? ').title()
    terceiro_aluno = input('Qual é o nome do terceiro aluno? ').title()
    quarto_aluno = input('Qual é o nome do quarto aluno? ').title()
    grupo = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
    shuffle(grupo)
    print(f'A ordem de apresentação será {grupo}.')

elif res == 'não':
    sleep(2)
    print('Dev: Infelizmente não vai dar professor.')
    sleep(2)
    print('Professor Thiago: Tudo bem, fica para a próxima então, muito obrigado.')
    sleep(1)
    print('Bad Ending')

else:
    sleep(1)
    print(' ')
    print('Professor Thiago: Irrelevante, responda da maneira solicitada.')
