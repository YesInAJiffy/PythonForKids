import pygame
import sys
import os
from pygame.locals import *
from PIL import Image

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game with Paddle, Scores, and Sound")

# Load background image
background_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "background.jpg"))
background_image = pygame.transform.scale(background_image, (width, height))

# Load ball image
ball_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "ball.png"))
ball_image = pygame.transform.scale(ball_image, (40, 40))
ball_angle = 0  # Initial angle of rotation

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up ball
ball_rect = ball_image.get_rect(center=(width // 2, height // 2))
ball_speed_x = 5
ball_speed_y = 5

# Set up paddle
paddle_width = 100
paddle_height = 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - paddle_height - 10
paddle_speed = 8

# Set up scores
score = 0
font = pygame.font.Font(None, 36)

# Set up game state
game_over = False

# Set up sound effects
bounce_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "bounce.wav"))
score_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "score.wav"))
game_over_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "game_over.wav"))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Restart game if it's over and the space bar is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_over:
            ball_rect.center = (width // 2, height // 2)
            score = 0
            game_over = False

    if not game_over:
        # Update ball position
        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y

        # Rotate the ball
        rotated_ball = pygame.transform.rotate(ball_image, ball_angle)
        ball_rect = rotated_ball.get_rect(center=ball_rect.center)
        ball_angle += 5  # Adjust the rotation speed

        # Bounce off walls
        if ball_rect.left < 0 or ball_rect.right > width:
            ball_speed_x = -ball_speed_x
            bounce_sound.play()

        if ball_rect.top < 0:
            ball_speed_y = -ball_speed_y
            bounce_sound.play()

        # Bounce off paddle
        if ball_rect.colliderect(paddle_x, paddle_y, paddle_width, paddle_height):
            ball_speed_y = -ball_speed_y
            bounce_sound.play()
            score += 1

        # Ball goes below paddle (game over)
        if ball_rect.top > height:
            game_over = True
            game_over_sound.play()

        # Move paddle with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
            paddle_x += paddle_speed

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the rotating ball
    screen.blit(rotated_ball, ball_rect)

    # Draw the paddle
    pygame.draw.rect(
        screen, black, (int(paddle_x), int(paddle_y), paddle_width, paddle_height)
    )

    # Draw the score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    if game_over:
        # Display game over text
        game_over_text = font.render("Game Over. Press SPACE to restart.", True, black)
        screen.blit(game_over_text, ((width - game_over_text.get_width()) // 2, height // 2))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
