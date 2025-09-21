# Monster class used in the game
# Moves around the screen and bounces off the edges
import pygame
import random
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        # Set image and position
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.type = monster_type
        # Choose a random direction and speed
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    def update(self):
        # Move the monster
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        # Bounce off the screen edges
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx *= -1
        if self.rect.top <= SAFE_ZONE_HEIGHT or self.rect.bottom >= WINDOW_HEIGHT - BOTTOM_PADDING:
            self.dy *= -1