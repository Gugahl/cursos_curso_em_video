"""
Variáveis Compostas
(Listas)    Parte 2

dados = list()
mutável
dados.append('Pedro')
dados.append(25)
print(dados[0])     Pedro
print(dados[1])     25

pessoas = list()
pessoas.append(dados[:])
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])    Pedro
print(pessoas[1][1])    19
print(pessoas[2][0])    João
print(pessoas[1])   ['Maria', 19]

teste = list()
teste.append('Gustavo')
teste.append(20)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for pessoa in galera:
    print(pessoa)

for pessoa in galera:
    print(pessoa[0])

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
"""

dado = list()
galera = list()
totmaior = totmenor = 0

for computador in range(3):
    if computador > 0:
        print(' ')
    dado.append(str(input(f'Nome da {computador + 1}ª pessoa: ')))
    dado.append(int(input(f'Idade da {computador + 1}ª pessoa: ')))
    galera.append(dado[:])
    dado.clear()

print(f'\n{galera}\n')

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} atingiu a maioridade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor += 1

print(f'\nAo todo temos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')