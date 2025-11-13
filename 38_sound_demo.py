#playing sound in python 
import pygame

pygame.mixer.init()
pygame.mixer.music.load("files/sound.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
print("Good bye.")