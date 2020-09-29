from level_ui import GraphicLevel
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


class GraphicMode(Constant):
    """
    Main class for graphical mode game
    """

    def __init__(self):
        Constant.__init__(self)
        self.level = GraphicLevel(self.constant['level'])
        self.window_side = \
            self.constant['sprite_number'] * self.constant['sprite_size']
        self.player = Character(self.constant['player'], self.level)

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
                        if self.player.move(
                                x_hero, y_hero, x_hero, y_hero + 1,
                                self.level, self.constant['player']):
                            y_hero += 1
                    elif event.key == K_LEFT:
                        if self.player.move(
                                x_hero, y_hero, x_hero, y_hero - 1,
                                self.level, self.constant['player']):
                            y_hero -= 1
                    elif event.key == K_UP:
                        if self.player.move(
                                x_hero, y_hero, x_hero - 1, y_hero,
                                self.level, self.constant['player']):
                            x_hero -= 1
                    elif event.key == K_DOWN:
                        if self.player.move(
                                x_hero, y_hero, x_hero + 1, y_hero,
                                self.level, self.constant['player']):
                            x_hero += 1

            window.blit(background, (0, 0))
            self.level.display(window)
            window.blit(item_collected, (300, 0))
            pygame.display.flip()

            if self.level.structure[x_hero][y_hero + 1] == 'b':
                if self.player.item_count < 4:
                    self.player.has_lose('ui', window)
                    progress = False
                else:
                    self.player.has_win('ui', window)
                    progress = False
