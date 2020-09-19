import pygame
import json


class Level:
    def __init__(self):
        self.constant = self.load_constant()
        self.file = self.constant['level_txt']
        self.structure = []

    @staticmethod
    def load_constant():
        with open('constant.json') as file:
            return json.load(file)

    def generate(self):
        with open(self.file) as file:
            level_structure = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                level_structure.append(line_level)
            self.structure = level_structure

    def display(self, window):
        wall = pygame.image.load(self.constant['wall_picture']).convert()
        line_number = 0
        for line in self.structure:
            sprite_number = 0
            for sprite in line:
                x = sprite_number * self.constant['sprite_size']
                y = line_number * self.constant['sprite_size']
                if sprite == 'm':
                    window.blit(wall, (x, y))
                sprite_number += 1
            line_number += 1
