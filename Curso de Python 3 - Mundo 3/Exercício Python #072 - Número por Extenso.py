"""Exercício Python #072 - Número por Extenso"""
"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
"""

exercicio = "Exercício #072"
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)

cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end='')
print(f'Você digitou o número {cont[num]}')
