from level import Level
import pygame


class GraphicLevel(Level):
    def __init__(self, file):
        Level.__init__(self, file)
        self.file = file

    @staticmethod
    def resize_set(pic):
        """
        resizing sets pictures
        """
        return pygame.transform.scale(
            pygame.image.load(pic).convert_alpha(), (30, 30))

    def display(self, window):
        """
        maze displaying items and bad guy
        """
        macgyver = self.resize_set(self.constant['macgyver'])
        wall = self.resize_set(self.constant['wall_picture'])
        floor = self.resize_set(self.constant['floor_picture'])
        flag = self.resize_set(self.constant['flag_picture'])
        bad_guy = self.resize_set(self.constant['bad_guy_picture'])
        needle = self.resize_set(self.constant['needle_picture'])
        ether = self.resize_set(self.constant['ether_picture'])
        syringe = self.resize_set(self.constant['syringe_picture'])
        tube = self.resize_set(self.constant['tube_picture'])
        line_number = 0
        for line in self.structure:
            sprite_number = 0
            for sprite in line:
                x = sprite_number * self.constant['sprite_size']
                y = line_number * self.constant['sprite_size']
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'X':
                    window.blit(floor, (x, y))
                    window.blit(macgyver, (x, y))
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
