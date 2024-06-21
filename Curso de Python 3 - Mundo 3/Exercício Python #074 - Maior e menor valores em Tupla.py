"""Exercício Python #074 - Maior e menor valores em Tupla"""
from random import randint
"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

exercicio = "Exercício #074"
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os valores sorteados foram: ", end='')
for n in numeros:
    print(f"{n} ", end='')
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
