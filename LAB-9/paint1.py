import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the brush size
BRUSH_SIZE = 10

# Set up the drawing mode
drawing = False
circle = False
rect = False
color = BLACK

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            if rect:
                pygame.draw.rect(screen, color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), BRUSH_SIZE)
            elif circle:
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, BRUSH_SIZE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rect = True
                circle = False
            elif event.key == pygame.K_c:
                circle = True
                rect = False
            elif event.key == pygame.K_b:
                color = BLACK
            elif event.key == pygame.K_w:
                color = WHITE
            elif event.key == pygame.K_q:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_u:
                color = BLUE
            elif event.key == pygame.K_e:
                screen.fill(WHITE)

    # Draw on the screen
    if drawing and not rect and not circle:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), BRUSH_SIZE)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
