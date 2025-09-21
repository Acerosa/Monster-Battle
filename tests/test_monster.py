# Tests for the Monster class
import unittest
import pygame
from entities.monster import Monster

# Check monster setup and attributes
class MonsterTestCase(unittest.TestCase):
    # Create a monster before each test
    def setUp(self):
        pygame.init()
        self.image = pygame.Surface((64, 64))
        self.monster = Monster(100, 100, self.image, monster_type=2)

    # Check the monster starts in the correct place
    def test_monster_initial_position(self):
        self.assertEqual(self.monster.rect.topleft, (100, 100))

    # Check the monster has the correct type
    def test_monster_type(self):
        self.assertEqual(self.monster.type, 2)

if __name__ == '__main__':
    unittest.main()