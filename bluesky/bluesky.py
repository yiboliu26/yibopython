import sys, pygame
from penguin import Penguin

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1440, 960))
    pygame.display.set_caption("Blue Sky")
    penguin = Penguin(screen)

    bg_color = (230, 230, 230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        penguin.blitme()
        pygame.display.flip()
run_game()