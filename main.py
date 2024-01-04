import time
import pygame
from utils import create_screen, draw_paths


def main():
    screen = create_screen()
    draw_paths(screen, 50)
    time.sleep(5)

    pygame.image.save(screen, "final_image.png")
    print("Image saved as 'final_image.png'.")


if __name__ == "__main__":
    main()
