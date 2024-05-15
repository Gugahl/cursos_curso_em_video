"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Aula 14 rev:
Enquanto não chegar na maçã:
  Se ele tiver um bloco na frente:
    Passo para frente
  Se ele tiver um abismo na frente:
    Pular
  Se tiver uma moeda:
    Pegar
Pegar
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Lógica
Enquanto Verdadeiro:
  Se tiver um bloco na frente:
    Passo para frente
  Se tiver um abismo na frente:
    Pular
  Se tiver uma moeda:
    Pegar
  Se tiver Troféu
    Pular
    Interrompa
Pegar

Sintaxe Python
while True:
  if bloco:
    passo
  if abismo:
    pula
  if moeda:
    pega
  if Troféu:
    pula
    break
pega
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Prática
cont = 1
while cont <= 10:
  print(cont, '-> ', end='')
  cont += 1
print('Acabou')

cont = 1
while True:
  print(cont, '-> ', end='')
  cont += 1
print('Acabou')

n = s = 0
while n != 999:
  n = int(input('Digite um número: '))
  s += n
s -= 999
print(f'A soma vale {s}')

n = s = 0
while True:
  n = int(input('Digite um número: '))
  if n == 999:
    break
  s += n
print(f'A soma vale {s}')
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
