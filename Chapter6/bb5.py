import pygame
import sys
import os

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game with Paddle, Scores, and Sound")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up ball
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
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
            ball_x = width // 2
            ball_y = height // 2
            score = 0
            game_over = False

    if not game_over:
        # Update ball position
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Bounce off walls
        if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
            ball_speed_x = -ball_speed_x
            bounce_sound.play()

        if ball_y - ball_radius < 0:
            ball_speed_y = -ball_speed_y
            bounce_sound.play()

        # Bounce off paddle
        if (
            ball_y + ball_radius > paddle_y
            and paddle_x < ball_x < paddle_x + paddle_width
        ):
            ball_speed_y = -ball_speed_y
            bounce_sound.play()
            score += 1

        # Ball goes below paddle (game over)
        if ball_y - ball_radius > height:
            game_over = True
            game_over_sound.play()

        # Move paddle with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
            paddle_x += paddle_speed

    # Clear the screen
    screen.fill(white)

    if game_over:
        # Display game over text
        game_over_text = font.render("Game Over. Press SPACE to restart.", True, black)
        screen.blit(game_over_text, ((width - game_over_text.get_width()) // 2, height // 2))

    else:
        # Draw the ball
        pygame.draw.circle(screen, black, (int(ball_x), int(ball_y)), ball_radius)

        # Draw the paddle
        pygame.draw.rect(
            screen, black, (int(paddle_x), int(paddle_y), paddle_width, paddle_height)
        )

        # Draw the score
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

