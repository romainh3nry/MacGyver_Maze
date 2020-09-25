import pygame
from level import Level


class GraphicLevel(Level):
    def __init__(self, file):
        Level.__init__(self, file)
        self.file = file

    @staticmethod
    def resize_set(pic):
        return pygame.transform.scale(
            pygame.image.load(pic).convert_alpha(), (31, 31))

    @staticmethod
    def resize_item(item):
        return pygame.transform.scale(
            pygame.image.load(item).convert(), (31, 31))

    def display(self, window):
        """
        maze displaying items and bad guy
        """
        wall = self.resize_set(self.constant['wall_picture'])
        floor = self.resize_set(self.constant['floor_picture'])
        flag = self.resize_set(self.constant['flag_picture'])
        bad_guy = self.resize_set(self.constant['bad_guy_picture'])
        needle = self.resize_item(self.constant['needle_picture'])
        ether = self.resize_item(self.constant['ether_picture'])
        syringe = self.resize_item(self.constant['syringe_picture'])
        tube = self.resize_item(self.constant['tube_picture'])
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
