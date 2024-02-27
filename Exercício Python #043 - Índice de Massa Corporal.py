"""Desafio #043"""
"""
Desenvolva uma lógica que leia o peso e a
altura de uma pessoa, calcule seu IMC e mostre
seu status de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

exercicio = 'Exercício #043'
print('-=' * 15)
print(f'{exercicio:^30}')
print('-=' * 15, '\n')

peso = float(input('Quantos quilos você pesa? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura * altura)

print(f'O IMC dessa pessoa é de {imc:.2f}.')
if imc < 18.5:
    print(f'Você está abaixo do peso.')

elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')

elif 25 <= imc < 30:
    print('Você está no sobrepeso.')

elif 30 <= imc < 40:
    print('Você está na obesidade.')

elif imc >= 40:
    print('Você está na obesidade mórbida.')
