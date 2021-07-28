#021 - Faça um programa python que abra e reproduza o áudio de um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('drown.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
