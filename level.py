import pygame
import json
import random


class Level:
    def __init__(self):
        self.constant = self.load_constant()
        self.file = self.constant['level_txt']
        self.structure = []
        self.inventory = 0

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

    def display(self, window):
        wall = pygame.transform.scale(pygame.image.load(self.constant['wall_picture']).convert_alpha(), (30, 30))
        floor = pygame.transform.scale(pygame.image.load(self.constant['floor_picture']).convert_alpha(), (30, 30))
        flag = pygame.transform.scale(pygame.image.load(self.constant['flag_picture']).convert_alpha(), (30, 30))
        bad_guy = pygame.transform.scale(pygame.image.load(self.constant['bad_guy_picture']).convert_alpha(), (30, 30))
        needle = pygame.transform.scale(pygame.image.load(self.constant['needle_picture']).convert(), (30, 30))
        ether = pygame.transform.scale(pygame.image.load(self.constant['ether_picture']).convert(), (30, 30))
        syringe = pygame.transform.scale(pygame.image.load(self.constant['syringe_picture']).convert(), (30, 30))
        tube = pygame.transform.scale(pygame.image.load(self.constant['tube_picture']).convert(), (30, 30))
        line_number = 0
        for line in self.structure:
            sprite_number = 0
            for sprite in line:
                x = sprite_number * self.constant['sprite_size']
                y = line_number * self.constant['sprite_size']
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == '0':
                    window.blit(floor, (x, y))
                elif sprite == 'd' or sprite == 'a':
                    window.blit(flag, (x, y))
                elif sprite == 'b':
                    window.blit(floor, (x, y))
                    window.blit(bad_guy, (x, y))
                elif sprite == 'N':
                    window.blit(floor, (x, y))
                    window.blit(needle, (x, y))
                elif sprite == 'E':
                    window.blit(floor, (x, y))
                    window.blit(ether, (x, y))
                elif sprite == 'S':
                    window.blit(floor, (x, y))
                    window.blit(syringe, (x, y))
                elif sprite == 'T':
                    window.blit(floor, (x, y))
                    window.blit(tube, (x, y))
                sprite_number += 1
            line_number += 1
