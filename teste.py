import math
print('Equação do Segundo Grau')
print('-----------------------')
valorA = int(input('Informe o valor de A: '))
print(valorA)
valorB = int(input('Informe o valor de B: '))
print(valorB)
valorC = int(input('Informe o valor de C: '))
print(valorC)
print('----------------------')
print('Sua equação é: ', valorA, 'x2 +', valorB, 'x +', valorC, '= 0')
delta = (valorB*valorB) - 4*valorA*valorC
print('Valor de Delta: ', delta)
print('---------------------------')
if (delta < 0):
    print('Para Delta negativo, não existem raízes reais.')
else:
    if delta == 0:
        x1 = (-valorB + math.sqrt(delta))/ (2*valorA)
        print('Para Delta zero, temos duas raízes iguais a ', x1)
    else:
        x1 = (-valorB + math.sqrt(delta))/(2*valorA)
        x2 = (-valorB - math.sqrt(delta))/(2*valorA)
        print('Para Delta positivo. Raízes diferentes: ')
        print("x1 = ", x1)
        print("x2 = ", x2)
