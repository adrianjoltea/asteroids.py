import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers=(updatable,drawable, shots)
    Player.containers = (updatable, drawable)
    player = Player(x,y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updates in updatable:
            updates.update(dt)
            
        screen.fill("black")
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot): 
                    shot.kill()
                    asteroid.kill()
            
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
                    
                    
        
        for draws in drawable:
            draws.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()