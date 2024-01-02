import time
import pygame
import random
from config import screen_size, center_dot_position, background_color, center_dot_color, screen_dots_color, \
    line_draw_color

pygame.init()

screen = pygame.display.set_mode(screen_size)
screen.fill(background_color)
pygame.display.update()

# Dot
center_circle = pygame.draw.circle(screen, pygame.Color(center_dot_color), center_dot_position, 10)
pygame.display.update()

place = (random.randint(1, 800), random.randint(1, 800))

one = pygame.draw.circle(screen, pygame.Color(screen_dots_color), place, 8)


def draw_line(end_pos):
    pygame.draw.line(screen, line_draw_color, center_dot_position, end_pos, 3)


draw_line(place)
pygame.display.update()

time.sleep(50)
