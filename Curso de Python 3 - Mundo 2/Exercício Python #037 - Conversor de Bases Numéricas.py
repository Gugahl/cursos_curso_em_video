"""Desafio #037"""
"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

exercicio = 'Exercício #036'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

numero_escolhido = int(input('Digite um número inteiro: '))
print(' ')
tabela_de_conversao = ('Escolha uma base numérica para converter o seu número:\n'
                       '(lembrando que seu número já está na base decimal)\n'
                       'Digite 1 se quiser converter para a BASE BINÁRIA;\n'
                       'Digite 2 se quiser converter para a BASE OCTAL;\n'
                       'Digite 3 se quiser converter para a BASE HEXADECIMAL.\n')
escolha_de_conversao = int(input(f'{tabela_de_conversao}\nVocê: '))

if escolha_de_conversao == 1:
    base_binaria = bin(numero_escolhido)[2:]
    print(f'O número {numero_escolhido} convertido para a base binária é igual a: {base_binaria}.')

elif escolha_de_conversao == 2:
    base_octal = oct(numero_escolhido)[2:]
    print(f'O número {numero_escolhido} convertido para a base octal, é igual a: {base_octal}.')

elif escolha_de_conversao == 3:
    base_hexadecimal = hex(numero_escolhido)[2:].upper()
    print(f'O número {numero_escolhido} convertido para a base hexadecimal, é igual a: {base_hexadecimal}.')

else:
    print('Opção inválida. Tente novamente.')