from console_level import ConsoleLevel
from character import Character, Constant


class ConsoleMode(Constant):
    """
    Main class for console mode game
    """
    def __init__(self):
        Constant.__init__(self)
        self.progress = True
        self.level = ConsoleLevel(self.constant['level_txt_console'])
        self.player = Character(self.constant['player'], self.level)

    def play(self):
        """
        method used to launch console game
        """
        self.level.generate()
        x_hero, y_hero = self.level.position(
            self.level.structure, self.constant['player'])
        while self.progress:
            print('Item : {}'.format(self.player.item_count))
            for elt in self.level.structure:
                print("".join(elt))
            direction = input('Choose a direction: ')
            if direction == 'd':
                if self.player.console_move(
                        x_hero, y_hero, x_hero, y_hero + 1,
                        self.level, self.constant['player']):
                    y_hero += 1
            elif direction == 'q':
                if self.player.console_move(
                        x_hero, y_hero, x_hero, y_hero - 1,
                        self.level, self.constant['player']):
                    y_hero -= 1
            elif direction == 's':
                if self.player.console_move(
                        x_hero, y_hero, x_hero + 1, y_hero,
                        self.level, self.constant['player']):
                    x_hero += 1
            elif direction == 'z':
                if self.player.console_move(
                        x_hero, y_hero, x_hero - 1, y_hero,
                        self.level, self.constant['player']):
                    x_hero -= 1

            if self.level.structure[x_hero][y_hero + 1] == 'b':
                if self.player.item_count < 4:
                    self.progress = False
                    print('You\'re dead !!')
                else:
                    self.progress = False
                    print('You win... but what did you expect? '
                          'you\'re Macgyver !')
