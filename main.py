import time
from utils import create_screen, create_center_dot, draw_dots


def main():
    screen = create_screen()
    create_center_dot(screen)
    draw_dots(screen)
    time.sleep(5)


if __name__ == "__main__":
    main()
