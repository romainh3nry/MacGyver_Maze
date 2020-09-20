import json
import pygame


class Character:
    def __init__(self, icon, level):
        self.constant = self.load_constant()
        self.icon = pygame.transform.scale(pygame.image.load(icon).convert_alpha(), (30, 30))
        self.level = level
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = 0
        self.y = 0
        self.inventory = 0

    @staticmethod
    def load_constant():
        with open('constant.json') as file:
            return json.load(file)

    def move(self, direction):
        if direction == 'right':
            if self.sprite_x < (self.constant['sprite_number'] - 1):
                if self.level.structure[self.sprite_y][self.sprite_x + 1] != 'm':
                    self.sprite_x += 1
                    self.x = self.sprite_x * self.constant['sprite_size']
        elif direction == 'left':
            if self.sprite_x > 0:
                if self.level.structure[self.sprite_y][self.sprite_x - 1] != 'm':
                    self.sprite_x -= 1
                    self.x = self.sprite_x * self.constant['sprite_size']
        elif direction == 'up':
            if self.sprite_y > 0:
                if self.level.structure[self.sprite_y - 1][self.sprite_x] != 'm':
                    self.sprite_y -= 1
                    self.y = self.sprite_y * self.constant['sprite_size']
        elif direction == 'down':
            if self.sprite_y < (self.constant['sprite_number'] - 1):
                if self.level.structure[self.sprite_y + 1][self.sprite_x] != 'm':
                    self.sprite_y += 1
                    self.y = self.sprite_y * self.constant['sprite_size']

    def delete_item(self):
        self.level.structure[self.sprite_y][self.sprite_x] = '0'
        self.inventory += 1
