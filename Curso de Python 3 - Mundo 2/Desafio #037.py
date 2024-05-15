"""Desafio #037"""
"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

desafio = ' Desafio #037 '
print(f'{desafio:=^30}')
print(' ')

numero = int(input('Me forneça um número: '))
print(' ')

print(f'O número {numero} está na base decimal, vamos mudar a base dele para transformar-lo.\n'
      f' \n'
      f'A seguir escolha um número entre 1 e 3, onde:\n'
      f'1 se refere a uma conversão para a base binária;\n'
      f'2 se refere a uma conversão para a base octal;\n'
      f'e 3 se refere a uma conversão para a base hexadecimal.\n')
escolha = int(input('Escolha um número de 1 a 3: '))

if escolha == 1:
    binario = str(numero % 2) + str((numero//2) % 2) + str(((numero//2)//2) % 2) + str((((numero//2)//2)//2) % 2)
    print(f'O número {numero} em base binária fica: {binario}.')

elif escolha == 2:
    octal = ((str((((numero // 8) // 8) // 8) % 8) + str(((numero // 8) // 8) % 8) + str((numero // 8) % 8) +
             str(numero % 8)).lstrip("0"))
    print(f'O número {numero} em base octal fica: {octal}.')

elif escolha == 3:
    hexa: str = ((str((((numero // 16) // 16) // 16) % 16) + str(((numero // 16) // 16) % 16) + str((numero // 16) % 16)
                  + str(numero % 16)).lstrip("0"))
    if "10" in hexa:
        hexa = hexa.replace("10", "A")
    if "11" in hexa:
        hexa = hexa.replace("11", "B")
    if "12" in hexa:
        hexa = hexa.replace("12", "C")
    if "13" in hexa:
        hexa = hexa.replace("13", "D")
    if "14" in hexa:
        hexa = hexa.replace("14", "E")
    if "15" in hexa:
        hexa = hexa.replace("15", "F")

    print(f'O número {numero} em base hexadecimal fica: {hexa}')
