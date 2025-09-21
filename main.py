import pygame
from settings import *
from managers.game_manager import GameManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Monster Wrangler")
    clock = pygame.time.Clock()
    game_manager = GameManager(screen)

    game_manager.start_screen()
    game_manager.new_round()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_manager.handle_event(event)

        screen.fill(BLACK)

        game_manager.update()
        game_manager.draw()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()