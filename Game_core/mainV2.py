# -*- coding: utf-8 -*-


import pygame, sys
from settings import *
from level import level1

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = level1(level_map,screen)


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
              
   
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 255)
    
    screen.fill(BLACK)
    level.run()

    pygame.display.update()
    clock.tick(60)
    
