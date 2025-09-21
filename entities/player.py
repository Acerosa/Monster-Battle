# Player class controlled by the user
# Can move, warp, and reset position
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image, sounds):
        super().__init__()
        # Set image and start position
        self.image = image
        self.rect = self.image.get_rect(centerx=WINDOW_WIDTH//2, bottom=WINDOW_HEIGHT)
        # Set starting values
        self.velocity = 8
        self.lives = 5
        self.warps = 2
        self.sounds = sounds

    def update(self):
        # Move player based on arrow key input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > SAFE_ZONE_HEIGHT:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - BOTTOM_PADDING:
            self.rect.y += self.velocity

    def warp(self):
        # Move player to bottom of screen if warps available
        if self.warps > 0:
            self.warps -= 1
            self.sounds["warp"].play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        # Return player to starting position
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT
