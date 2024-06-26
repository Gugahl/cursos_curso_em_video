"""Exercício Python #077 - Contando vogais em Tupla"""
"""
Crie um programa que tenha uma tupla com várias palavras (não use acentos).

Depois disso você deve mostrar para cada palavra quais são as suas vogais.
"""

exercicio = "Exercício #077"
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
