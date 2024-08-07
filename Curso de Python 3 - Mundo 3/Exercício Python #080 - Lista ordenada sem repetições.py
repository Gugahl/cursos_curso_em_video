"""Exercício Python #080 - Lista ordenada sem repetições"""
"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final mostre a lista ordenada na tela.
"""

exercicio = f'Exercício Python #080'
print(f'=~' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'~=' * 15)

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            lista.insert(pos, n)
            print(f'Adicionando na posição {pos} da lista...')
            break
        pos += 1
print('~=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
