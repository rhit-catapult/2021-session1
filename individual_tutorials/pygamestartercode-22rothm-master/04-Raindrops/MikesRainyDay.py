import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # Done 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randrange[5, 16]

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # TODO 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # TODO 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # TODO     from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (0, 0, 127), (self.x, self.y), (self.x, self.y + 5))


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # TODO 16: Initialize this Hero, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Hero to x and y.
        # TODO    - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        # TODO    - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        # TODO    - Set the "last hit time" to 0.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella)
        self.image_without_umbrella = pygame.image.load(without_umbrella)
        self.last_hit_time = 0


    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        current_image = self.image_without_umbrella
        if time.time() - self.last_hit_time < 1.0:
            current_image = self.image_with_umbrella
        self.screen.blit(current_image, (self.x, self.y))

        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.


    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # Done 19: Return True if this Hero is currently colliding with the given Raindrop.
        hero_hit_box = pygame.Rect(self.x, self.y, 170, 192)
        return hero_hit_box.collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # Done 24: Initialize this Cloud, as follows:
        # Done    - Store the screen.
        # Done    - Set the initial position of this Cloud to x and y.
        # Done    - Set the image of this Cloud to the given image filename.
        # Done    - Create a list for Raindrop objects as an empty list called raindrops.
        # Done  Use instance variables:
        # Done     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image.load(image_filename)
        self.raindrop = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # Done 28: Append a new Raindrop to this Cloud's list of raindrops,
        # Done    where the new Raindrop starts at:
        # Done      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # Done      - y is this Cloud's y + 100.
        new_raindrop = Raindrop(self.screen, self.x + random. randint(0, 300))
        self.raindrops.append(new_raindrop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # Done 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("Mike's riany day")
    pygame.display.set_mode((1000, 600))
    screen = pygame.display.set_mode((1000, 600))

    # Done 2: Make a Clock
    clock = pygame.time.Clock()
    # Done 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    test_drop = Raindrop(screen, 320,10)
    # Done 15: Make a Hero, named mike, with appropriate images, starting at position x=300 y=400.
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")
    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "cloud.png")
    # Done 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.

        # Done 4:   Make the pygame.QUIT event stop the game.
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Done 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        # Dlone    Arrange so that the Cloud moves:
        # Done      5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # Done      5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        # Done      5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        # Done      5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 5
        if pressed_keys[pygame.LEFT]:
            cloud.x = cloud.x - 5
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 5
        # Done 5: Inside the game loop, draw the screen (fill with white)
        screen.fill((255, 255, 255))

        # TODO 12: As a temporary test, move test_drop
        test_drop.move()
        cloud.draw()

        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        pygame.display.update()

main()
