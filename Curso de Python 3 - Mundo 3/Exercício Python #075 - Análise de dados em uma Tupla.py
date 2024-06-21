"""Exercício Python #075 - Análise de dados em uma Tupla"""
"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor?

C) Quais foram os números pares
"""

exercicio = "Exercício #075"
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)


num = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

print(f"Você digitou os números {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}ª posição")
else:
    print(f"O valor 3 não foi digitado")
print("Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end='')
