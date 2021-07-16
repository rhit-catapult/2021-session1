import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(-5, 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    circle_center_x = random.randint(0, 300)
    circle_center_y = random.randint(0, 300)
    # TODO: Create an instance of the Ball class called ball1
    speed_x = random.randint(5, 20)
    speed_y = random.randint(5, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball
        circle_color = (100, 20, 210)
        circle_center = (circle_center_x , circle_center_y)
        circle_radius = 10
        circle_border_width = 10
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)
        circle_center_x = circle_center_x + speed_x
        circle_center_y = circle_center_y + speed_y
        if circle_center_x >= screen.get_width():
            speed_x = -speed_x
        if circle_center_x <= circle_radius:
            speed_x = -speed_x
        if circle_center_y <= circle_radius:
            speed_y = -speed_y
        if circle_center_y >= screen.get_height():
            speed_y = -speed_y

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
