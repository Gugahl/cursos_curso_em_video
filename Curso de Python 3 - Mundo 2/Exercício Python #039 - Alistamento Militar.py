"""Desafio #039"""
from datetime import datetime, date
from math import floor
"""
Faça um programa que leia o ano de nascimento de um jovem
e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

exercicio = 'Exercício #039'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

homem_ou_mulher = str(input('Você é homem ou mulher? ')).lower()

if homem_ou_mulher == 'mulher':
    print('Mulheres não podem se alistar, bote as mãos para o céu e agradeça.')

elif homem_ou_mulher == 'homem':
    nome_do_candidato = str(input('Qual é o seu primeiro nome? ')).lower().title()
    dia_do_nascimento = int(input('Qual foi o dia do seu nascimento(1 a 31)? '))
    mes_do_nascimento = int(input('Qual foi o mês do seu nascimento(1 a 12)? '))
    ano_de_nascimento = int(input('Em qual ano você nasceu? '))

    # Transformando as informações coletadas do nascimento em data para o Python
    data_de_nascimento = datetime(day=dia_do_nascimento, month=mes_do_nascimento, year=ano_de_nascimento)
    # Data atual já formatada para o Python
    data_atual = datetime.now()
    # Diferença de dias, horas, minutos e segundos entre uma data e outra
    idade_do_candidato = data_atual - data_de_nascimento
    # Ano do alistamento militar
    ano_do_alistamento = ano_de_nascimento + 18
    # Se acaso você ainda não tiver no ano do alistamento, essa variável mostra quantos anos faltam para o ano do
    # alistamento
    anos_que_faltam = ano_do_alistamento - date.today().year
    # Essa variável encontra o primeiro espaço da variável que mostra o tempo de uma data a outra
    espaco = str(idade_do_candidato).find(' ')
    # Essa variável mostra somente quantos dias existem entre uma data e outra
    dias_de_vida_bruto = int(str(idade_do_candidato)[:espaco])
    # Essa variável mostra somente quantos anos completos existem entre uma data e outra
    anos_de_vida = dias_de_vida_bruto // 365
    # Essa variável mostra os dias entre uma data e outra, tirando os dias contados pela última variável
    dias_de_vida_sem_anos = dias_de_vida_bruto % 365
    # Essa variável mostra os meses completos entre uma data e outra usando a última variável como início
    meses_de_vida = floor(dias_de_vida_sem_anos / 30.4167)
    # Essa variável mostra os dias entre uma data e outra tirando anos completos e meses completos
    dias_de_vida_liquido = floor(dias_de_vida_sem_anos % 30.4167)
    # Essa variável mostra quantos anos você deveria ter se alistado subtraindo do ano atual, o ano que você deveria ter
    # se alistado, se acaso você tiver passado do ano de alistamento.
    qts_anos_que_deveria_ter_se_alistado = date.today().year - ano_do_alistamento

    if date.today().year - ano_de_nascimento < 18:
        print(f'\n'
              f'Seu nome é {nome_do_candidato};\n'
              f'Você tem: {anos_de_vida} anos, {meses_de_vida} meses\n'
              f'e {dias_de_vida_liquido} dias;\n'
              f'Você ainda não chegou no ano de se alistar no serviço militar;\n'
              f'Ainda faltam {anos_que_faltam} anos para o seu alistamento no serviço militar;\n'
              f'Seu alistamento será em {ano_do_alistamento}.')

    elif date.today().year - ano_de_nascimento == 18:
        print(f'\n'
              f'Seu nome é {nome_do_candidato};'
              f'Você tem: {anos_de_vida} anos, {meses_de_vida} meses\n'
              f'e {dias_de_vida_liquido} dias;\n'
              f'Você chegou no ano de se alistar no serviço militar, dirija-se à Junta de Serviço Militar\n'
              f'mais próxima até o dia 31/06/{date.today().year}.')

    else:
        print(f'\n'
              f'Seu nome é {nome_do_candidato};\n'
              f'Você tem: {anos_de_vida} anos, {meses_de_vida} meses e {dias_de_vida_liquido} dias;\n'
              f'Já passou do ano de você se alistar, você deveria\nter se alistado há '
              f'{qts_anos_que_deveria_ter_se_alistado} anos atrás, no ano de {ano_do_alistamento}.')
