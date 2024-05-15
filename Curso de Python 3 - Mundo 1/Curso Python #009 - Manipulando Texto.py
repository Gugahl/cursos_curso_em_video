"""Curso em Python #09 - Manipulado Texto"""
"""
# Manipulando Texto
# Frase = Cadeia de Caracteres = String = Cadeia de Texto (Para o Python só é string se estiver entre aspas simples, ou
# aspas duplas.)
# Variável = Recebe algo, atribui algo, uma variável pode receber strings a exemplo ( aluno = Gustavo )
# Cada caractere é um mini-espaço alocado na memória (começando do 0)

# Operações com strings:

frase = 'Curso em Video Python'

# Fatiamento:
# Fatiar uma string, é conseguir pegar pedaços dela;

# Primeira maneira é pegando um caractere por vez:
var = frase[9]
print(var)

# Segunda maneira é pegando os caracteres de um número a outro:
var2 = frase[9:13]
print(var2)

var3 = frase[9:21]
print(var3)

# Terceira maneira é pegando os caracteres de um número a outro pulando caracteres:
var4 = frase[9:21:2]
print(var4)
var7 = frase[9::3]
print(var7)


# Quarta maneira é pegando os caracteres do começo para outro número:
var5 = frase[:5]
print(var5)

# Quinta maneira é pegando os caracteres de um número até o final:
var6 = frase[15:]
print(var6)

# Análise:
# Analisar uma string, é saber informações sobre ela;

# len(): Conta a quantidade de caracteres de uma string a partir de 0:
var8 = len(frase)
print(var8)

# var.count(''): Conta quantas vezes um caractere aparece dentro de uma string:
var9 = frase.count('o')
print(var9)

# var.count('o', 0, 13): Conta quantas vezes o caractere 'o' apareceu dentro da string representada pela variável var
# no intervalo do caractere 0 ao caractere 13:
var10 = frase.count('o', 0, 13)
print(var10)

# var.find(''): Conta a quantidade de vezes que o programa encontrou um determinada string:
var11 = frase.find('deo')
print(var11)

# frase.find('Android'): Quando você coloca para o find uma string que não existe naquela variável ele te retorna -1:
var12 = frase.find('Android')
print(var12)

# '' in var: Você pergunta se existe uma string específica dentro de uma variável
var13 = 'Curso' in frase
print(var13)

# Transformação
# Transforma uma string, consegue mudar ela

# var.replace(' ',' '): Muda uma string para outra:
var14 = frase.replace('Python', 'Android')
print(var14)

# var.upper(): Muda a string para maiúscula:
var15 = frase.upper()
print(var15)

# var.lower(): Muda a string para minúscula:
var16 = frase.lower()
print(var16)

# var.capitalize(): Muda a string para minúscula e transforma a primeira letra em maiúscula:
var17 = frase.capitalize()
print(var17)

# var.title(): Muda string para minúscula e transforma a primeira letra de cada palavra em maiúscula:
var18 = frase.title()
print(var18)

frase1 = '   Aprenda Python '
# var.strip(): Remove espaços inúteis da uma string tanto na esquerda como na direita:
var19 = frase1.strip()
print(var19)

# var.rstrip(): Remove espaços inúteis de uma string na direita:
var20 = frase1.rstrip()
print(var20)

# var.lstrip(): Remove espaços inúteis de uma string na esquerda:
var21 = frase1.lstrip()
print(var21)

# Divisão
# Divide strings

frase2 = 'Curso em Video Python'

# var.split(): Vai pegar onde tiver espaços e criar uma divisão de strings
var22 = frase2.split()
print(var22)

# ''.join(var): Vai pegar um caractere para juntar variáveis splitadas:
var23 = '-'.join(var22)
print(var23)
"""
