"""Desafio #074"""
from random import randint
"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

desafio = "Desafio #074"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

num1, num2, num3, num4, num5 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
tupla = (num1, num2, num3, num4, num5)
print(f"A tupla gerada foi {tupla}")
tupla = sorted(tupla)
print(f"O menor valor gerado foi {tupla[0]}, já o maior valor gerado foi {tupla[-1]}")
