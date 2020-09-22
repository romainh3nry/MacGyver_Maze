from constant import *


class ConsoleMode(Constant):
    def __init__(self):
        Constant.__init__(self)
        self.progress = True

    def position(self, maze, position):
        for index_line, line in enumerate(maze):
            for index_sprite, sprite in enumerate(line):
                if sprite == position:
                    return index_sprite, index_line
