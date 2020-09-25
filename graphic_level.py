from level import *


class GraphicLevel(Level):
    def __init__(self, file):
        Level.__init__(self, file)
        self.file = file

    def display(self, window):
        """
        maze displaying items and bad guy
        """
        wall = pygame.transform.scale(pygame.image.load(self.constant['wall_picture']).convert_alpha(), (30, 30))
        floor = pygame.transform.scale(pygame.image.load(self.constant['floor_picture']).convert_alpha(), (30, 30))
        flag = pygame.transform.scale(pygame.image.load(self.constant['flag_picture']).convert_alpha(), (30, 30))
        bad_guy = pygame.transform.scale(pygame.image.load(self.constant['bad_guy_picture']).convert_alpha(), (30, 30))
        needle = pygame.transform.scale(pygame.image.load(self.constant['needle_picture']).convert(), (30, 30))
        ether = pygame.transform.scale(pygame.image.load(self.constant['ether_picture']).convert(), (30, 30))
        syringe = pygame.transform.scale(pygame.image.load(self.constant['syringe_picture']).convert(), (30, 30))
        tube = pygame.transform.scale(pygame.image.load(self.constant['tube_picture']).convert(), (30, 30))
        line_number = 0
        for line in self.structure:
            sprite_number = 0
            for sprite in line:
                x = sprite_number * self.constant['sprite_size']
                y = line_number * self.constant['sprite_size']
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == '0':
                    window.blit(floor, (x, y))
                elif sprite == 'd' or sprite == 'a':
                    window.blit(flag, (x, y))
                elif sprite == 'b':
                    window.blit(floor, (x, y))
                    window.blit(bad_guy, (x, y))
                elif sprite == 'N':
                    window.blit(floor, (x, y))
                    window.blit(needle, (x, y))
                elif sprite == 'E':
                    window.blit(floor, (x, y))
                    window.blit(ether, (x, y))
                elif sprite == 'S':
                    window.blit(floor, (x, y))
                    window.blit(syringe, (x, y))
                elif sprite == 'T':
                    window.blit(floor, (x, y))
                    window.blit(tube, (x, y))
                sprite_number += 1
            line_number += 1
