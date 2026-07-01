import pygame
from circle import Ball
from vector2 import Vector2

WIN_SIZE = (600, 400)
WIN_TITLE = "Physics Sim"
BACKGROUND_COLOR = "black"
FPS = 60

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(WIN_TITLE)
    window = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.Clock()

    ball = Ball(window, Vector2(300, 200), 10)

    is_running = True
    dt = 0
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window.fill(BACKGROUND_COLOR)
        
        ball.update(dt)
        ball.render(window, "red", width=1)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000
    pygame.quit()
