import pygame
from engine.renderer import Renderer
from engine.scene import Scene

class Game:
    def __init__(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.scene.update()

            self.renderer.clear()
            self.scene.draw(self.renderer.screen)
            self.renderer.update()

        pygame.quit()
