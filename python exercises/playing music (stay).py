#from playsound import playsound
import pygame
from pygame import mixer

print('utillizando a funcionalidade "mixer"')
mixer.init()
mixer.music.load('Gryffin   Body Back ft. Maia Wright (Official Music Audio).mp3')
mixer.music.play()
input('Digite qualquer coisa e aperte enter para desligar: ')

print('Utilizando a bibllioteca "pygame"')
pygame.mixer.init()
pygame.mixer.music.load('Avicii   Fade Into Darkness (Official Audio)   Le7els RecordsVeratone.mp3')
pygame.mixer.music.play()
input('Digite algo e aperte enter para parar a musica: ')

#print('Usando a funcionalidade "playsound"')
#playsound('Avicii - The Nights.mp3')