import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Set up Snake
snake_size = 20
snake_speed = 15
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (1, 0)  # Initial direction: right

# Set up Food
food_size = 20
food = (random.randrange(1, (width//food_size)) * food_size,
        random.randrange(1, (height//food_size)) * food_size)

# Set up clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0] * snake_size,
                snake[0][1] + snake_direction[1] * snake_size)

    # Check for collisions with the screen edges or itself
    if (new_head[0] < 0 or new_head[0] >= width or
            new_head[1] < 0 or new_head[1] >= height or
            new_head in snake):
        pygame.quit()
        sys.exit()

    # Check for collision with food
    if new_head == food:
        snake.append(snake[-1])  # Grow the snake
        food = (random.randrange(1, (width//food_size)) * food_size,
                random.randrange(1, (height//food_size)) * food_size)

    # Update snake body
    snake = [new_head] + snake[:-1]

    # Clear the screen
    screen.fill(white)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], snake_size, snake_size))

    # Draw food
    pygame.draw.rect(screen, black, (food[0], food[1], food_size, food_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(snake_speed)

