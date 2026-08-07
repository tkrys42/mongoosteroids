import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.wrap_around()

    def split(self):
        self.kill()
        # if asteroid is smallest size already, it's just destroyed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # otherwise destroy it but also create two smaller ones
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            direction_a = self.velocity.rotate(random_angle)
            direction_b = self.velocity.rotate(-random_angle)
            # the two new asteroids are one size smaller
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # spawn two new asteroids at the position of the old one with the new radius
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            # send the two new asteroids flying in the random directions established before
            asteroid_a.velocity = direction_a * 1.2
            asteroid_b.velocity = direction_b * 1.2





