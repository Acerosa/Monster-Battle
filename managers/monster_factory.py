# Creates a list of monsters for each round
import random
from entities.monster import Monster
from settings import *

class MonsterFactory:
    @staticmethod
    # Makes monsters with random positions for the current round
    def create_round_monsters(round_number, images):
        monsters = []
        for i in range(round_number):
            for monster_type, image in enumerate(images):
                # Set random position for each monster
                x = random.randint(0, WINDOW_WIDTH - 64)
                y = random.randint(SAFE_ZONE_HEIGHT, WINDOW_HEIGHT - BOTTOM_PADDING - 64)
                # Create a monster and add to the list
                monsters.append(Monster(x, y, image, monster_type))
        return monsters