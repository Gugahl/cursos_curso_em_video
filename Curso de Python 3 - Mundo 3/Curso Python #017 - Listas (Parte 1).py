"""
Variáveis Compostas (Listas)
        Parte 01

Eu preciso guardar diversos valores em uma variável;
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche[2])
pizza

lanche[3] = 'picolé'
lanche = ['hamburguer', 'suco', 'pizza', 'picolé']
Listas são mudáveis

lanche.append('cookie')
lanche = ['hamburguer', 'suco', 'pizza', 'picolé', 'cookie']

lanche.insert(0, 'cachorro quente')
lanche = ['cachorro quente', 'hamburguer', 'suco', 'pizza', 'picolé', 'cookie']

del lanche[3] # Remove pelo índice
lanche.pop(3) # Remove pelo índice
lanche.remove('pizza') # Remove pelo valor

lanche = ['cachorro quente', 'hamburguer', 'suco', 'picolé', 'cookie']

lanche.pop()
lanche = ['cachorro quente', 'hamburguer', 'suco', 'picolé']

if pizza in lanche:
    lanche.remove('pizza')

valores = list(range(4, 11))
valores = [4, 5, 6, 7, 8, 9, 10]

valores [8, 2, 5, 4, 9, 3, 0]
valores.sort()
valores.sort(reverse=True)
len(valores)  7

num = (2, 5, 9, 1)
# num[2] = 3 # erro

num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # erro
num.append(7)
num.sort()
print(num)
[1, 2, 3, 5, 7]

num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
[7, 5, 3, 2, 1]
Essa lista tem 5 elementos.

num.sort(reverse=True)
num.insert(2, 0)
num.pop()
num.pop(2)
[7, 5, 3, 2]


valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontei o valor {v}!')
print("Cheguei ao final da lista.")

a = [2, 3, 4, 7]
b = a
b[2] = 8

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
"""