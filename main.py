import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255


main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1,1]

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False  # pygame.quit()
    ball_rect = ball_rect.move(ball_speed)
    
    
    
    main_surface.fill(BLACK)

    main_surface.blit(ball, ball_rect)

    
    # main_surface.fill((155,155,155))
    pygame.display.flip()
