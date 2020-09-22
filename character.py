from constant import *


class Character(Constant):
    """
    class used for Macgyver's moves and items pick up logic
    """
    def __init__(self, icon, level):
        Constant.__init__(self)
        self.icon = icon
        self.level = level
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = 0
        self.y = 0
        self.inventory = 0

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
