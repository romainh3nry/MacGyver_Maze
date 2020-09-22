from constant import *


class ConsoleMode(Constant):
    """
    Console mode setting class
    """
    def __init__(self):
        Constant.__init__(self)
        self.progress = True

    @staticmethod
    def position(maze, position):
        """
        function used to find position of the hero in the maze
        """
        for index_line, line in enumerate(maze):
            for index_sprite, sprite in enumerate(line):
                if sprite == position:
                    return index_sprite, index_line
