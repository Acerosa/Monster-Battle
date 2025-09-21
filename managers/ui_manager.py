# Draws game information (HUD) on the screen
from settings import *

class UIManager:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    # Shows score, lives, round, time, warps, and target monster
    def draw_hud(self, game, player):
        score_text = self.font.render(f"Score: {game.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {player.lives}", True, WHITE)
        round_text = self.font.render(f"Round: {game.round_number}", True, WHITE)
        time_text = self.font.render(f"Time: {game.round_time}", True, WHITE)
        warps_text = self.font.render(f"Warps: {player.warps}", True, WHITE)
        catch_text = self.font.render("Current Catch", True, WHITE)

        self.screen.blit(score_text, (5, 5))
        self.screen.blit(lives_text, (5, 35))
        self.screen.blit(round_text, (5, 65))
        self.screen.blit(time_text, (WINDOW_WIDTH - 180, 5))
        self.screen.blit(warps_text, (WINDOW_WIDTH - 180, 35))
        self.screen.blit(catch_text, (WINDOW_WIDTH//2 - 100, 5))

        # Show the image of the current monster to catch
        rect = game.target_image.get_rect(centerx=WINDOW_WIDTH // 2, top=30)
        self.screen.blit(game.target_image, rect)