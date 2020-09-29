from constant import Constant
import pygame
import time


class Character(Constant):
    """
    class used for MacGyver's moves and items pick up logic
    """

    def __init__(self, icon, level):
        Constant.__init__(self)
        self.icon = icon
        self.level = level
        self.item_count = 0
        self.item = ['N', 'E', 'S', 'T']

    def move(self, x_before, y_before, x_new, y_new, level, icon):
        """
        method used for moving on console mode
        """
        if level.structure[x_new][y_new] != 'm':
            if level.structure[x_new][y_new] in self.item:
                self.item_count += 1
            level.structure[x_before][y_before] = '0'
            level.structure[x_new][y_new] = icon
            return True
        else:
            return False

    def has_win(self, mode, *window):
        if mode == 'ui' and window[0]:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            window[0].fill('white')
            text = font.render('Victory !', False, (50, 205, 50))
            window[0].blit(text, (170, 190))
            pygame.display.flip()
            time.sleep(3)
        elif mode == 'console':
            print('You win... but what did you expect? '
                  'you\'re Macgyver !')

    def has_lose(self, mode, *window):
        if mode == 'ui' and window[0]:
            window[0].fill('white')
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = font.render('You\'re dead...', False, (178, 34, 34))
            window[0].blit(text, (140, 190))
            pygame.display.flip()
            time.sleep(3)
        elif mode == 'console':
            print('You\'re dead !!')
