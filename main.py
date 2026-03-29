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
    pygame.font.init()
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

    score = 0
    font = pygame.font.Font(None, 36)

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
                print(f"Final Score: {score}!")
                sys.exit()
        # when shot, the shot is destroyed and the asteroid splits or is destroyed if small enough
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    if asteroid.radius < 30:
                        score += 250
                    elif asteroid.radius < 50:
                        score += 150
                    else:
                        score += 100

        for obj in drawable:
            obj.draw(screen)
        # Render the score on the screen
        score_surface = font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (10, 10))
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
