import pygame
import math

# initialize pygame
pygame.init()

# Size of the Window
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Name of the window
pygame.display.set_caption("Solar System Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 76, 5)
GREY = (80, 71, 81)
VENUS = (255, 122, 69)


class Planet:

    AU = 14959787070000000000
    G = 6.67430e-11
    SCALE = 250 / AU # 1AU = 100 pixels 
    TIMESTEP = 3600 * 24 # One day 


    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []

        self.x_velocity = 0
        self.y_velocity = 0

        self.sun = False
        self.distance_to_sun = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y

        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance
        
        theta = math.atan2(distance_y, distance_x)
        force = self.G * self.mass * other.mass / (distance ** 2)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)
        return force_x, force_y


def main():
    run = True;
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9722 * 10**24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, ORANGE, 6.39 * 10**23)
    mercury = Planet(-.387 * Planet.AU, 0, 8, GREY, 3.30 * 10**23)
    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WINDOW)

        pygame.display.update()


    pygame.quit()

main()