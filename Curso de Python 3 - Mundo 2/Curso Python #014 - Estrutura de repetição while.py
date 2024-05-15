"""
- Laços de repetição parte 2

enquanto não chegar na maçã:
    Dê um passo
Pegue a maçã

while not maçã:
    passo
pega

enquanto não maçã:
    se tiver chão na frente:
        passo
    se tiver um buraco:
        pule
    se tiver uma moeda:
        pega
pega

while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega
"""
"""
for c in range(1, 10):
    print(c)
print('Fim')
"""
"""
c=1
while c < 11:
    print(c)
    c += 1
print('Fim')
"""
"""
for c in range(1, 5):
    n = int(input('Digite um número: '))
print('Fim')
"""
"""
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')
"""
"""
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
"""
"""
n = 1
while n != 0:
    n = int(input("Digite um número: "))
print("Acabou.")
"""

"""
n = 1
tot = 0
par = impar = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        tot += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {tot} números, desses {par} números eram pares e {impar} números eram ímpares.")
"""