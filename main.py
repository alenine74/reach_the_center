import time
import pygame
from utils import create_screen, create_center_dot, draw_dots


def main():
    screen = create_screen()
    create_center_dot(screen)
    draw_dots(screen)
    time.sleep(5) 
    
    pygame.image.save(screen, "final_image.png")
    print("Image saved as 'final_image.png'.")


if __name__ == "__main__":
    main()
