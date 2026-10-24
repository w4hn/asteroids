import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_asteroid_movement = self.velocity.rotate(angle)
        second_asteroid_movement = self.velocity.rotate(-angle)
        asteroid_new_raidus = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, asteroid_new_raidus)
        second_asteroid = Asteroid(self.position.x, self.position.y, asteroid_new_raidus)
        first_asteroid.velocity = first_asteroid_movement * 1.2
        second_asteroid.velocity = second_asteroid_movement * 1.2


    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
