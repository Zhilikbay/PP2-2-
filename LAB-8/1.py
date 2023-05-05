import pygame
import random

# инициализация Pygame
pygame.init()

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# загрузка изображений
player_img = pygame.image.load('\AZ\PP2(2)\LAB-8\images\PLayer.png')
coin_img = pygame.image.load('\AZ\PP2(2)\LAB-8\images\coin.png')
car_img = pygame.image.load('\AZ\PP2(2)\LAB-8\images\Enemy.png')

# размеры игрока и монеты
PLAYER_SIZE = (50, 100)
COIN_SIZE = (50, 50)
CAR_SIZE = (50, 100)

# скорость игрока и машин
PLAYER_SPEED = 5
CAR_SPEED = 7

# количество машин на экране
NUM_CARS = 3

# создание игрока
player_pos = [SCREEN_WIDTH // 2 - PLAYER_SIZE[0] // 2, SCREEN_HEIGHT - PLAYER_SIZE[1] - 10]
player_score = 0

# создание монет и машин
coins = []
cars = []
for i in range(NUM_CARS):
    car_x = random.randint(0, SCREEN_WIDTH - CAR_SIZE[0])
    car_y = random.randint(-SCREEN_HEIGHT, -CAR_SIZE[1])
    cars.append([car_x, car_y])
for i in range(5):
    coin_x = random.randint(0, SCREEN_WIDTH - COIN_SIZE[0])
    coin_y = random.randint(-SCREEN_HEIGHT, -COIN_SIZE[1])
    coins.append([coin_x, coin_y])

# функция для отображения игрока, монет и машин
def draw_objects():
    # отображение игрока
    screen.blit(player_img, player_pos)
    # отображение монет
    for coin in coins:
        screen.blit(coin_img, coin)
    # отображение машин
    for car in cars:
        screen.blit(car_img, car)

# функция для движения машин и монет
def move_objects():
    global player_score
    # движение машин
    for car in cars:
        car[1] += CAR_SPEED
        # проверка столкновения с игроком
        if car[1] + CAR_SIZE[1] > player_pos[1] and car[1] < player_pos[1] + PLAYER_SIZE[1] and \
            car[0] + CAR_SIZE[0] > player_pos[0] and car[0] < player_pos[0] + PLAYER_SIZE[0]:
            player_score -= 1
            car[1] = random.randint(-SCREEN_HEIGHT, -CAR_SIZE[1])
            car[0] = random.randint(0, SCREEN_WIDTH - CAR_SIZE[0])
        # проверка, если машина выходит за границы экрана
        elif car[1] > SCREEN_HEIGHT:
            car[1] = random.randint(-SCREEN_HEIGHT, -CAR_SIZE[1])
            car[0] = random.randint(0, SCREEN_WIDTH - CAR_SIZE[0])
    # движение монет

for coin in coins:
        coin[1] += CAR_SPEED
        # проверка столкновения с игроком
        if coin[1] + COIN_SIZE[1] > player_pos[1] and coin[1] < player_pos[1] + PLAYER_SIZE[1] and \
            coin[0] + COIN_SIZE[0] > player_pos[0] and coin[0] < player_pos[0] + PLAYER_SIZE[0]:
            player_score += 1
            coin[1] = random.randint(-SCREEN_HEIGHT, -COIN_SIZE[1])
            coin[0] = random.randint(0, SCREEN_WIDTH - COIN_SIZE[0])
        # проверка, если монета выходит за границы экрана
        elif coin[1] > SCREEN_HEIGHT:
            coin[1] = random.randint(-SCREEN_HEIGHT, -COIN_SIZE[1])
            coin[0] = random.randint(0, SCREEN_WIDTH - COIN_SIZE[0])

# игровой цикл
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= PLAYER_SPEED
    elif keys[pygame.K_RIGHT] and player_pos[0] + PLAYER_SIZE[0] < SCREEN_WIDTH:
        player_pos[0] += PLAYER_SPEED
    
    # очистка экрана
    screen.fill(WHITE)
    
    # отображение количества монет и очков
    font = pygame.font.SysFont(None, 25)
    text = font.render("Coins: " + str(player_score), True, BLACK)
    screen.blit(text, (10, 10))
    
    # движение и отображение монет и машин
    move_objects()
    draw_objects()
    
    # обновление экрана
    pygame.display.update()
    
    # ограничение FPS
    clock.tick(60)

# завершение Pygame
pygame.quit()