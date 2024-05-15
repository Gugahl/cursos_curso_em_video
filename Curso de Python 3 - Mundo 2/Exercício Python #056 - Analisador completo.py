"""Desafio #056"""
"""
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres tem menos de 20 anos.
"""

exercicio = ' Exercício #056 '
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

soma_das_idades = 0
media_das_idades = 0
idade_do_homem_mais_velho = 0
nome_do_homem_mais_velho = 0
total_de_mulheres_com_menos_de_20_anos = 0
for pessoa in range(1, 5):
    texto = f' {pessoa}ª PESSOA '
    print(f'{texto:-^30}')
    nome = str(input('Qual é o seu nome? ')).strip().lower().title()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Você é homem ou mulher? ')).strip().lower()
    soma_das_idades += idade
    if pessoa == 1 and sexo == 'homem':
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
    if idade > idade_do_homem_mais_velho and sexo == 'homem':
        idade_do_homem_mais_velho == idade
    if sexo == 'mulher' and idade < 20:
        total_de_mulheres_com_menos_de_20_anos += 1
media_das_idades = soma_das_idades / 4
print(' ')
print(f'A média de idade do grupo é de {media_das_idades} anos.')
print(f'O homem mais velho tem {idade_do_homem_mais_velho} anos e seu nome é {nome_do_homem_mais_velho}.')
print(f'Ao todo são {total_de_mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos.')