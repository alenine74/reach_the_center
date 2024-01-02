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

def draw_line(screen, start_pos, end_pos):
    line_thickness = 4 
    pygame.draw.line(screen, pygame.Color(line_draw_color), start_pos, end_pos, line_thickness)
    pygame.display.update()
    time.sleep(0.1)

def draw_dot(screen, pos):
    dot_radius = 3 
    pygame.draw.circle(screen, pygame.Color(screen_dots_color), pos, dot_radius)
    pygame.display.update()

def is_out_of_bounds(point):
    return not (0 <= point[0] < screen_size[0] and 0 <= point[1] < screen_size[1])

def generate_path_to_edge(screen):
    current_point = center_dot_position
    dots_count = 0
    while not is_out_of_bounds(current_point):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(10, 30)
        new_x = int(current_point[0] + distance * math.cos(angle))
        new_y = int(current_point[1] + distance * math.sin(angle))
        new_point = (new_x, new_y)
        if not is_out_of_bounds(new_point):
            draw_dot(screen, new_point)
            dots_count += 1
        current_point = new_point
    return current_point, dots_count

def draw_paths(screen, num_paths):
    total_dots_count = 0
    edge_points_count = 0
    for _ in range(num_paths):
        edge_point, dots_count = generate_path_to_edge(screen)
        total_dots_count += dots_count
        if is_out_of_bounds(edge_point):
            edge_points_count += 1
        draw_line(screen, center_dot_position, edge_point)
    print(f"Number of points that reached the edge: {edge_points_count}")
    print(f"Total number of dots drawn: {total_dots_count}")



def draw_dots(screen):
    draw_paths(screen, 50)
