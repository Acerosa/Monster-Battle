# Loads images, fonts, and sounds for the game
import pygame

class AssetManager:
    def __init__(self):
        # Monster images by colour
        self.monster_images = [
            pygame.image.load("assets/blue_monster.png"),
            pygame.image.load("assets/green_monster.png"),
            pygame.image.load("assets/purple_monster.png"),
            pygame.image.load("assets/yellow_monster.png"),
        ]
        self.knight = pygame.image.load("assets/knight.png")
        # Main font used in the game
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)

        # Game sounds
        self.sounds = {
            "catch": pygame.mixer.Sound("assets/catch.wav"),
            "die": pygame.mixer.Sound("assets/die.wav"),
            "warp": pygame.mixer.Sound("assets/warp.wav"),
            "next_level": pygame.mixer.Sound("assets/next_level.wav"),
        }