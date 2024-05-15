"""DESAFIO 011"""
"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta ne-
-cessária para pintá-la, sabendo que, cada litro de tinta, pinta uma área de 2m².
"""

desafio = ' DESAFIO 011 '
print(f'{desafio:=^30}', '\n')
print('Ok, você quer que eu pinte a sua casa, vamos começar por essa parede, vou\n'
      'tirar as medidas e te direi quantos litros de tinta será necessário.', '\n')
larg = float(input('Quantos metros de largura essa parede tem? '))
alt = float(input('Quantos metros de altura essa parede tem? '))
arpar = larg * alt
litros = arpar/2
lata = (litros//3.6) + 1
print(f'Nesse caso sua parede vai precisar de mais ou menos {litros} litros de tinta, ou seja, '
      f'quase {lata} latas de tinta daquelas de 3,6L.')
