import pygame

screen_width = 580
screen_height = 560

back_color = (200,200,200)

pygame.init()
clock = pygame.time.clock()

screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    pygame.display.flip()
    clock.tick(60)