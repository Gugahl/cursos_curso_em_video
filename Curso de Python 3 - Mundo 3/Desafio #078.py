"""Desafio #078"""
"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

desafio = "Desafio #078"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

valores = []
cont = 0
imaior = f' '
imenor = f' '

while cont < 5:
    cont += 1
    num = int(input(f'Digite o {cont}º número: '))
    valores.append(num)
    if cont == 1:
        maior = menor = num
        imaior = imenor = f'{cont - 1}'
    else:
        if num > maior:
            maior = num
            imaior = f'{cont - 1}'
        elif num == maior:
            imaior += f', {cont - 1}'

        if num < menor:
            menor = num
            imenor = f'{cont - 1}'
        elif num == menor:
            imenor += f', {cont - 1}'

print(f"Você digitou {valores}")
print(f"O maior número computado foi {maior} na posição de índice {imaior};")
print(f"Já o menor número computado foi {menor} na posição de índice {imenor}.")
