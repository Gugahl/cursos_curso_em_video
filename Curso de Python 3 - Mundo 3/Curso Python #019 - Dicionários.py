"""
Curso Python #019 - Dicionários

Variáveis Compostas 
        (Dicionários)

dados = list()
dados.append('Pedro')
dados.append('Pedro')
print(dados[0])  Pedro
print(dados[1])  25

Listas e Tuplas operam com índices numéricos
Dicionários operam com índices literais, ou seja, eu consigo nomear os índices

Tuplas ()
Listas []
Dicionários {}

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])  Pedro
print(dados['idade'])  25
dados['sexo'] = 'M'
del dados['idade']

filme = {'titulo':'Star Wars',
'ano':1977,
'diretor':'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in fime.items():
        print(f'O {k} é {v}')   O título é Star Wars
                                O ano é 1977
                                O diretor é George Lucas

filme1 = dict()
filme2 = dict()
filme3 = dict()

locadora = list()
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme2)

print(locadora[0]['ano'])       1977
print(locadora[2]['titulo'])    'Matrix'

gustavo = {'nome': 'Gustavo', 'idade': 20, 'sexo': 'Masculino', 'peso': 81}
lais = {'nome': 'Laís', 'idade': 20, 'sexo': 'Feminino', 'peso': 73}
pessoas = (gustavo, lais)
for i in range(len(pessoas)):
        print('')
        print(pessoas[i].keys())
        print(pessoas[i].values())
        print(pessoas[i].items())
        if pessoas[i]['sexo'] == 'Masculino':
                print(f'O {pessoas[i]["nome"]} tem {pessoas[i]["idade"]} anos de idade e pesa {pessoas[i]["peso"]} quilos.')
        if pessoas[i]['sexo'] == 'Feminino':
                print(f'A {pessoas[i]['nome']} tem {pessoas[i]["idade"]} anos de idade e pesa {pessoas[i]["peso"]} quilos.')
        print('')

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

brasil = list()
estado = dict()
for c in range(3):
        estado['uf'] = str(input('Unidade Federativa: '))
        estado['sigla'] = str(input('Sigla do Estado: '))
        brasil.append(estado.copy())
for e in brasil:
        for uf, sigla in e.items():
                print(f'O campo {uf} tem valor {sigla}')
"""
