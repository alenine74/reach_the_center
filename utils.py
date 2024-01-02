import random
import time
import pygame
from config import screen_size, center_dot_position, background_color, center_dot_color, screen_dots_color, \
    line_draw_color

list_dots = list()


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill(background_color)
    pygame.display.update()
    return screen


def create_center_dot(screen):
    pygame.draw.circle(screen, pygame.Color(center_dot_color), center_dot_position, 10)
    pygame.display.update()


def draw_line(screen, end_pos):
    pygame.draw.circle(screen, pygame.Color(screen_dots_color), end_pos, 10)
    pygame.draw.line(screen, line_draw_color, center_dot_position, end_pos, 3)
    pygame.display.update()
    time.sleep(0.5)


def _dots_position():
    i = 0
    while i < 50:
        x = random.randint(1, 800)
        y = random.randint(1, 800)
        if (x, y) not in list_dots:
            list_dots.append((x, y))
            i += 1
    return list_dots


def draw_dots(screen):
    _dots_position()
    for dot in list_dots:
        draw_line(screen, dot)
