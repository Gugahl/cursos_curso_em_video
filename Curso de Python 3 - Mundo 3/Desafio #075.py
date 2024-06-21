"""Desafio #075"""
"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor?

C) Quais foram os números pares
"""

desafio = "Desafio #075"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

pares = ' '
nove = 0
for i in range(4):
    numero = int(input("Digite um valor: "))
    if i == 0:
        tupla = (numero, )
        menor = numero
    if i > 0:
        tupla += (numero, )
    if numero % 2 == 0:
        pares += f"{numero} "
    if numero == 9:
        nove += 1
    if numero < menor:
        menor = numero

print(f"A tupla organizada ficou {sorted(tupla)}")
print(f"O valor 9 aparece {nove} vezes")
print(f"O primeiro valor foi {menor}, ele foi declarado na posição {tupla.index(menor)}")
print(f"Os número pares foram {pares}")
