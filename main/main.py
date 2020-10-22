import logging

from mode.console_mode import ConsoleMode
from constant.constant import Constant
from mode.graphic_mode import GraphicMode


class MainClass:
    def __init__(self):
        Constant.load_constant()
        self.mode_choice = self.playing_mode()
        if self.mode_choice == 1:
            GraphicMode().play()
        elif self.mode_choice == 2:
            ConsoleMode().play()

    def playing_mode(self):
        """
        method used for choosing graphic or console mode
        """
        choice = input('Please choose the mode you want to play: \n1 - '
                       'Graphic mode\n2 - Console mode\n3 - Quit\n:')
        try:
            choice = int(choice)
            assert 0 < choice < 4
        except ValueError:
            logging.error('The choice has to be digit')
            return self.playing_mode()
        except AssertionError:
            logging.error('The choice has to be digit between 1 and 3')
            return self.playing_mode()
        if choice == 3:
            exit()
        return choice
