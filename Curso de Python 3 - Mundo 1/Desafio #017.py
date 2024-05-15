"""DESAFIO 017"""
from math import hypot
"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e m-
o comprimento da hipotenusa.
"""

desafio = ' DESAFIO 017 '
print(f'{desafio:=^30}\n')
catopo = float(input('Me forneça o comprimento do cateto oposto em metros: '))
catadja = float(input('Me forneça o comprimento do cateto adjacente em metros: '))
hipot = hypot(catopo, catadja)
print(f'A hipotenusa equivale a {hipot} metros quadrados.')
