"""Desafio #042"""
"""
Refaça o DESAFIO 035 dos triângulos
acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""

desafio = ' Desafio #042 '
print(f'{desafio:=^30}')
print(' ')

r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!', end=' ')

    if r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2:
        print('Esse triângulo é ISÓSCELES.')
    elif r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO.')
    elif r1 != r2 != r3:
        print('Esse triângulo é ESCALENO.')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
