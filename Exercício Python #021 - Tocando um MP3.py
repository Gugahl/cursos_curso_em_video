"""Desafio 021"""
import pygame
"""
Faça um programa em Python que abra e reproduza o aúdio de um arquivo .mp3.
"""

exercicio = 'Exercício #021'
print('=' * 30)
print(f'{exercicio:^30}')
print('=' * 30, '\n')

print('Deus Está Te Ensinando a Ser Forte')

pygame.init()
pygame.mixer.music.load('serforte.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
