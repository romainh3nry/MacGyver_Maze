from level import *


class ConsoleMode:
    def __init__(self):
        self.constant = self.load_constant()
        self.progress = True

    @staticmethod
    def load_constant():
        with open('constant.json') as file:
            return json.load(file)

    def position(self, maze, position):
        for index_line, line in enumerate(maze):
            for index_sprite, sprite in enumerate(line):
                if sprite == position:
                    return index_sprite, index_line

