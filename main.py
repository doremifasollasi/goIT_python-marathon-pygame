import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0,255, 0


main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect() #координати положення ball - початкове(0,0)
ball_speed = 1

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False  # pygame.quit()

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

    if pressed_key[K_DOWN]: #додаємо керування клавіши ВНИЗ
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_key[K_UP]: #додаємо керування клавіши ДОГОРИ
        ball_rect = ball_rect.move(0, -ball_speed)

    if pressed_key[K_RIGHT]: #додаємо керування клавіши ПРАВОРУЧ
        ball_rect = ball_rect.move(ball_speed, 0)

    if pressed_key[K_LEFT]: #додаємо керування клавіши ЛІВОРУЧ
        ball_rect = ball_rect.move(-ball_speed, 0)
    
    # main_surface.fill((155,155,155))
    pygame.display.flip()
