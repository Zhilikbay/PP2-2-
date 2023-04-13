import pygame
import sys

# Constants
WIDTH = 700
HEIGHT = 500
BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
MOVEMENT_AMOUNT = 20

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

# Initialize ball position
ball_x = WIDTH // 2 - BALL_RADIUS
ball_y = HEIGHT // 2 - BALL_RADIUS

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Update ball position based on arrow keys
    if keys[pygame.K_UP]:
        if ball_y - MOVEMENT_AMOUNT >= 0:
            ball_y -= MOVEMENT_AMOUNT
    elif keys[pygame.K_DOWN]:
        if ball_y + MOVEMENT_AMOUNT <= HEIGHT - BALL_SIZE:
            ball_y += MOVEMENT_AMOUNT
    elif keys[pygame.K_LEFT]:
        if ball_x - MOVEMENT_AMOUNT >= 0:
            ball_x -= MOVEMENT_AMOUNT
    elif keys[pygame.K_RIGHT]:
        if ball_x + MOVEMENT_AMOUNT <= WIDTH - BALL_SIZE:
            ball_x += MOVEMENT_AMOUNT

    # Update screen
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)