from level import Level
from character import Character, Constant


class ConsoleMode(Constant):
    """
    Main class for console mode game
    """
    def __init__(self):
        Constant.__init__(self)
        self.level = Level(self.constant['level'])
        self.player = Character(self.constant['player'], self.level)

    def play(self):
        """
        method used to launch console game
        """
        progress = True
        self.level.generate()
        x_hero, y_hero = self.level.position(
            self.level.structure, self.constant['player'])
        while progress:
            print('Item : {}'.format(self.player.item_count))
            for elt in self.level.structure:
                print("".join(elt))
            direction = input('Choose a direction: ')
            if direction == 'd':
                if self.player.move(
                        x_hero, y_hero, x_hero, y_hero + 1,
                        self.level, self.constant['player']):
                    y_hero += 1
            elif direction == 'q':
                if self.player.move(
                        x_hero, y_hero, x_hero, y_hero - 1,
                        self.level, self.constant['player']):
                    y_hero -= 1
            elif direction == 's':
                if self.player.move(
                        x_hero, y_hero, x_hero + 1, y_hero,
                        self.level, self.constant['player']):
                    x_hero += 1
            elif direction == 'z':
                if self.player.move(
                        x_hero, y_hero, x_hero - 1, y_hero,
                        self.level, self.constant['player']):
                    x_hero -= 1

            if self.level.structure[x_hero][y_hero + 1] == 'b':
                if self.player.item_count < 4:
                    self.player.has_lose(mode='console')
                    progress = False
                else:
                    self.player.has_win(mode='console')
                    progress = False
