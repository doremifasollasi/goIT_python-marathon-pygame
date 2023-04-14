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

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect() #координати положення ball - початкове(0,0)
ball_speed = 5

def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 3)
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)


enemies = []

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False  # pygame.quit()

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy()) # на кожній ітерації ми викликатимемо ф-ю create enemy(), яка створює нового ворога і додає його у список enemies

    # ball_rect = ball_rect.move(ball_speed) перенесли в команду K_DOWN
    
    # if ball_rect.bottom >= height or ball_rect.top <= 0: #відбивання м'яча від верхньої та нижньої сторони ігрового поля зі зміною кольору
    #     ball.fill((RED))
    #     ball_speed[1] = -ball_speed[1]
    
    # if ball_rect.right >= width or ball_rect.left <= 0: #відбивання м'яча від правої та лівої сторони ігрового поля зі зміною кольору
    #     ball.fill((GREEN))
    #     ball_speed[1] = -ball_speed[1]

    pressed_key = pygame.key.get_pressed()

    main_surface.fill(BLACK)

    main_surface.blit(ball, ball_rect)

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2],0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0: # Проблема: кількість ворогів у списку буде постійно збільшуватись, що призведе до навантаження на пам'ять. Рішення: видалення. Реалізація: Якщо позиція нашого ворога більша за 0, то ми його видяляємо.
            enemies.pop(enemies.index(enemy))
    # print(len(enemies)) # перевіримо, чи дійсно працює логіка видалення ворогів зі списку

        if ball_rect.colliderect(enemy[1]): # Видаляємо ворога при зустрічі з нашим героєм
            enemies.pop(enemies.index(enemy))
        

    if pressed_key[K_DOWN] and not ball_rect.bottom >= height: #додаємо керування клавіши ВНИЗ
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_key[K_UP]: #додаємо керування клавіши ДОГОРИ
        ball_rect = ball_rect.move(0, -ball_speed)

    if pressed_key[K_RIGHT]: #додаємо керування клавіши ПРАВОРУЧ
        ball_rect = ball_rect.move(ball_speed, 0)

    if pressed_key[K_LEFT]: #додаємо керування клавіши ЛІВОРУЧ
        ball_rect = ball_rect.move(-ball_speed, 0)
    
    # main_surface.fill((155,155,155))
    pygame.display.flip()
