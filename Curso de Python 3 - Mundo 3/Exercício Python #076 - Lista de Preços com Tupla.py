"""Exercício Python #076 - Lista de Preços com Tupla"""
"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.

No final mostre uma listagem de preços organizando os dados em forma tabular.
"""

exercicio = "Exercício #076"
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)

listagem = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

print('-' * 30)
print(f'{"Listagem de preços":^30}')
print('-' * 30)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

