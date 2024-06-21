"""Desafio #076"""
"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.

No final mostre uma listagem de preços organizando os dados em forma tabular.
"""

desafio = "Desafio #076"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

tupla = (f"Arroz", 3.5, f"Feijão", 5, f"Coca Cola 2L", 8, f"Picanha", 39)

print("-=" * 20)
nome, preco = "Nome", "Preço"
print(f"{nome:<30}{preco:>10}")
print("-=" * 20)
for c in range(0, len(tupla), 2):
    print(f"{tupla[c]:.<30}R${tupla[c + 1]:>8.2f}")
print("-=" * 20)