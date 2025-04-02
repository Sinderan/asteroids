import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        new_asteroids = []
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return new_asteroids
        else:
            random_angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(random_angle) 
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            new_asteroids.append(asteroid1)
            
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2
            new_asteroids.append(asteroid2)

            return new_asteroids
