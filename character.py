class Character:
    """
    class used for MacGyver's moves and items pick up logic
    """

    def __init__(self, icon, level):
        self.icon = icon
        self.level = level
        self.item_count = 0
        self.item = ['N', 'E', 'S', 'T']

    def move(self, x_before, y_before, x_new, y_new, level, icon):
        """
        method used for moving on console mode
        """
        if level.structure[x_new][y_new] != 'm':
            if level.structure[x_new][y_new] in self.item:
                self.item_count += 1
            level.structure[x_before][y_before] = '0'
            level.structure[x_new][y_new] = icon
            return True
        else:
            return False

    def has_all_items(self):
        """
        check in the player has all the required items
        """
        return self.item_count == 4
