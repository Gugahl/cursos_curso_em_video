"""Desafio #060"""
"""
Faça um programa que leia um número
qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
"""

desafio = 'Desafio #060'
print(f'=-' * 30 + f'\n' + f'{desafio:^60}' + f'\n' + f'=-' * 30)

valor = int(input('Digite um valor inteiro: '))
valor_inicial = valor
fatorial = valor
while valor > 1:
    valor -= 1
    fatorial *= valor
print(f'O fatorial de {valor_inicial} é igual a {fatorial}.')


"""Com for"""
"""
numero = int(input("Digite um número para calcular o fatorial: "))
antecessores = ""
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
    if i != 1:
        antecessores += " x " + str(i)
print(str(numero) + ' = ' + antecessores[::-1] + '1' + " = " + str(fatorial))
"""
