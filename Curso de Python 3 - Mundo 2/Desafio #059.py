"""Desafio #059"""
"""
Crie um programa que leia dois valores e mostre um menu
na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em
cada caso.
"""

desafio = 'Desafio #059'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

menu = f"[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n"
numero_1 = float(input(f'Me forneça um valor: '))
numero_2 = float(input(f'Me forneça outro valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input(f'Escolha um número do menu para fazer uma das operações declaradas:\n'
                        f'{menu}\n'
                        f'Você: '))
    if escolha == 1:
        soma = numero_1 + numero_2
        print(f'A soma entre {numero_1} e {numero_2} é igual a: {soma}.\n')
    if escolha == 2:
        multiplicação = numero_1 * numero_2
        print(f'A multiplicação entre {numero_1} e {numero_2} é igual a: {multiplicação}.\n')
    if escolha == 3:
        if numero_1 > numero_2:
            print(f'O número {numero_1} é o maior.\n')
        if numero_2 > numero_1:
            print(f'O número {numero_2} é o maior.\n')
        if numero_1 == numero_2:
            print(f'Os números são iguais.\n')
    if escolha == 4:
        print('Me informe os números novamente.')
        numero_1 = float(input(f'Me forneça o primeiro valor: '))
        numero_2 = float(input(f'Me forneça o segundo valor: '))
    if escolha > 5:
        print(f'Digite um número válido.\n')
