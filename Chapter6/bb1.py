import pygame
import sys

#initialize pygame
pygame.init()

# setup display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game")

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

# setup the ball
ball_radius = 20
ball_x = width // 2
ball_y = height // 2

ball_speed_x = 5
ball_speed_y = 5


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #update the ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    
    # Bounce when going outside the boundary
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width :
        ball_speed_x = - ball_speed_x
    if ball_y- ball_radius < 0 or ball_y +ball_radius > height :
        ball_speed_y = -ball_speed_y
    
    #Clear the screen
    screen.fill(white)
    
    #Draw the ball
    pygame.draw.circle(screen, green, (int(ball_x), int(ball_y)), ball_radius)
    
    #Control the game frame rate
    pygame.time.Clock().tick(60)
    #Update the display
    pygame.display.flip()
    





