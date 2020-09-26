from level import Level


class ConsoleLevel(Level):
    def __init__(self, file):
        Level.__init__(self, file)
        self.file = file

    @staticmethod
    def position(maze, position):
        """
        method used to find position in the maze
        """
        for index_line, line in enumerate(maze):
            for index_sprite, sprite in enumerate(line):
                if sprite == position:
                    return index_sprite, index_line
