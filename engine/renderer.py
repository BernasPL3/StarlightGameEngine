import pygame

class Renderer:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

    def clear(self):
        self.screen.fill((20, 20, 30))

    def update(self):
        pygame.display.flip()
