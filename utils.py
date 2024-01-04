import random
import time
import pygame
import math
from config import screen_size, center_dot_position, background_color, center_dot_color


def _distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def _new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill(background_color)
    pygame.display.update()
    _create_center_dot(screen)
    return screen


def _create_center_dot(screen):
    pygame.draw.circle(screen, pygame.Color(center_dot_color), center_dot_position, 5)
    pygame.display.update()


def _draw_line(screen, color, start_pos, end_pos):
    line_thickness = 2
    pygame.draw.line(screen, pygame.Color(color), start_pos, end_pos, line_thickness)
    pygame.display.update()
    time.sleep(0.1)


def _is_out_of_bounds(point):
    return not (0 <= point[0] < screen_size[0] and 0 <= point[1] < screen_size[1])


def _generate_path_to_edge(screen):
    last_point = 0
    current_point = center_dot_position
    dots_count = 0
    line_color = _new_color()
    while not _is_out_of_bounds(current_point):
        angle = random.uniform(0, 2 * math.pi)
        coefficient = random.uniform(150, 200)
        new_x = abs(coefficient * math.cos(angle))
        new_y = abs(coefficient * math.sin(angle))
        new_point = (random.randint(0, 800), random.randint(0, 800))
        # print(new_point)
        # new_point = (new_x, new_y)
        ex_distance = _distance(center_dot_position, current_point)
        new_distance = _distance(center_dot_position, new_point)
        if new_distance > ex_distance:
            if not _is_out_of_bounds(new_point):
                _draw_line(screen, line_color, current_point, new_point)
                dots_count += 1
                last_point = new_point
            current_point = new_point
    _draw_line(screen, line_color, last_point, current_point)
    return current_point, dots_count


def draw_paths(screen, num_paths):
    total_dots_count = 0
    edge_points_count = 0
    for _ in range(num_paths):
        edge_point, dots_count = _generate_path_to_edge(screen)
        total_dots_count += dots_count
        if _is_out_of_bounds(edge_point):
            edge_points_count += 1
    print(f"Number of points that reached the edge: {edge_points_count}")
    print(f"Total number of dots drawn: {total_dots_count}")
