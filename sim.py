import pygame
from circle import Ball
from vector2 import Vector2
import debug

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

    # Debug info
    debug_info = debug.DebugInfo(window, clock)
    debug_info.add_info("FPS", 0)
    debug_info.add_info("Ball Position", ball.pos)
    debug_info.add_info("Ball Velocity", ball.velocity)

    is_running = True
    dt = 0
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window.fill(BACKGROUND_COLOR)

        debug_info.delay_timer += dt
        if debug_info.delay_timer >= debug_info.delay:
            debug_info.delay_timer = 0
            debug_info.set_info_value("FPS", f"{clock.get_fps():.2f}")
            debug_info.set_info_value("Ball Position", ball.pos)
            debug_info.set_info_value("Ball Velocity", ball.velocity)
        debug_info.debug_render("white")
        
        ball.update(dt)
        ball.render(window, "red", width=1)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000
    pygame.quit()
