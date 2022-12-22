import pygame
import sys  # TODO what is that?
import configuration as c

pygame.init()
screen = pygame.display.set_mode((c.screen_width, c.screen_height))  # Устанавливаем рабочую область
print("Hello World")

def game():
    screen.fill(color=0)
    while True:

        keys = pygame.key.get_pressed()  # Нажатия клавиатуры
        game_mouse_pos = pygame.mouse.get_pos()
        # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


game()
