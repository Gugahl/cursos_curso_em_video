"""Curso Python #012 - Condições Aninhadas"""
"""
Condições aninhadas são estruturas condicionais (if's) dentro de estruturas condicionais (if's)
if: se
elif: senão se
elif: senão se
else: senão
Dentro de um if você pode usar quantos elif's quiser, e o else só pode ser usado no máximo uma vez
"""

nome = str(input('Qual é o seu nome? ')).lower().title()
if nome == 'Gustavo':
    print(f'Que nome lindo {nome}!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print(f'Parabéns {nome}! Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print(f'Que belo nome feminino, {nome}!')
else:
    print(f'Poxa {nome}, seu nome é tão normal.')
print(f'Tenha um bom dia, {nome}!')
