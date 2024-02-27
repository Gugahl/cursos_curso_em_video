"""Desafio #042"""
"""
Refaça o DESAFIO 035 dos triângulos
acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""

exercicio = 'Exercício #042'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

r1 = float(input('Digite aqui o primeiro segmento de reta: '))
r2 = float(input('Digite aqui o segundo segmento de reta: '))
r3 = float(input('Digite aqui o terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2:
        print(f'Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')

    elif r1 == r2 == r3:
        print(f'Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')

    elif r1 != r2 != r3:
        print(f'Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
