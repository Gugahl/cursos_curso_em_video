"""Exercício Python #079 - Valores únicos em uma Lista"""
"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.
"""

exercicio = f'Exercício Python #079'
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)

números = []
while True:
    n = int(input(f'Digite um valor: '))
    if n not in números:
        números.append(n)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    r = str(input(f'Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

print('~=' * 30)
números.sort()
print(f'Você digitou os valores: {números}')
