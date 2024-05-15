"""Desafio #047"""
from time import sleep
"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50;
"""

desafio = ' Desafio #047 '
print(f'{desafio:=^30}')
print(' ')

print('Números pares entre o número 1 e o número 50:')
for numeros_pares in range(2, 52, 2):
    print(f'{numeros_pares}')
    sleep(1)
print('Fim!')

#  ou
#  from time import sleep
#  for numeros_pares in range(1-1, 50+1):
#   if numeros_pares % 2 == 0:
#       print(numeros_pares)
#       sleep(0.5)
