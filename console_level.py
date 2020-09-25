from level import Level


class ConsoleLevel(Level):
    def __init__(self, file):
        Level.__init__(self, file)
        self.file = file

    @staticmethod
    def position(maze, position):
        """
        function used to find position of the hero in the maze
        """
        for index_line, line in enumerate(maze):
            for index_sprite, sprite in enumerate(line):
                if sprite == position:
                    return index_sprite, index_line
