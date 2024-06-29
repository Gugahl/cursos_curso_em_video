"""Desafio #078"""
"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

desafio = "Desafio #078"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

valores = []
for c in range(0, 5):
    num = int(input(f"Digite um valor para a posição {c}: "))
    valores.append(num)

num_maior = num_menor = num = 0
i_maior = i_menor = f' '
for i, num in enumerate(valores):
    if i == 0:
        num_menor = num
        i_menor = i

    if num == num_menor:
        i_menor = f'{i_menor}'
        i_menor += f'e {i} '

    if num == num_maior:
        i_maior = f'{i_maior}'
        i_maior += f'e {i} ' 

    if num > num_maior:
        num_maior = num
        i_maior = f'{i} '

    if num < num_menor:
        num_menor = num
        i_menor = f'{i} '


print(f"""
A lista foi {valores}
O maior valor foi {num_maior}, pego nas posições {i_maior}
O menor valor foi {num_menor}, pego nas posições {i_menor}
""")
