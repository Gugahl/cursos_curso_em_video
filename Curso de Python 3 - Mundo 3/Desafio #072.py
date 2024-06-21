"""Desafio #072"""
"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
"""

desafio = "Desafio #072"
print(f"-=" * 15 + f"\n" + f"{desafio:^30}" + f"\n" + f"-=" * 15)

while True:
    extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
    
    usuario = input(f"Digite um número inteiro (entre 0 e 20): ")
    while not usuario.isnumeric():
        usuario = input(f"Digite um número inteiro (entre 0 e 20): ")
    usuario = int(usuario)
    
    while usuario > 20 or usuario < 0:
        usuario = input(f"Digite um número inteiro (entre 0 e 20): ")
        usuario = int(usuario)
    
    print(f"Você digitou {usuario}, escrito em extenso fica: {extenso[usuario]}\n")
    
    continuar = input("Deseja continuar[S/N]? ").upper()[0]
    if continuar == "N":
        break
