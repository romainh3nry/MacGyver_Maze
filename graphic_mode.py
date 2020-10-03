from level_ui import GraphicLevel
from character import Character
from constant import Constant
import pygame
from pygame.locals import \
    QUIT, \
    KEYDOWN, \
    K_ESCAPE, \
    K_RIGHT, \
    K_LEFT, \
    K_UP, \
    K_DOWN
import time


class GraphicMode:
    """
    Main class for graphical mode game
    """

    def __init__(self):
        self.level = GraphicLevel(Constant.constant['level'])
        self.window_side = \
            Constant.constant['sprite_number'] \
            * Constant.constant['sprite_size']
        self.player = Character(Constant.constant['player'],
                                self.level)
        self.window = pygame.display.set_mode(
            (self.window_side, self.window_side))

    def check_victory(self, x_hero, y_hero):
        """
        this method will check, at every moves,
        if the player is in front of the boss and
        if he has all requirement to win or not
        """
        if self.level.is_final_boss(x_hero, y_hero):
            if self.player.has_all_items():
                font = pygame.font.SysFont('Comic Sans MS', 30)
                self.window.fill('white')
                text = font.render('Victory !', False, (50, 205, 50))
                self.window.blit(text, (170, 190))
                pygame.display.flip()
                time.sleep(3)
                exit()
            else:
                self.window.fill('white')
                font = pygame.font.SysFont('Comic Sans MS', 30)
                text = font.render('You\'re dead...', False, (178, 34, 34))
                self.window.blit(text, (140, 190))
                pygame.display.flip()
                time.sleep(3)
                exit()

    def play(self):
        """
        method used to launch graphical game
        """
        progress = True
        pygame.init()
        pygame.font.init()
        background = pygame.image.load(
            Constant.constant['background']).convert()
        self.window.blit(background, (0, 0))
        self.level.generate()
        self.level.display(self.window)
        x_hero, y_hero = self.level.position(self.level.structure, 'X')
        pygame.display.flip()
        while progress:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            item_collected = font.render(
                'Items : {}'.format(
                    self.player.item_count), False, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    progress = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        progress = False
                    elif event.key == K_RIGHT:
                        self.check_victory(x_hero, y_hero + 1)
                        if self.player.move(
                                x_hero, y_hero, x_hero, y_hero + 1,
                                self.level, Constant.constant['player']):
                            y_hero += 1
                    elif event.key == K_LEFT:
                        self.check_victory(x_hero, y_hero - 1)
                        if self.player.move(
                                x_hero, y_hero, x_hero, y_hero - 1,
                                self.level, Constant.constant['player']):
                            y_hero -= 1
                    elif event.key == K_UP:
                        self.check_victory(x_hero - 1, y_hero)
                        if self.player.move(
                                x_hero, y_hero, x_hero - 1, y_hero,
                                self.level, Constant.constant['player']):
                            x_hero -= 1
                    elif event.key == K_DOWN:
                        self.check_victory(x_hero + 1, y_hero)
                        if self.player.move(
                                x_hero, y_hero, x_hero + 1, y_hero,
                                self.level, Constant.constant['player']):
                            x_hero += 1

            self.window.blit(background, (0, 0))
            self.level.display(self.window)
            self.window.blit(item_collected, (300, 0))
            pygame.display.flip()
