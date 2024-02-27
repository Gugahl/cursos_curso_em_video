"""Curso Python #10 - Condições (Parte 1)"""

"""
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')
"""

"""
nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}!')
"""
"""
nome = str(input('Qual é seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
"""

"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
"""

"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
print('Parabéns!!!' if m >= 6 else 'ESTUDE MAIS!!!')
"""
