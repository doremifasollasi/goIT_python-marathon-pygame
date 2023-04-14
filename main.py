import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT


pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0,255, 0

font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(screen)

player = pygame.Surface((20, 20))
player.fill(WHITE)
player_rect = player.get_rect() #координати положення player - початкове(0,0)
player_speed = 5

def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(4, 6)
    return [enemy, enemy_rect, enemy_speed]

def create_bonus(): # функція, яка створює бонуси зеленого кольору, які рухаються згори донизу
    bonus = pygame.Surface((20, 20))
    bonus.fill(GREEN)
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(4, 6)
    return [bonus, bonus_rect, bonus_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

scores = 0

enemies = []
bonuses = []

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False  # pygame.quit()

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy()) # на кожній ітерації ми викликатимемо ф-ю create enemy(), яка створює нового ворога і додає його у список enemies
        
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
    # player_rect = player_rect.move(player_speed) перенесли в команду K_DOWN
    
    # if player_rect.bottom >= height or player_rect.top <= 0: #відбивання м'яча від верхньої та нижньої сторони ігрового поля зі зміною кольору
    #     player.fill((RED))
    #     player_speed[1] = -player_speed[1]
    
    # if player_rect.right >= width or player_rect.left <= 0: #відбивання м'яча від правої та лівої сторони ігрового поля зі зміною кольору
    #     player.fill((GREEN))
    #     player_speed[1] = -player_speed[1]

    pressed_key = pygame.key.get_pressed()

    main_surface.fill(BLACK)

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores), True, WHITE), (width-30, 0)) # відмальовуємо рахунок гри

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2],0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0: # Проблема: кількість ворогів у списку буде постійно збільшуватись, що призведе до навантаження на пам'ять. Рішення: видалення. Реалізація: Якщо позиція нашого ворога більша за 0, то ми його видяляємо.
            enemies.pop(enemies.index(enemy))
    # print(len(enemies)) # перевіримо, чи дійсно працює логіка видалення ворогів зі списку

        if player_rect.colliderect(enemy[1]): # Видаляємо ворога при зустрічі з нашим героєм
            # enemies.pop(enemies.index(enemy))
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])   

        if bonus[1].bottom >= height: # Проблема: кількість ворогів у списку буде постійно збільшуватись, що призведе до навантаження на пам'ять. Рішення: видалення. Реалізація: Якщо позиція нашого ворога більша за 0, то ми його видяляємо.
            bonuses.pop(bonuses.index(bonus))
            scores += 1

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))

    if pressed_key[K_DOWN] and not player_rect.bottom >= height: #додаємо керування клавіши ВНИЗ
        player_rect = player_rect.move(0, player_speed)

    if pressed_key[K_UP] and not player_rect.top <= 0: #додаємо керування клавіши ДОГОРИ
        player_rect = player_rect.move(0, -player_speed)

    if pressed_key[K_RIGHT] and not player_rect.right >= width: #додаємо керування клавіши ПРАВОРУЧ
        player_rect = player_rect.move(player_speed, 0)

    if pressed_key[K_LEFT] and not player_rect.left <= 0: #додаємо керування клавіши ЛІВОРУЧ
        player_rect = player_rect.move(-player_speed, 0)
    
    # main_surface.fill((155,155,155))
    pygame.display.flip()
