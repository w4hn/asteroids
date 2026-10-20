import pygame
from constants import *
from logger import log_state
from player import Player

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    dt = 0.0
    player_x: float = SCREEN_WIDTH / 2
    player_y: float = SCREEN_HEIGHT / 2

    player = Player(player_x, player_y)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
