import pygame
import sys
import configuration as c

pygame.init()
clock = pygame.time.Clock()

# Load
screen = pygame.display.set_mode((c.screen_width, c.screen_height))  # Устанавливаем рабочую область
rocket = pygame.image.load('Images/Rocket.png').convert_alpha()
rocket_position = rocket.get_rect(centerx=c.screen_width / 2, centery=c.screen_height / 2)
# Planets
planet_one = pygame.image.load('Images/object_planet_1.png').convert_alpha()
planet_pos = planet_one.get_rect(centerx=c.screen_width / 2, centery=c.screen_height / 2)

# Program icon and name
pygame.display.set_caption("EAM1studio: Snail Space")
pygame.display.set_icon(pygame.image.load('Images/Rocket.png'))

# Colors
bg_color = (0, 102, 102)



speed = 10

def game():
    while True:

        keys = pygame.key.get_pressed()  # Нажатия клавиатуры
        game_mouse_pos = pygame.mouse.get_pos()
        # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rocket_position.x -= speed
            if rocket_position.x < 0:
                rocket_position.x = 0
        elif keys[pygame.K_RIGHT]:
            rocket_position.x += speed
            if rocket_position.x > c.screen_width - rocket_position.width:
                rocket_position.x = c.screen_width - rocket_position.width

        screen.fill(bg_color)
        screen.blit(rocket, rocket_position)
        screen.blit(planet_one, planet_pos)
        pygame.display.update()

        clock.tick(c.FPS)


game()
