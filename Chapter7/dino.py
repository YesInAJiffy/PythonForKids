import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 300

# Load background image
background_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "background.jpeg"))
background_image = pygame.transform.scale(background_image, (width, height))



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Run Game with Random Cactus and Gravity")

# Load images for dino running animation
dino_images = [pygame.image.load(f"dino{i}.png") for i in range(1, 10)]
for i in range(9):
    dino_images[i] = pygame.transform.scale(dino_images[i], (50, 50))

# Load cactus image
cactus_image = pygame.image.load("cactus.png")
cactus_image = pygame.transform.scale(cactus_image, (30, 30))

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up dino
dino_index = 0
dino_rect = dino_images[dino_index].get_rect()
dino_rect.topleft = (50, height - dino_rect.height - 20)
dino_speed = 5
jump_height = 10
is_jumping = False
gravity = 5

# Set up cactus (obstacle)
cacti = []
cactus_speed = 8
spawn_timer = 0
timer_trigger = 2

# Set up scoring
score = 1
#levelup = 10

# Set up clock
clock = pygame.time.Clock()

def reset():
    global gravity
    gravity = 5
    
# Function to spawn a random cactus
def spawn_cactus():
    cactus_rect = cactus_image.get_rect()
    cactus_rect.topleft = (width, height - cactus_rect.height - 20)
    #print(cactus_rect.topleft)
    return cactus_rect

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))
    
    instructions = font.render(f"UP -> Jump", True, blue)
    screen.blit(instructions, (10, 50))
    instructions = font.render(f"Down -> Increase Deceleration", True, blue)
    screen.blit(instructions, (10, 70))
    instructions = font.render(f"Spacebar -> Restart", True, red)
    screen.blit(instructions, (10, 90))
    #score_text = font.render(f"Score: {score}", True, black)

# Function to restart the game
def restart_game():
    global score, is_jumping, cacti, dino_rect, cactus_speed
    score = 0
    is_jumping = False
    cacti = []
    dino_rect.topleft = (50, height - dino_rect.height - 20)
    cactus_speed = 8

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Restart game if it's over and the space bar is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_jumping:
            restart_game()

    # Move dino with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not is_jumping:
        is_jumping = True
        reset()
         
    if keys[pygame.K_DOWN]:
        gravity = gravity * 2

    if (dino_rect.y != (height - dino_rect.height - 20)):
        is_jumping = False
        
    if is_jumping:
        if False: #jump_height >= -10:
            dino_rect.y -= (jump_height ** 2) * 0.5
            jump_height -= 1
        else:
            is_jumping = False
            jump_height = 120
            dino_rect.y -= jump_height
            
            

    # Apply gravity
    if dino_rect.y < height - dino_rect.height - 20:
        dino_rect.y += gravity
    else:
        dino_rect.y = height - dino_rect.height - 20

    if score > 5 and score < 10 :
        cactus_speed = 15
    elif score >= 10 and score < 15 :
        cactus_speed = 20
    elif score >= 15 and score < 20 :
        cactus_speed = 25
    elif score >= 20 :
        cactus_speed = 30
    #cactus_speed = 8
    #print(f"{cactus_speed}    {score}")
    # Move and spawn cacti
    spawn_timer += 1
    if (spawn_timer >= timer_trigger - cactus_speed) or (len(cacti) == 0):  # Adjust spawn rate
        #print(f" {spawn_timer}   {timer_trigger}  {cactus_speed}")

        cacti.append(spawn_cactus())
        timer_trigger = random.randint(35, 55)
        spawn_timer = 0
        # Update score
        score += 1
    #print(f"OUTSIDE {spawn_timer}   {timer_trigger}  {cactus_speed}")
    for cactus_rect in cacti:
        cactus_rect.x -= cactus_speed

     
    # Remove off-screen cacti
    cacti = [cactus_rect for cactus_rect in cacti if cactus_rect.right > 0]

    # Check for collision with cacti
    for cactus_rect in cacti:
        if dino_rect.colliderect(cactus_rect):
            print("Game Over! Score:", score)
            restart_game()

    
    # Clear the screen
    screen.fill(white)
    
    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw dino running animation
    screen.blit(dino_images[dino_index], dino_rect)
    dino_index = (dino_index + 1) % 9  # Cycle through frames

    # Draw cacti
    for cactus_rect in cacti:
        screen.blit(cactus_image, cactus_rect)

    # Display the score
    display_score()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)  # Adjust animation speed

