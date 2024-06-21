"""Exercício Python #073 - Tuplas com Times de Futebol"""
"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time do Flamengo
"""

exercicio = "Exercício #073"
print(f"-=" * 15 + f"\n" + f"{exercicio:^30}" + f"\n" + f"-=" * 15)

times = ("Botafogo", "Flamengo", "Bahia", "Athletico-PR", "Palmeiras", "São Paulo", "Bragantino", "Cruzeiro", "Atlético-MG", "Internacional", "Juventude", "Fortaleza", "Atlético-GO", "Cuiabá", "Vasco da Gama", "Corinthians", "Grêmio", "Criciúma", "Fluminense", "EC Vitória")

print("-=" * 15 + "\n" + f"Lista de times do Brasileirão: {times}" + "\n" + "-=" * 15 + "\n")

print(f"Os 5 primeiros são: {times[:5]}")
print(f"Os 4 últimos são: {times[-4:]}")
print(f"Times em ordem alfabética: {sorted(times)}")
print(f"O Flamengo está na {times.index("Flamengo") + 1}ª posição")
