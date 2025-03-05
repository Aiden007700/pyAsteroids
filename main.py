import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import  SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)


    asteroidField = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)  / 1000
        screen.fill("black", rect=None, special_flags=0)

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        print(dt)


if __name__ == "__main__":
    main()