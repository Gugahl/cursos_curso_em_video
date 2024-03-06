"""Desafio #053"""
"""
Crie um programa que leia uma frase qualquer e diga se ela é um 
palíndromo, desconsidere os espaços.
"""
desafio = ' Desafio #053 '
print(f'{desafio:=^30}', '\n')


frase_usuario = str(input("Me forneça uma frase para verificar se é palíndroma: "))
frase_formatada = frase_usuario.replace(" ", "").lower()
frase_invertida = ""
for letra in reversed(frase_formatada):
    frase_invertida += letra

if frase_formatada == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
