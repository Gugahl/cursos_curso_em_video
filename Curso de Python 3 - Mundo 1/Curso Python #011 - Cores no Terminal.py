"""Curso Python #11 - Cores no Terminal"""
"""
Padrão ANSI: Padrão de normalização internacional que tem escape sequence, que basicamente funciona em vários ambientes
vamos utilizar ele em terminal.
Código ANSI para cores: O código ANSI começa com \ e depois vem um código, um dos códigos para cores que funciona para
cores é o código 033, logo, sempre que você quiser representar uma cor em Python, você começa com \033[m, entre esse
colchete e esse m você vai colocar o código da cor, podendo variar entre nenhum código, um código, dois códigos até
três códigos, o primeiro código que a gente vai representar é o código de comportamento estilo, em seguida, você coloca 
; e vai colocar o segundo código que é o código do texto e por final você vai colocar o último código que é o código do
background que é a cor de fundo, então basicamente você vai ter que indicar qual é o estilo da fonte, se ela ta normal,
se ela ta em negrito, se ela vai ta sublinhada..., você vai informar em segundo lugar qual é a cor do texto, e por 
último, a cor do fundo, na verdade você pode colocar em qualquer ordem que o Python diferencia os códigos de fonte, cor
de texto e cor de fundo.
"""
"""
\033[0;33;44m
Códigos para estilo de fonte:
0: Sem estilo
1: Negrito
4: Sublinhado
7: Trocar as cores, a que estiver no fundo vem para a letra, e a que ta na letra vai para o fundo

Códigos para cor de texto:
30: Preto
31: Vermelho
32: Verde
33: Amarelo
34: Azul
35: Lilás
36: Ciano
37: Cinza
97: Branco

Códigos para cor de fundo:
40: Preto
41: Vermelho
42: Verde
43: Amarelo
44: Azul
45: Lilás
46: Ciano
47: Cinza
107: Branco
"""
"""
Testes:

Fundo vermelho + letra branca: \033[30;41m
Fundo azul claro + letra amarela + sublinhado: \033[4;33;44m
Fundo amarelo + letra lilás + negrito: \033[1;35;43m
Fundo verde + letra branca: \033[97;42m
Fundo preto + letra cinza: \033[m
Fundo branco + letra preta: \033[30;107m ou Fundo branco + letra preta: \033[7;97m

print('\033[31mOlá, Mundo!')  # Letra vermelha
print('\033[31;43mOlá, Mundo!')  # Letra vermelha + fundo amarelo
print('\033[1;31;43mOlá, Mundo!')  # Letra vermelha + fundo amarelo + negrito
print('\033[1;31;43mOlá, Mundo!\033[m')  # Letra vermelha + fundo amarelo + negrito + fim de fundo
print('\033[4;97;45mOlá, Mundo!\033[m')  # Letra branca + fundo lilás + sublinhado + fim de fundo
print('\033[97mOlá, Mundo!\033[m')  # Letra branca
print('\033[mOlá, Mundo!\033[m')  # Letra cinza claro (Padrão)
print('\033[37mOlá, Mundo!\033[m')  # Letra cinza escuro
print('\033[30;107mOlá, Mundo!\033[m')  # Letra preta + fundo branco
print('\033[7;97mOlá, Mundo!\033[m')  # Letra preta + fundo branco (Inversor)
print('\033[33;44mOlá, Mundo!\033[m')  # Letra amarela + fundo azul
print('\033[7;33;44mOlá, Mundo!\033[m')  # Letra azul + fundo amarelo (Inversor)
print('\033[34;43mOlá, Mundo!\033[m')  # Letra azul + fundo amarelo
"""
"""
valor1 = int(input('Me forneça um valor inteiro: '))
valor2 = int(input('Me forneça outro valor inteiro: '))
print(f'O primeiro valor foi o número: \033[31m{valor1}\033[m, e o segundo valor foi o número: '
      f'\033[32m{valor2}\033[m.')
"""
"""
nome = str(input('Qual é o seu nome? ')).lower().title()
print(f'Olá! Prazer em te conhecer \033[4;34m{nome}!')
"""

letras = {"limpar": "\033[m",
          "preto": "\033[30m",
          "vermelho": "\033[31m",
          "verde": "\033[32m",
          "amarelo": "\033[33m",
          "azul": "\033[34m",
          "lilás": "\033[35m",
          "ciano": "\033[36m",
          "cinza": "\033[37m",
          "branco": "\033[97m"}

fundo = {"limpar": "\033[m",
         "preto": "\033[40m",
         "vermelho": "\033[41m",
         "verde": "\033[42m",
         "amarelo": "\033[43m",
         "azul": "\033[44m",
         "lilás": "\033[45m",
         "ciano": "\033[46m",
         "cinza": "\033[47m",
         "branco": "\033[107m"}

estilo = {"limpar": "\033[0m",
          "negrito": "\033[1m",
          "sublinhado": "\033[4m",
          "inversor": "\033[7m"}

nome = str(input('Qual é o seu nome? ')).lower().title()
print(f'Olá! Prazer em te conhecer {fundo["limpar"]}{estilo["sublinhado"]}{letras["azul"]}{nome}{letras["limpar"]}!')
