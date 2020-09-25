from constant import Constant


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
        self.item_count = 0
        self.item = ['N', 'E', 'S', 'T']

    def ui_move(self, direction):
        if direction == 'right':
            if self.sprite_x < (self.constant['sprite_number'] - 1):
                if self.level.structure[
                    self.sprite_y][
                    self.sprite_x + 1]\
                        != 'm':
                    self.sprite_x += 1
                    self.x = self.sprite_x * self.constant['sprite_size']
        elif direction == 'left':
            if self.sprite_x > 0:
                if self.level.structure[
                    self.sprite_y][
                    self.sprite_x - 1]\
                        != 'm':
                    self.sprite_x -= 1
                    self.x = self.sprite_x * self.constant['sprite_size']
        elif direction == 'up':
            if self.sprite_y > 0:
                if self.level.structure[
                    self.sprite_y - 1][
                    self.sprite_x] \
                        != 'm':
                    self.sprite_y -= 1
                    self.y = self.sprite_y * self.constant['sprite_size']
        elif direction == 'down':
            if self.sprite_y < (self.constant['sprite_number'] - 1):
                if self.level.structure[
                    self.sprite_y + 1][
                    self.sprite_x] \
                        != 'm':
                    self.sprite_y += 1
                    self.y = self.sprite_y * self.constant['sprite_size']

    def console_move(self, x_before, y_before, x_new, y_new, level, hero):
        if level.structure[x_new][y_new] != 'm':
            if level.structure[x_new][y_new] in self.item:
                self.item_count += 1
            level.structure[x_before][y_before] = '0'
            level.structure[x_new][y_new] = hero
            return True
        else:
            return False

    def delete_item(self):
        self.level.structure[self.sprite_y][self.sprite_x] = '0'
        self.inventory += 1
