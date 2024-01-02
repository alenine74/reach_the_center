import random
import time
import pygame
import math
from config import screen_size, center_dot_position, background_color, center_dot_color, screen_dots_color, line_draw_color

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
    pygame.draw.circle(screen, pygame.Color(screen_dots_color), end_pos, 5) 
    pygame.draw.line(screen, pygame.Color(line_draw_color), center_dot_position, end_pos, 2)
    pygame.display.update()
    time.sleep(0.1)

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def generate_random_dots(num_dots):
    max_distance = math.sqrt(screen_size[0]**2 + screen_size[1]**2) / 2
    distance_increment = max_distance / num_dots

    dots = []
    for i in range(1, num_dots + 1):
        angle = random.uniform(0, 2 * math.pi)
        dist = distance_increment * i
        x = center_dot_position[0] + dist * math.cos(angle)
        y = center_dot_position[1] + dist * math.sin(angle)

        x = max(0, min(screen_size[0], x))
        y = max(0, min(screen_size[1], y))

        dots.append((int(x), int(y)))

    return dots

def draw_dots(screen):
    dots = generate_random_dots(50)
    for dot in dots:
        draw_line(screen, dot)
