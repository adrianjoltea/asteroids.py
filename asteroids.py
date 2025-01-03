import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

        
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        r_angle = random.uniform(20,50)
        a1_vel = self.velocity.rotate(r_angle)
        a2_vel = self.velocity.rotate(-r_angle)
        small_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, small_radius) 
        a2 = Asteroid(self.position.x, self.position.y, small_radius) 
        
        a1.velocity = a1_vel * 1.2
        a2.velocity = a2_vel * 1.2
        
        
        
    