"""Desafio 021"""
import pygame
"""
Faça um programa em Python que abra e reproduza o aúdio de um arquivo .mp3.
"""

desafio = ' Desafio #021 '
print(f'{desafio:=^30}')

print('Deus Está Te Ensinando a Ser Forte.mp3')

pygame.init()
pygame.mixer.music.load('serforte.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
