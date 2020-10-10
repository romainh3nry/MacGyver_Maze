from constant import Constant


class Character:
    """
    class used for MacGyver's moves and items pick up logic
    """

    def __init__(self, icon, level):
        self.icon = icon
        self.level = level
        self.item_count = 0
        self.item = ['N', 'E', 'S', 'T']

    def move(self, x, y, level, direction):
        """
        method used for moving
        """
        if direction == 'right':
            if level.structure[x][y + 1] != 'm':
                if level.structure[x][y + 1] in self.item:
                    self.item_count += 1
                level.structure[x][y] = '0'
                level.structure[x][y + 1] = Constant.constant['player']
                return True
            else:
                return False
        elif direction == 'left':
            if level.structure[x][y - 1] != 'm':
                if level.structure[x][y - 1] in self.item:
                    self.item_count += 1
                level.structure[x][y] = '0'
                level.structure[x][y - 1] = Constant.constant['player']
                return True
            else:
                return False
        elif direction == 'up':
            if level.structure[x - 1][y] != 'm':
                if level.structure[x - 1][y] in self.item:
                    self.item_count += 1
                level.structure[x][y] = '0'
                level.structure[x - 1][y] = Constant.constant['player']
                return True
            else:
                return False
        elif direction == 'down':
            if level.structure[x + 1][y] != 'm':
                if level.structure[x + 1][y] in self.item:
                    self.item_count += 1
                level.structure[x][y] = '0'
                level.structure[x + 1][y] = Constant.constant['player']
                return True
            else:
                return False

    def has_all_items(self):
        """
        check in the player has all the required items
        """
        return self.item_count == 4
