"""Desafio #077"""
"""
Crie um programa que tenha uma tupla com várias palavras (não use acentos).

Depois disso você deve mostrar para cada palavra quais são as suas vogais.
"""

desafio = "Desafio #077"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

tupla = ("Programa", "Site", "Aplicativo", "Computador")

for palavra in tupla:
    vogais = ""
    for letra in palavra:
        if letra.lower() in "aeiou":
            vogais += letra + " "
    print(f"Na palavra '{palavra.upper()}' temos: {vogais}")
