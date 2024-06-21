"""
Mundo 03 Python -

Estruturas Compostas (Variáveis Compostas);
Rotinas;
Tratamentos de erros; 

Aula 16 - Variáveis Compostas (Tuplas)

lanche
espaço na memória

lanche = " "
toda variável é um espaço na memória

lanche = hamburguer
lanche recebe hamburguer
Hamburguer vai para o espaço reservado lanche na memória

lanche = suco
O computador elimina o hamburguer e adiciona o suco
Você não consegue declarar dois valores para uma variável

Tem como eu criar uma variável que declare mais valores?
É possível e uma das formas de fazer isso é com tuplas!

Variáveis Simples só declaram um valor
Variáveis Compostas declaram vários valores

Variáveis Compostas:
Tuplas;
Listas;
Dicionários;

Índices:
lanche = (hamburguer, suco, pizza, pudim)       comida
0 = hamburguer                                  hamburguer/suco/pizza/pudim
1 = suco                                
2 = pizza
3 = pudim

print(lanche)
(hamburguer, suco, pizza, pudim)

print(lanche[2])
(pizza)

print(lanche[0:2])
(hamburguer, suco)
    1          2

print(lanche[1:])
(suco, pizza, pudim)

print(lanche[-1])
(pudim)

len(lanche)
4

for comida in lanche:
    print(comida)

"As tuplas são IMUTÁVEIS"
"""

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(f"{lanche}")
print(f"{lanche[1]}")
print(f"{lanche[3]}")
print(f"{lanche[-2]}")
print(f"{lanche[1:2]}")
print(f"{lanche[2:]}")
print(f"{lanche[:2]}")
print(f"{lanche[-2:]}")
print("")
for comida in lanche:
    print(f"Eu vou comer {comida}")
print("")
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print("")
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("")
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("")
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c1 = a + b
c2 = b + a
print(a)
print(b)
print(c1)
print(c2)
print(len(c1))
print(c1.count(5))
print(c1.count(4))
print(c1.count(9))
print(c1)
print(c1.index(8))
print(c1.index(4))
print(c1.index(2))
print(c1.index(2, 4))
print(c1.index(5, 1))
pessoa = ("Gustavo", 20, "M", 81)
print(pessoa)
print("\nComi para caramba!")
