"""Desafio #056"""
"""
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres tem menos de 20 anos.
"""

desafio = ' Desafio #056 '
print(f'{desafio:=^30}', '\n')
soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
contagem_mulheres_menos_20_anos = 0

for pesquisa in range(1, 5):
    nome = str(input('Me informe seu nome: ')).lower()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Você é homem ou mulher: ')).lower()
    print(' ')
    soma_idades += idade
    if sexo == "homem" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == "mulher" and idade < 20:
        contagem_mulheres_menos_20_anos += 1
media_idade = soma_idades / 4

print(f'\n'
        f'A média de idade do grupo foi de: {media_idade} anos.\n'
        f'O nome do homem mais velho é: {nome_homem_mais_velho.title()}\n'
        f'Existem {contagem_mulheres_menos_20_anos} mulheres com menos de 20 anos.')