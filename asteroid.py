import random

import pygame
from pygame.surface import Surface

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r_angle = random.uniform(20, 50)
            angle_1 = self.velocity.rotate(r_angle)
            angle_2 = self.velocity.rotate(-r_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_a.velocity = angle_1 * 1.2
            child_asteroid_b.velocity = angle_2 * 1.2
