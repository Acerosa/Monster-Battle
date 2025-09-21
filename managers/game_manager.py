# Manages the game state, rounds, player, and collisions
import random
import pygame
from managers.asset_manager import AssetManager
from managers.ui_manager import UIManager
from managers.monster_factory import MonsterFactory
from entities.player import Player
from settings import *

class GameManager:
    # Set up the game manager with player, assets, and screen
    def __init__(self, screen):
        self.screen = screen
        self.assets = AssetManager()
        self.ui = UIManager(screen, self.assets.font)

        self.player = Player(self.assets.knight, self.assets.sounds)
        self.player_group = pygame.sprite.Group(self.player)
        self.monsters = pygame.sprite.Group()

        self.score = 0
        self.round_number = 0
        self.round_time = 0
        self.frame_count = 0

        self.target_type = None
        self.target_image = None

    # Show the start screen and reset the game
    def start_screen(self):
        self._pause("Monster Wrangler", "Press Enter to Start")
        self.reset_game()

    # Handle player key inputs
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.warp()

    # Update all game elements
    def update(self):
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        self.player_group.update()
        self.monsters.update()

        self._check_collision()

    # Draw all game elements to the screen
    def draw(self):
        self.player_group.draw(self.screen)
        self.monsters.draw(self.screen)
        self.ui.draw_hud(self, self.player)

    # Start a new round and create new monsters
    def new_round(self):
        self.score += int(10000 * self.round_number / (1 + self.round_time))
        self.round_number += 1
        self.round_time = 0
        self.frame_count = 0
        self.player.warps += 1
        self.player.reset()

        self.monsters.empty()
        for monster in MonsterFactory.create_round_monsters(self.round_number, self.assets.monster_images):
            self.monsters.add(monster)

        self._choose_target()
        self.assets.sounds["next_level"].play()

    # Reset score, lives, and round
    def reset_game(self):
        self.score = 0
        self.round_number = 0
        self.player.lives = 5
        self.player.warps = 2
        self.new_round()

    # Pick a random monster as the target
    def _choose_target(self):
        target = random.choice(self.monsters.sprites())
        self.target_type = target.type
        self.target_image = target.image

    # Check if player catches the correct or wrong monster
    def _check_collision(self):
        hit = pygame.sprite.spritecollideany(self.player, self.monsters)
        if hit:
            if hit.type == self.target_type:
                self.assets.sounds["catch"].play()
                self.score += 100 * self.round_number
                hit.kill()
                if self.monsters:
                    self._choose_target()
                else:
                    self.new_round()
            else:
                self.assets.sounds["die"].play()
                self.player.lives -= 1
                if self.player.lives <= 0:
                    self._pause(f"Final Score: {self.score}", "Press Enter to Restart")
                    self.reset_game()
                self.player.reset()

    # Pause the game with a message
    def _pause(self, main_text, sub_text):
        main = self.assets.font.render(main_text, True, WHITE)
        sub = self.assets.font.render(sub_text, True, WHITE)
        main_rect = main.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        sub_rect = sub.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))

        self.screen.fill(BLACK)
        self.screen.blit(main, main_rect)
        self.screen.blit(sub, sub_rect)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
                elif event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    exit()