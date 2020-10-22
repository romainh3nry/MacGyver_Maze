from constant.constant import Constant


class Character:
    """
    class used for MacGyver's moves and items pick up logic
    """

    def __init__(self, icon, level):
        self.icon = icon
        self.level = level
        self.item_count = 0
        self.item = ['N', 'E', 'S', 'T']

    def move(self, x, y, direction):
        if direction == 'right':
            if self.is_moving_to(x, y, x, y + 1):
                return True
        elif direction == 'left':
            if self.is_moving_to(x, y, x, y - 1):
                return True
        elif direction == 'up':
            if self.is_moving_to(x, y, x - 1, y):
                return True
        elif direction == 'down':
            if self.is_moving_to(x, y, x + 1, y):
                return True

    def has_all_items(self):
        """
        check in the player has all the required items
        """
        return self.item_count == 4

    def get_item_count(self):
        return self.item_count

    def is_moving_to(self, x_before, y_before, x_new, y_new):
        if self.level.is_not_wall(x_new, y_new):
            if self.level.maze_structure()[x_new][y_new] in self.item:
                self.item_count += 1
            self.level.maze_structure()[x_before][y_before] = '0'
            self.level.maze_structure()[x_new][y_new] = (
                Constant.constant['player'])
            return True
        else:
            return False
