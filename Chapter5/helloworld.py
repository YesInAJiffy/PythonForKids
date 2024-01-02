import pygame
import sys


pygame.init()

width, height = 800 , 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("First Game")

#Load images
background = pygame.image.load("background.jpg")

character = pygame.image.load("character.png")
character_pos = [ 100, 100]
# Set up clock
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
            
    screen.blit(background, (0,0))
    character_pos[0] += 1
    screen.blit(character, character_pos)
    pygame.display.flip()
    clock.tick(10)  # Adjust animation speed

        
        
        
        
        
        
