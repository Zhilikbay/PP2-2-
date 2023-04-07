import pygame
import sys

pygame.init()


window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Ball Game')


ball_radius = 25
ball_size = ball_radius * 2
ball_color = (255, 0, 0)
ball_pos = [window_width // 2, window_height // 2]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_pos[1] = max(ball_pos[1] - 20, ball_radius)
    elif keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + 20, window_height - ball_radius)
    elif keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - 20, ball_radius)
    elif keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + 20, window_width - ball_radius)


    window.fill((255, 255, 255))

    pygame.draw.circle(window, ball_color, ball_pos, ball_radius)

    pygame.display.flip()