import pygame
import sys


# 5 6
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

#setup the paddle
paddle_width = 100
paddle_height = 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - paddle_height - 10

paddle_speed  = 8

# Setup Scores
score = 0
font = pygame.font.Font(None, 36)

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
    if ball_y- ball_radius < 0  :
        ball_speed_y = -ball_speed_y
    
    # Bounce from the paddle
    if((ball_y + ball_radius > paddle_y) and paddle_x < ball_x < paddle_x + paddle_width) :
        ball_speed_y = -ball_speed_y
        score += 1
    
    # Ball goes below paddle (this means we should end the game)
    
    if ball_y - ball_radius > height :
        ball_x = width // 2
        ball_y = height // 2
        score = 0
    
    #Move the paddle on the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width :
        paddle_x += paddle_speed
    #Clear the screen
    screen.fill(white)
    
    #Draw the ball
    pygame.draw.circle(screen, green, (int(ball_x), int(ball_y)), ball_radius)
    #Draw the paddle
    pygame.draw.rect( screen, green, (int(paddle_x),int(paddle_y), paddle_width, paddle_height))
    
    #Show the score
    score_text = font.render(f"Score: {score}", True, black)
    
    screen.blit(score_text, (10,10))
    
    #Control the game frame rate
    pygame.time.Clock().tick(60)
    #Update the display
    pygame.display.flip()
    





