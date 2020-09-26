from graphic_level import GraphicLevel
from character import Character, Constant
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


class GraphicMode(Constant):
    """
    Main class for graphical mode game
    """
    def __init__(self):
        Constant.__init__(self)
        self.level = GraphicLevel(self.constant['level_txt'])
        self.window_side = \
            self.constant['sprite_number'] * self.constant['sprite_size']

    def play(self):
        """
        method used to launch graphical game
        """
        progress = True
        pygame.init()
        pygame.font.init()
        window = pygame.display.set_mode((self.window_side, self.window_side))
        background = pygame.image.load(self.constant['background']).convert()
        window.blit(background, (0, 0))
        self.level.generate()
        self.level.display(window)
        hero = Character(
            pygame.transform.scale(
                pygame.image.load(self.constant['macgyver']).convert_alpha(),
                (30, 30)),
            self.level)
        pygame.display.flip()
        while progress:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            item_collected = font.render(
                'Items : {}'.format(hero.inventory), False, (255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    progress = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        progress = False
                    elif event.key == K_RIGHT:
                        hero.ui_move('right')
                    elif event.key == K_LEFT:
                        hero.ui_move('left')
                    elif event.key == K_UP:
                        hero.ui_move('up')
                    elif event.key == K_DOWN:
                        hero.ui_move('down')

            window.blit(background, (0, 0))
            self.level.display(window)
            window.blit(hero.icon, (hero.x, hero.y))
            window.blit(item_collected, (300, 0))
            pygame.display.flip()

            if self.level.structure[hero.sprite_y][hero.sprite_x] == 'N':
                hero.delete_item()
            elif self.level.structure[hero.sprite_y][hero.sprite_x] == 'E':
                hero.delete_item()
            elif self.level.structure[hero.sprite_y][hero.sprite_x] == 'S':
                hero.delete_item()
            elif self.level.structure[hero.sprite_y][hero.sprite_x] == 'T':
                hero.delete_item()
            elif self.level.structure[hero.sprite_y][hero.sprite_x] == 'b':
                if hero.inventory != 4:
                    window.fill('white')
                    font = pygame.font.SysFont('Comic Sans MS', 30)
                    text = font.render('You\'re dead...', False, (178, 34, 34))
                    window.blit(text, (140, 190))
                    pygame.display.flip()
                    time.sleep(3)
                    progress = False
            elif self.level.structure[hero.sprite_y][hero.sprite_x] == 'a':
                window.fill('white')
                text = font.render('Victory !', False, (50, 205, 50))
                window.blit(text, (170, 190))
                pygame.display.flip()
                time.sleep(3)
                progress = False
