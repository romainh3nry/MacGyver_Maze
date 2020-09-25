import pygame
import random
from constant import *


class Level(Constant):
    def __init__(self, file):
        Constant.__init__(self)
        self.file = file
        self.structure = []
        self.inventory = 0

    def generate(self):
        """
        maze generating
        """
        with open(self.file) as file:
            level_structure = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                level_structure.append(line_level)
        while self.inventory < 4:
            item_x = random.randint(0, 14)
            item_y = random.randint(0, 14)
            if level_structure[item_y][item_x] == '0':
                if self.inventory == 0:
                    level_structure[item_y][item_x] = 'N'
                elif self.inventory == 1:
                    level_structure[item_y][item_x] = 'E'
                elif self.inventory == 2:
                    level_structure[item_y][item_x] = 'S'
                elif self.inventory == 3:
                    level_structure[item_y][item_x] = 'T'
                self.inventory += 1
        self.structure = level_structure

