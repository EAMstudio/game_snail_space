import pygame
import sys
from random import randint
import configuration as c

pygame.init()
clock = pygame.time.Clock()

# Load
screen = pygame.display.set_mode((c.screen_width, c.screen_height))  # Устанавливаем рабочую область
rocket = pygame.image.load('Images/Rocket.png').convert_alpha()
rocket = pygame.transform.scale(rocket, (rocket.get_width() // 3, rocket.get_height() // 3))
rocket_position = rocket.get_rect(centerx=c.screen_width / 2, centery=c.screen_height / 2)
# Planets
planet_one = pygame.image.load('Images/object_planet_1.png').convert_alpha()
planet_one = pygame.transform.scale(planet_one, (planet_one.get_width() // 2, planet_one.get_height() // 2))
planet_pos = planet_one.get_rect(centerx=c.screen_width / 2, centery=c.screen_height / 2)

# Program icon and name
pygame.display.set_caption("EAM1studio: Snail Space")
pygame.display.set_icon(pygame.image.load('Images/Rocket.png'))

# Colors
bg_color = (0, 102, 102)


# Planet
class Planet_sprite(pygame.sprite.Sprite):
    """Наследование класса спрайтов"""
    def __init__(self, pos, group):
        super().__init__(group)  # Переносим функцию из родителького класса
        self.image = pygame.image.load('Images/object_planet_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


camera_group = pygame.sprite.Group()
for i in range(20):
    random_x = randint(0, 1000)
    random_y = randint(0, 1000)
    Planet_sprite(pos=(random_x, random_y), group=camera_group)
speed = 10


def game():
    while True:

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
        elif keys[pygame.K_UP]:
            rocket_position.y -= speed
            if rocket_position.y < 0:
                rocket_position.y = 0
        elif keys[pygame.K_DOWN]:
            rocket_position.y += speed
            if rocket_position.y > c.screen_height - rocket_position.height:
                rocket_position.y = c.screen_height - rocket_position.height

        screen.fill(bg_color)
        screen.blit(rocket, rocket_position)
        screen.blit(planet_one, planet_pos)

        camera_group.draw(screen)
        camera_group.update()

        pygame.display.update()

        clock.tick(c.FPS)


game()
