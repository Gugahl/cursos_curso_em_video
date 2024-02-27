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

desafio = ' Desafio #043 '
print(f'{desafio:=^30}')
print(' ')

peso = float(input('Quantos quilos você tem? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Você está abaixo do peso.')

elif 18.5 < imc < 25:
    print(f'Você está no peso ideal.')

elif 25 < imc < 30:
    print(f'Você está no sobrepeso.')

elif 30 < imc < 40:
    print(f'Você está no quadro de obesidade, cuidado.')

elif imc > 40:
    print(f'Você está no quadro de obesidade mórbida, você deve se preocupar,\n'
          f'talvez seja hora de ter uma rotina mais saudável.')
