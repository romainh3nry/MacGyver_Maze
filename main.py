from pygame.locals import *
from level import *
from character import *
import json
import pygame


class MainClass:
    def __init__(self):
        self.constant = self.load_constant()
        self.level = Level()
        self.progress = True
        self.window_side = self.constant['sprite_number'] * self.constant['sprite_size']
        self.play()

    @staticmethod
    def load_constant():
        with open('constant.json') as file:
            return json.load(file)

    def play(self):
        pygame.init()
        window = pygame.display.set_mode((self.window_side, self.window_side))
        background = pygame.image.load(self.constant['background_picture']).convert()
        window.blit(background, (0, 0))
        self.level.generate()
        self.level.display(window)
        hero = Character(self.constant['macgyver_picture'], self.level)
        pygame.display.flip()
        while self.progress:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.progress = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.progress = False
                    elif event.key == K_RIGHT:
                        hero.move('right')
                    elif event.key == K_LEFT:
                        hero.move('left')
                    elif event.key == K_UP:
                        hero.move('up')
                    elif event.key == K_DOWN:
                        hero.move('down')

            window.blit(background, (0, 0))
            self.level.display(window)
            window.blit(hero.icon, (hero.x, hero.y))
            pygame.display.flip()
