# Tests for the Player class
import unittest
import pygame
from entities.player import Player
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from unittest.mock import MagicMock

# Mock sound class to stop real sound playing
class MockSounds(dict):
    def __getitem__(self, item):
        return MagicMock()

# Check the player's position, warp, and reset functions
class PlayerTestCase(unittest.TestCase):
    # Create a player before each test
    def setUp(self):
        pygame.init()
        self.player = Player(pygame.Surface((64, 64)), sounds=MockSounds())

    # Check player starts in the middle bottom of the screen
    def test_initial_position(self):
        self.assertEqual(self.player.rect.centerx, WINDOW_WIDTH // 2)
        self.assertEqual(self.player.rect.bottom, WINDOW_HEIGHT)

    # Check warp uses one warp and plays sound
    def test_warp_decreases_warps(self):
        self.player.warps = 2
        original_warps = self.player.warps
        self.player.warp()
        self.assertEqual(self.player.warps, original_warps - 1)
        self.player.sounds["warp"].play.assert_called_once()

    # Check warp does not play sound if no warps left
    def test_warp_does_not_play_sound_when_no_warps_left(self):
        self.player.warps = 0
        self.player.warp()
        self.player.sounds["warp"].play.assert_not_called()

    # Check reset moves player to the starting place
    def test_reset_resets_position(self):
        self.player.rect.centerx = 100
        self.player.reset()
        self.assertEqual(self.player.rect.centerx, WINDOW_WIDTH // 2)

if __name__ == '__main__':
    unittest.main()