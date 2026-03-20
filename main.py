import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

# game loop
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(dt)
        # asteroids kill player when one hits it
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        # when shot, the shot is destroyed and the asteroid splits or is destroyed if small enough
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.split()
        for obj in drawable:
            obj.draw(screen)
        # refresh the screen, called last
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000


        # if you click the x on the window, it closes the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    
if __name__ == "__main__":
    main()
