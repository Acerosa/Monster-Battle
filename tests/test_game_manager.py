# Tests for the GameManager class
import unittest
import pygame
from managers.game_manager import GameManager

# A simple mock screen for testing without real drawing
class DummyScreen:
    def fill(self, color): pass
    def blit(self, *args): pass

# Unit tests for game setup and round logic
class GameManagerTestCase(unittest.TestCase):
    # Prepare a game with a dummy screen before each test
    def setUp(self):
        pygame.init()
        self.screen = DummyScreen()
        self.game = GameManager(self.screen)

    # Check if score starts at zero
    def test_game_starts_with_score_zero(self):
        self.assertEqual(self.game.score, 0)

    # Check if round number goes up after new round
    def test_new_round_increases_round_number(self):
        self.game.new_round()
        self.assertEqual(self.game.round_number, 1)

    # Check if a target monster is chosen with valid type
    def test_choose_target_sets_target_type_and_image(self):
        self.game.new_round()
        self.assertIsNotNone(self.game.target_image)
        self.assertIn(self.game.target_type, [0, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()