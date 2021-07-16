import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class BouncyBall:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-10, 10)

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), 20)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.x > 980:
            self.speed_x = -self.speed_x
        if self.x < 20:
            self.speed_x = -self.speed_x
        if self.y < 20:
            self.speed_y = -self.speed_y
        if self.y > 980:
            self.speed_y = -self.speed_y
def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    more_balls = []
    i = 0
    while i < 4500:
        i += 1
        ball = BouncyBall(screen, (0, 0, 255), 500, 500, 20, 0, 0)
        more_balls.append(ball)

    # TODO: Create an instance of the Ball class called ball1
    ball = BouncyBall(screen, (0, 0, 255), 500, 500, 20, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pygame.Color('gray'))
        clock.tick(60)
    # DONE: Move the ball
        ball.move()
        for b in more_balls:
            b.move()
            b.draw()
    # DONE: Draw the ball
        ball.draw()
        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
