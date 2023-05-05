import pygame

# initialize Pygame
pygame.init()

# set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint")

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set the default color to black
current_color = BLACK

# set up the eraser
eraser_size = 20
eraser = pygame.Surface((eraser_size, eraser_size))
eraser.fill(WHITE)
eraser.set_colorkey(WHITE)

# define functions for drawing shapes
def draw_square(pos, size):
    pygame.draw.rect(screen, current_color, (pos[0], pos[1], size, size))

def draw_right_triangle(pos, size):
    points = [(pos[0], pos[1] + size),
              (pos[0] + size, pos[1] + size),
              (pos[0], pos[1])]
    pygame.draw.polygon(screen, current_color, points)

def draw_equilateral_triangle(pos, size):
    points = [(pos[0] + size / 2, pos[1]),
              (pos[0], pos[1] + size),
              (pos[0] + size, pos[1] + size)]
    pygame.draw.polygon(screen, current_color, points)

def draw_rhombus(pos, size):
    points = [(pos[0] + size / 2, pos[1]),
              (pos[0] + size, pos[1] + size / 2),
              (pos[0] + size / 2, pos[1] + size),
              (pos[0], pos[1] + size / 2)]
    pygame.draw.polygon(screen, current_color, points)

def draw_rectangle(pos, size_x, size_y):
    pygame.draw.rect(screen, current_color, (pos[0], pos[1], size_x, size_y))

def draw_circle(pos, radius):
    pygame.draw.circle(screen, current_color, pos, radius)

# set up the clock
clock = pygame.time.Clock()

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the user clicked on the eraser
            if eraser.get_rect(center=event.pos).colliderect(screen.get_rect()):
                current_color = WHITE
            else:
                current_color = RED
        elif event.type == pygame.KEYDOWN:
            # check if the user pressed a key for a shape
            if event.key == pygame.K_1:
                draw_square(pygame.mouse.get_pos(), 50)
            elif event.key == pygame.K_2:
                draw_right_triangle(pygame.mouse.get_pos(), 50)
            elif event.key == pygame.K_3:
                draw_equilateral_triangle(pygame.mouse.get_pos(), 50)
            elif event.key == pygame.K_4:
                draw_rhombus(pygame.mouse.get_pos(), 50)
            elif event.key == pygame.K_5:
                draw_rectangle(pygame.mouse.get_pos(), 100, 50)
            elif event.key == pygame.K_6:
                draw_circle(pygame.mouse.get_pos(), 25)
                
    # draw the eraser
    screen.blit(eraser, (pygame.mouse.get_pos()[0] - eraser_size / 2, pygame.mouse.get_pos()[1] - eraser_size / 2))
    pygame.display.update()

pygame.quit()




