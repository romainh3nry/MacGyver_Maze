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
        self.hero = Character('X', self.level)

    def play(self):
        """
        method used to launch console game
        """
        self.level.generate()
        hero = 'X'
        x_hero, y_hero = self.level.position(self.level.structure, hero)
        while self.progress:
            print('Item : {}'.format(self.hero.item_count))
            for elt in self.level.structure:
                print("".join(elt))
            direction = input('Choose a direction: ')
            if direction == 'd':
                if self.hero.console_move(
                        x_hero, y_hero, x_hero, y_hero + 1, self.level, hero):
                    y_hero += 1
            elif direction == 'q':
                if self.hero.console_move(
                        x_hero, y_hero, x_hero, y_hero - 1, self.level, hero):
                    y_hero -= 1
            elif direction == 's':
                if self.hero.console_move(
                        x_hero, y_hero, x_hero + 1, y_hero, self.level, hero):
                    x_hero += 1
            elif direction == 'z':
                if self.hero.console_move(
                        x_hero, y_hero, x_hero - 1, y_hero, self.level, hero):
                    x_hero -= 1

            if self.level.structure[x_hero][y_hero + 1] == 'b':
                if self.hero.item_count < 4:
                    self.progress = False
                    print('You\'re dead !!')
                else:
                    self.progress = False
                    print('You win... but what did you expect? '
                          'you\'re Macgyver !')
