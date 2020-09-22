"""
game progression file
"""
import pygame
from pygame.locals import *
from level import *
from character import *
from console_mode import *
from constant import *
import time


class MainClass(Constant):
    def __init__(self):
        Constant.__init__(self)
        self.level = Level(self.constant['level_txt'])
        self.console_mode = ConsoleMode()
        self.progress = True
        self.item_count = 0
        self.item = ['N', 'E', 'S', 'T']
        self.window_side = self.constant['sprite_number'] * self.constant['sprite_size']
        self.mode_choice = self.playing_mode()
        if self.mode_choice == 1:
            self.play_graphic_mode()
        elif self.mode_choice == 2:
            self.play_console_mode()

    def playing_mode(self):
        """
        Fonction uses for choosing graphic or console mode
        """
        choice = input('Please choose the mode you want to play: \n1 - Graphic mode\n2 - Console mode\n3 - Quit\n:')
        try:
            choice = int(choice)
            assert 0 < choice < 4
        except ValueError:
            print('The choice has to be digit')
            return self.playing_mode()
        except AssertionError:
            print('The choice has to be digit between 1 and 3')
            return self.playing_mode()
        if choice == 3:
            exit()
        return choice

    def play_graphic_mode(self):
        """
        Graphic mode progression function
        """
        pygame.init()
        pygame.font.init()
        window = pygame.display.set_mode((self.window_side, self.window_side))
        background = pygame.image.load(self.constant['background_picture']).convert()
        window.blit(background, (0, 0))
        self.level.generate()
        self.level.display(window)
        hero = Character(
            pygame.transform.scale(pygame.image.load(self.constant['macgyver_picture']).convert_alpha(), (30, 30)),
            self.level)
        pygame.display.flip()
        while self.progress:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            item_collected = font.render('Items : {}'.format(hero.inventory), False, (255, 255, 255))
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
                    self.progress = False
            elif self.level.structure[hero.sprite_y][hero.sprite_x] == 'a':
                window.fill('white')
                text = font.render('Victory !', False, (50, 205, 50))
                window.blit(text, (170, 190))
                pygame.display.flip()
                time.sleep(3)
                self.progress = False

    def play_console_mode(self):
        """
        Console mode progression function
        """
        level = Level(self.constant['level_txt_console'])
        level.generate()
        hero = 'X'
        x_hero, y_hero = self.console_mode.position(level.structure, hero)
        while self.progress:
            print('Item : {}'.format(self.item_count))
            for elt in level.structure:
                print("".join(elt))
            direction = input('Choose a direction: ')
            if direction == 'd':
                if level.structure[x_hero][y_hero + 1] != 'm':
                    level.structure[x_hero][y_hero] = '0'
                    level.structure[x_hero][y_hero + 1] = hero
                    y_hero += 1
            elif direction == 'q':
                if level.structure[x_hero][y_hero - 1] != 'm':
                    level.structure[x_hero][y_hero] = '0'
                    level.structure[x_hero][y_hero - 1] = hero
                    y_hero -= 1
            elif direction == 's':
                if level.structure[x_hero + 1][y_hero] != 'm':
                    level.structure[x_hero][y_hero] = '0'
                    level.structure[x_hero + 1][y_hero] = hero
                    x_hero += 1
            elif direction == 'z':
                if level.structure[x_hero - 1][y_hero] != 'm':
                    level.structure[x_hero][y_hero] = '0'
                    level.structure[x_hero - 1][y_hero] = hero
                    x_hero -= 1

            if level.structure[x_hero][y_hero + 1] == 'b':
                if self.item_count < 4:
                    self.progress = False
                    print('You\'re dead !!')
                else:
                    self.progress = False
                    print('You win... but what did you expect? you\'re Macgyver !')

            elif level.structure[x_hero][y_hero + 1] in self.item or level.structure[x_hero][y_hero - 1] in self.item or level.structure[x_hero + 1][y_hero] in self.item or level.structure[x_hero - 1][y_hero] in self.item:
                self.item_count += 1

