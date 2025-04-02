import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0,1).rotate(rotation) * PLAYER_SHOT_SPEED
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 1)
        
    def update(self, dt):
        self.position += self.velocity * dt
