import random


class Level:
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.inventory = 0

    @staticmethod
    def position(maze, position):
        """
        method used to find position in the maze
        """
        for index_line, line in enumerate(maze):
            for index_sprite, sprite in enumerate(line):
                if sprite == position:
                    return index_sprite, index_line

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

    def is_final_boss(self, x, y):
        """
        check if the player is in front of the boss
        """
        return self.structure[x][y] == 'b'
