import pygame
import sys
import random


class Ball:
    def __init__(self, screen, color, x, y, radius):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x

    def draw(self):
        pygame.draw.circle(self.screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           (self.x, self.y), self.radius)

    def border(self):
        if self.x > self.screen.get_width() - self.radius:
            self.speed_x = -self.speed_x

        if self.y > self.screen.get_height() - self.radius:
            self.speed_y = -self.speed_y

        if self.x < 0 + self.radius:
            self.speed_x = -self.speed_x

        if self.y < 0 + self.radius:
            self.speed_y = -self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    balls = Ball(screen, (0, 0, 0),
                 random.randint(50, 250), random.randint(50, 250), random.randint(5, 20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        balls.draw()
        balls.move()
        balls.border()

        pygame.display.update()


main()


#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
