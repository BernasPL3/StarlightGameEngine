import pygame
from engine.renderer import Renderer
from engine.scene import Scene
from engine.sprite import Sprite

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Statlight Game Engine"

def main():
    pygame.init()

    renderer = Renderer(WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_caption(WINDOW_TITLE)

    scene = Scene()

    try:
        player = Sprite("assets/icon.png", 100, 100)
        scene.add(player)
    except Exception as e:
        print(f"Erro ao carregar sprite: {e}")

    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scene.update()

        renderer.clear()
        scene.draw(renderer.screen)

        fps = int(clock.get_fps())
        pygame.display.set_caption(
            f"{WINDOW_TITLE} | FPS: {fps}"
        )

        renderer.update()

    pygame.quit()

if __name__ == "__main__":
    main()
