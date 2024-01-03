import random
import time
import pygame
import math
from config import SCREEN_SIZE, CENTER_DOT_POSITION, background_color, center_dot_color, screen_dots_color, \
    line_draw_color, num_dots


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(background_color)
    pygame.display.update()
    return screen


def create_center_dot(screen):
    pygame.draw.circle(screen, pygame.Color(center_dot_color), CENTER_DOT_POSITION, 10)
    pygame.display.update()


def _draw_line(screen, end_pos):
    pygame.draw.circle(screen, pygame.Color(screen_dots_color), end_pos, 5)
    pygame.draw.line(screen, pygame.Color(line_draw_color), CENTER_DOT_POSITION, end_pos, 2)
    pygame.display.update()
    time.sleep(0.1)


# def _distance(point1, point2):
#     """distance calculation with Pythagoras Formula"""
#     return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


"""
generates random angles,
calculates coordinate points incrementally further
from the center point using trigonometry
"""


def _generate_random_dots():
    max_distance = math.sqrt(SCREEN_SIZE[0] ** 2 + SCREEN_SIZE[1] ** 2) / 2
    distance_increment = max_distance / num_dots

    dots = []
    for i in range(1, num_dots + 1):
        angle = random.uniform(0, 2 * math.pi)
        dist = distance_increment * i
        x = CENTER_DOT_POSITION[0] + dist * math.cos(angle)
        y = CENTER_DOT_POSITION[1] + dist * math.sin(angle)

        x = max(0, min(SCREEN_SIZE[0], x))
        y = max(0, min(SCREEN_SIZE[1], y))

        dots.append((int(x), int(y)))

    return dots


def draw_dots(screen):
    dots = _generate_random_dots()
    for dot in dots:
        _draw_line(screen, dot)
