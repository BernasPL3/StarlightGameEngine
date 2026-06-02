import pygame

class Input:
    @staticmethod
    def key_pressed(key):
        keys = pygame.key.get_pressed()
        return keys[key]
