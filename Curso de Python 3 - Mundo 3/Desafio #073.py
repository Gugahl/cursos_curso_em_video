"""Desafio #073"""
"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time do Flamengo
"""

desafio = "Desafio #073"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

tabela_brasileirao = ("Botafogo", "Flamengo", "Bahia", "Athletico-PR", "Palmeiras", "São Paulo", "Bragantino", "Cruzeiro", "Atlético-MG", "Internacional", "Juventude", "Fortaleza", "Atlético-GO", "Cuiabá", "Vasco da Gama", "Corinthians", "Grêmio", "Criciúma", "Fluminense", "EC Vitória")

print(f"Os cinco primeiros colocados são: {tabela_brasileirao[:5]}\n")
print(f"Os quatro últimos colocados são: {tabela_brasileirao[-4:]}\n")
print(f"A tupla em ordem alfabética ficou: {sorted(tabela_brasileirao)}\n")
for pos, time in enumerate(tabela_brasileirao):
    if tabela_brasileirao[pos] == "Flamengo":
        print(f"A posição de que Flamengo ficou na tabela foi: {pos+1}")
