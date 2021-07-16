import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# Done: Create a Ball class.
# Done: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = random.randint(0, 50)
        self.speedy = random.randint(0, 50)
    def move(self):
        self.y = self.y + self.speedy
        self.x = self.x + self.speedx
        if self.x < 0 or self.x > 300:
            self.speedx = -self.speedx
        if self.y < 0 or self.y > 300:
            self.speedy = -self.speedy
    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 0), (self.x, self.y), 15)

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball = Ball(screen, 150, 150)

    # TODO: Create an instance of the Ball class called ball1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        ball.move()
        ball.draw()
        # Done: Draw the ball


        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
