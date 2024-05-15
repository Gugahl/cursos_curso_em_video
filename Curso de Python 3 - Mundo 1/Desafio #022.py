"""Desafio 022"""
"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
<> O nome com todas as letras maiúsculas;
<> O nome com todas as letras minúsculas;
<> Quantas letras ao todo sem considerar os espaços;
<> Quantas letras tem o primeiro nome.
"""

desafio = ' Desafio #022 '
print(f'{desafio:=^30}', '\n')

nome_completo = input('Digite seu nome completo: ').title()
nome_completo_sem_espacos = nome_completo.replace(' ', '')
primeiro_nome = nome_completo.split()
print(f'Seu nome completo é: {nome_completo};\n'
      f'Seu nome completo tem {len(nome_completo_sem_espacos)} letras;\n'
      f'Seu nome em CAPS LOCK fica: {nome_completo.upper()};\n'
      f'Seu nome com todas as letras minúsculas fica: {nome_completo.lower()};\n'
      f'Seu primeiro nome é: {primeiro_nome[0]};\n'
      f'Seu primeiro nome tem {len(primeiro_nome[0])} letras.')
