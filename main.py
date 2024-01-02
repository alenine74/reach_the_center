import time
from utils import create_screen, create_center_dot, draw_dots

screen = create_screen()

center_dot = create_center_dot(screen)

draw_dots(screen)

time.sleep(3)
