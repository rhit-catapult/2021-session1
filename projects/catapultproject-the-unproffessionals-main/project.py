import pygame
import sys


class DamageCounter:
    def __init__(self, screen, x, y, font_color, player):
        """Initializes the damage counter and its variables"""
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 100  # this value will be mutated throughout the game as characters take damage
        self.font = pygame.font.SysFont("", 40, False, True)
        self.font_color = font_color  # must enter an RGB value when creating an instance
        self.player = "Player " + str(player) + ": "

    def draw(self):
        """Gives the string value for the text and blits it onto the screen at given (x, y) position"""
        damage_string = self.player + str(self.health) + "%"
        damage_image = self.font.render(damage_string, True, self.font_color)
        self.screen.blit(damage_image, (self.x, self.y))


class Fireball:
    def __init__(self, screen, x, y):
        """Initializes the fireball and its variables"""
        self.screen = screen
        self.x = x
        self.y = y
        self.has_hit = False
        self.image = pygame.image.load("Projectiles/Projectiles0.png")

    @property
    def hitbox(self):
        """Returns the dimensions of the hitbox for the fireball"""
        return pygame.Rect(self.x, self.y, 10, 5)

    def move_left(self):
        """Gives the distance the character should move left when movement is triggered"""
        self.x -= 5

    def move_right(self):
        """Gives the distance the character should move right when movement is triggered"""
        self.x += 5

    def draw_right(self):
        """Blits the right facing fireball onto the screen at given (x, y) position"""
        self.screen.blit(self.image, (self.x, self.y))

    def draw_left(self):
        """Flips the fireball sprite image and blits it onto the screen at given (x, y) position"""
        self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))


class Arrow:
    def __init__(self, screen, x, y):
        """Initializes the arrow and its variables"""
        self.screen = screen
        self.x = x
        self.y = y
        self.has_hit = False
        self.image = pygame.image.load("Projectiles/Projectiles1.png")

    @property
    def hitbox(self):
        """Returns the dimensions of the hitbox for the arrow"""
        return pygame.Rect(self.x, self.y, 10, 5)

    def move_left(self):
        """Gives the distance the character should move left when movement is triggered"""
        self.x -= 5

    def move_right(self):
        """Gives the distance the character should move right when movement is triggered"""
        self.x += 5

    def draw_right(self):
        """Blits the right facing arrow onto the screen at given (x, y) position"""
        self.screen.blit(self.image, (self.x, self.y))

    def draw_left(self):
        """Flips the arrow sprite image and blits it onto the screen at given (x, y) position"""
        self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))


class Player1:  # Wizard character, AWSD controls
    def __init__(self, screen, x, y, speed, jump_speed, clock):
        """Initializes the wizard character and its variables"""
        self.screen = screen
        self.scale = 1.5  # scalar factor for sprite image
        self.x = x
        # this will offset the y so when coordinates are entered, the bottom of the wizard is touching the ground
        self.y = y - 48 * 1.45
        self.y_safe = y  # this was created so the y value would not change for collision detection
        self.speed = speed
        self.jump_speed = jump_speed  # the amount the character moves up for each jump
        self.picture = pygame.image.load("Flame Wizard (1)/sprite_00.png")
        # scales the sprite image
        self.image = pygame.transform.scale(self.picture, (int(self.picture.get_width() * self.scale),
                                                           int(self.picture.get_height() * self.scale)))
        self.image_paths = []

        # loads all the sprite images and loads them into a list
        for i in range(0, 30):
            file_name = "Flame Wizard (1)/sprite_{:02d}.png".format(i)
            self.image_paths.append(file_name)
        # scales all the sprite images in the list according to the scale factor above
        self.frames = [pygame.transform.scale(pygame.image.load(x), (int(self.picture.get_width() * self.scale),
                       int(self.picture.get_height() * self.scale))) for x in self.image_paths]
        self.left_index = 8
        self.right_index = 0
        self.up_left_index = 21
        self.up_right_index = 16
        self.counter = 0  # aids in the animation of the character by keeping track of the number of frames
        self.jump_direction = "right"
        self.hitbox = pygame.Rect(self.x + 19, self.y_safe - (72-5), 10, 5)  # gives the hitbox dimensions
        self.clock = clock

        # the last functions help to limit the number of projectiles a character can throw at once
        self.fireballs_left = []
        self.fireballs_right = []
        self.numBalls = 0

    def draw(self):
        """Blits the wizard image onto the screen at given (x, y) position"""
        self.screen.blit(self.image, (self.x, self.y))

    def remove_exploded_left(self):
        """Removes fireballs that hit something or left the screen from the game"""
        for k in range(len(self.fireballs_left) - 1, -1, -1):
            if self.fireballs_left[k].has_hit or self.fireballs_left[k].x < 0 or self.fireballs_left[k].x > 960:
                del self.fireballs_left[k]
                self.numBalls -= 1

    def remove_exploded_right(self):
        """Removes fireballs that hit something or left the screen from the game"""
        for k in range(len(self.fireballs_right) - 1, -1, -1):
            if self.fireballs_right[k].has_hit or self.fireballs_right[k].x < 0 or self.fireballs_right[k].x > 960:
                del self.fireballs_right[k]
                self.numBalls -= 1

    def fire_left(self):
        """Adds a fireball to the list in the left direction and tells the Fireball class to create a new fireball"""
        if self.numBalls < 3:
            new_fireball = Fireball(self.screen, self.x,
                                    self.y + 30)
            self.fireballs_left.append(new_fireball)
            self.numBalls += 1

    def fire_right(self):
        """Adds a fireball to the list in the right direction and tells the Fireball class to create a new fireball"""
        if self.numBalls < 3:
            new_fireball = Fireball(self.screen, self.x + 35,
                                    self.y + 30)
            self.fireballs_right.append(new_fireball)
            self.numBalls += 1

    def getX(self):
        """A method to return the x coordinate of the character during the game"""
        return self.x

    def getY(self):
        """A method to return the y coordinate of the character during the game"""
        return self.y

    def hit_by(self, hitbox):
        """Creates an invisible hitbox around the wizard and registers if it collides with another hitbox"""
        hitbox_hit = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox_hit.colliderect(hitbox)  # we had to change this from collidepoint()

    def move_left(self):
        """Gives the amount the wizard should walk left and cycles through frames to animate the wizard"""
        self.x -= self.speed
        self.counter += 1
        # will change the sprite image every 5 frames
        if self.counter % 5 == 0:
            self.image = self.frames[self.left_index]
            self.left_index += 1
            if self.left_index > 15:
                self.left_index = 8

    def move_right(self):
        """Gives the amount the wizard should walk right and cycles through frames to animate the wizard"""
        self.x += self.speed
        self.counter += 1
        # will change the sprite image every 5 frames
        if self.counter % 5 == 0:
            self.image = self.frames[self.right_index]
            self.right_index += 1
            if self.right_index > 7:
                self.right_index = 0

    def jump_left(self):
        """Gives the amount the wizard should move up while facing left and jumping
        and cycles through frames to animate the wizard"""
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 21
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 22
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        for j in range(1, 3):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 23
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        for j in range(1, 2):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 24
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        self.up_left_index = 25
        self.image = self.frames[self.up_left_index]
        self.draw()

    def jump_right(self):
        """Gives the amount the wizard should move up while facing right and jumping
        and cycles through frames to animate the wizard"""
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 16
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 17
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        for j in range(1, 3):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 18
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        for j in range(1, 2):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 19
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        self.up_right_index = 20
        self.image = self.frames[self.up_right_index]
        self.draw()

    def gravity(self):
        """Gives a value to how fast the character should fall"""
        self.y += 5

    def anti_gravity(self):
        """A value opposite to gravity that is turned on when the character collides with a platform"""
        self.y -= 5


class Player2:  # Knight character, arrow controls
    def __init__(self, screen, x, y, speed, jump_speed):
        """Initializes the knight character and its variables"""
        self.screen = screen
        self.scale = 1.5  # scalar factor for sprite image
        self.x = x
        # this will offset the y so when coordinates are entered, the bottom of the knight is touching the ground
        self.y = y - 48 * 1.45
        self.y_safe = y  # this was created so the y value would not change for collision detection
        self.speed = speed
        self.jump_speed = jump_speed  # the amount the character moves up for each jump
        self.picture = pygame.image.load("Blue-Knight/sprite_07.png")
        # scales the sprite image
        self.image = pygame.transform.scale(self.picture, (int(self.picture.get_width() * self.scale),
                                                           int(self.picture.get_height() * self.scale)))
        self.image_paths = []

        # loads all the sprite images and loads them into a list
        for i in range(0, 29):
            file_name = "Blue-Knight/sprite_{:02d}.png".format(i)
            self.image_paths.append(file_name)
        # scales all the sprite images in the list according to the scale factor above
        self.frames = [pygame.transform.scale(pygame.image.load(x), (int(self.picture.get_width() * self.scale),
                       int(self.picture.get_height() * self.scale))) for x in self.image_paths]
        self.left_index = 7
        self.right_index = 0
        self.up_left_index = 20
        self.up_right_index = 16
        self.slash_index = 25
        self.counter = 0  # aids in the animation of the character by keeping track of the number of frames
        self.jump_direction = "left"
        self.hitbox = pygame.Rect(self.x + 19, self.y_safe - (72-5), 10, 5)  # gives the hitbox dimensions

        # the last functions help to limit the number of projectiles a character can throw at once
        self.arrows_left = []
        self.arrows_right = []
        self.numBalls = 0

    def draw(self):
        """Blits the knight image onto the screen at given (x, y) position"""
        self.screen.blit(self.image, (self.x, self.y))

    def remove_exploded_left(self):
        """Removes arrows that have hit something or left the screen from the game"""
        for k in range(len(self.arrows_left) - 1, -1, -1):
            if self.arrows_left[k].has_hit or self.arrows_left[k].x < 0 or self.arrows_left[k].x > 960:
                del self.arrows_left[k]
                self.numBalls -= 1

    def remove_exploded_right(self):
        """Removes arrows that have hit something or left the screen from the game"""
        for k in range(len(self.arrows_right) - 1, -1, -1):
            if self.arrows_right[k].has_hit or self.arrows_right[k].x < 0 or self.arrows_right[k].x > 960:
                del self.arrows_right[k]
                self.numBalls -= 1

    def fire_left(self):
        """Adds an arrow to the list in the left direction and tells the Arrow class to create a new arrow"""
        if self.numBalls < 3:
            new_arrow = Arrow(self.screen, self.x,
                              self.y + 30)
            self.numBalls += 1

            self.arrows_left.append(new_arrow)

    def fire_right(self):
        """Adds an arrow to the list in the left direction and tells the Arrow class to create a new arrow"""
        if self.numBalls < 3:
            new_arrow = Arrow(self.screen, self.x + 35,
                              self.y + 30)
            self.numBalls += 1
            self.arrows_right.append(new_arrow)

    def getX(self):
        """A method to return the x coordinate of the character during the game"""
        return self.x

    def getY(self):
        """A method to return the y coordinate of the character during the game"""
        return self.y

    def hit_by(self, hitbox):
        """Creates an invisible hitbox around the knight and registers if it collides with another hitbox"""
        hitbox_hit = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox_hit.colliderect(hitbox)  # we had to change this from collidepoint()

    def move_left(self):
        """Gives the amount the knight should walk left and cycles through frames to animate the knight"""
        self.x -= self.speed
        self.counter += 1
        # will change the sprite image every 5 frames
        if self.counter % 5 == 0:
            self.image = self.frames[self.left_index]
            self.left_index += 1
            if self.left_index > 15:
                self.left_index = 8

    def move_right(self):
        """Gives the amount the knight should walk right and cycles through frames to animate the knight"""
        self.x += self.speed
        self.counter += 1
        # will change the sprite image every 5 frames
        if self.counter % 5 == 0:
            self.image = self.frames[self.right_index]
            self.right_index += 1
            if self.right_index > 6:
                self.right_index = 0

    def jump_left(self):
        """Gives the amount the knight should move up while facing left and jumping
        and cycles through frames to animate the knight"""
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 20
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 21
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        for j in range(1, 3):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 22
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        for j in range(1, 2):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_left_index = 23
                self.image = self.frames[self.up_left_index]
                self.draw()
                i += 1
        self.up_left_index = 24
        self.image = self.frames[self.up_left_index]
        self.draw()

    def jump_right(self):
        """Gives the amount the knight should move up while facing right and jumping
        and cycles through frames to animate the knight"""
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 16
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        for j in range(1, 4):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 17
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        for j in range(1, 3):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 18
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1
        for j in range(1, 2):
            self.y -= self.jump_speed / 9
            i = 1
            while i < 100:
                self.up_right_index = 19
                self.image = self.frames[self.up_right_index]
                self.draw()
                i += 1

    def gravity(self):
        """Gives a value to how fast the character should fall"""
        self.y += 5

    def anti_gravity(self):
        """A value opposite to gravity that is turned on when the character collides with a platform"""
        self.y -= 5


class KnightSlash:
    def __init__(self, screen, x, y):
        """Initializes the knight slash attack and its variables"""
        self.screen = screen
        self.scale = 2  # scalar factor for sprite image
        self.x = x
        self.y = y
        self.picture = pygame.image.load("Blue-Knight/sprite_25.png")
        # scales the sprite image
        self.image = pygame.transform.scale(self.picture, (int(self.picture.get_width() * self.scale),
                                                           int(self.picture.get_height() * self.scale)))
        self.image_paths = []

        # loads all the sprite images and loads them into a list
        for i in range(25, 29):
            file_name = "Blue-Knight/sprite_{:02d}.png".format(i)
            self.image_paths.append(file_name)
        # scales all the sprite images in the list according to the scale factor above
        self.frames = [pygame.transform.scale(pygame.image.load(x), (int(self.picture.get_width() * self.scale),
                       int(self.picture.get_height() * self.scale))) for x in self.image_paths]
        self.index = 0
        self.counter = 0

        # gives the dimensions for the hitboxes that will tell the characters if they are hit or not
        self.hitbox_left = pygame.Rect(self.x - 32, self.y + 10, 25, 20)
        self.hitbox_right = pygame.Rect(self.x + 32, self.y + 10, 25, 20)

    def changeX(self, num):
        """A method to change the x coordinate of the slash attack during the game"""
        self.x = num

    def changeY(self, num):
        """A method to change the y coordinate of the slash attack during the game"""
        self.y = num

    def draw(self):
        """Cycles through frames to animate the slash attack while the character is facing right
        and blits them onto the screen"""
        i = 1
        while i < 25:
            self.index = 0
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 1
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 2
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 3
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1

    def secondDraw(self):
        """Flips the sprite images and cycles through frames to animate the slash attack
        while the character is facing left and blits them onto the screen"""
        i = 1
        while i < 25:
            self.index = 0
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 1
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 2
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 3
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1


class WizardSlash:
    def __init__(self, screen, x, y):
        """Initializes the wizard slash attack and its variables"""
        self.screen = screen
        self.scale = 2  # scalar factor for sprite image
        self.x = x
        self.y = y
        self.picture = pygame.image.load("Flame Wizard (1)/sprite_26.png")
        # scales the sprite image
        self.image = pygame.transform.scale(self.picture, (int(self.picture.get_width() * self.scale),
                                                           int(self.picture.get_height() * self.scale)))
        self.image_paths = []

        # loads all the sprite images and loads them into a list
        for i in range(26, 30):
            file_name = "Flame Wizard (1)/sprite_{:02d}.png".format(i)
            self.image_paths.append(file_name)
        # scales all the sprite images in the list according to the scale factor above
        self.frames = [pygame.transform.scale(pygame.image.load(x), (int(self.picture.get_width() * self.scale),
                       int(self.picture.get_height() * self.scale))) for x in self.image_paths]
        self.index = 0
        self.counter = 0

        # gives the dimensions for the hitboxes that will tell the characters if they are hit or not
        self.hitbox_left = pygame.Rect(self.x - 32, self.y + 10, 25, 20)
        self.hitbox_right = pygame.Rect(self.x + 32, self.y + 10, 25, 20)

    def changeX(self, num):
        """A method to change the x coordinate of the slash attack during the game"""
        self.x = num

    def changeY(self, num):
        """A method to change the y coordinate of the slash attack during the game"""
        self.y = num

    def draw(self):
        """Cycles through frames to animate the slash attack while the character is facing right
                and blits them onto the screen"""
        i = 1
        while i < 25:
            self.index = 0
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 1
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 2
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 3
            self.image = self.frames[self.index]
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            i += 1

    def secondDraw(self):
        """Flips the sprite images and cycles through frames to animate the slash attack
                while the character is facing left and blits them onto the screen"""
        i = 1
        while i < 25:
            self.index = 0
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 1
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 2
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1
        i = 1
        while i < 25:
            self.index = 3
            self.image = self.frames[self.index]
            self.screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            pygame.display.update()
            i += 1


class Hitbox:
    def __init__(self, screen, x, y, width, height):
        """Initializes the platform hitbox class and its variables"""
        self.screen = screen
        self.scale = 6
        self.x = x * 6 - 6
        self.y = y * 6 - 6
        self.width = width * 6 + 6
        self.height = height * 6 + 6

    def draw(self):
        """Creates a solid version of the invisible hitbox for debugging purposes and blits it onto the screen"""
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def hit_by(self, player):
        """Creates an invisible hitbox at the specified coordinates and registers if it collides with another hitbox"""
        hitbox = pygame.Rect(self.x, self.y, self.width, self.height - 6)
        player.hitbox.update(player.x + 16, player.y + 66, 16, 5)  # updates the position of the characters' hitbox
        return hitbox.colliderect(player.hitbox)


def main():
    # turn on pygame
    pygame.init()
    # create a screen
    pygame.display.set_caption("Medieval Bashout")
    # choose a screen size
    screen = pygame.display.set_mode((960, 720))
    # let's set the framerate
    clock = pygame.time.Clock()

    # aides in telling the characters which way to face
    jump_direction = "right"
    jump_state_wizard = 1
    jump_state_knight = 1

    # create all needed instances of classes
    damage_counter1 = DamageCounter(screen, 5, 1, (165, 0, 0), 1)  # Player 1 damage counter in blue
    damage_counter2 = DamageCounter(screen, screen.get_width() - 200, 1, (0, 165, 0), 2)
    player_1 = Player1(screen, 168, 635, 5, 150, clock)
    player_2 = Player2(screen, 755, 635, 5, 150)
    wiz_slash = WizardSlash(screen, player_1.x + 48, player_1.y + 10)
    test_slash = KnightSlash(screen, player_2.x + 48, player_2.y)
    test_slash.changeX(player_2.getX())
    test_slash.changeY(player_2.getY())

    # load sound effects and music for the game
    background_music = pygame.mixer.Sound("Sound Effects + Music/Background Music Final.wav")
    pygame.mixer.Sound.set_volume(background_music, 50.0)
    pygame.mixer.Sound.play(background_music, 2)
    bow_hit = pygame.mixer.Sound("Sound Effects + Music/Bow-Hit.wav")
    bow_shoot = pygame.mixer.Sound("Sound Effects + Music/Bow-Shoot.wav")
    fireball_hit = pygame.mixer.Sound("Sound Effects + Music/Fireball Explosion.wav")
    fireball_shoot = pygame.mixer.Sound("Sound Effects + Music/Fireball Cast.wav")
    flame_slash = pygame.mixer.Sound("Sound Effects + Music/Flame-Slash.wav")
    sword_slash = pygame.mixer.Sound("Sound Effects + Music/Sword_Slash_New.wav")
    wizard_jump = pygame.mixer.Sound("Sound Effects + Music/Wizard_Jump.wav")
    knight_jump = pygame.mixer.Sound("Sound Effects + Music/Knight_Jump_New.wav")

    # horizontal platform hitboxes
    hitbox1 = Hitbox(screen, 29, 112, 106, 1)
    hitbox2 = Hitbox(screen, 64, 70.5, 23, 1)
    hitbox3 = Hitbox(screen, 4, 94.5, 22, 1)
    hitbox4 = Hitbox(screen, 94, 87.5, 23, 1)
    hitbox5 = Hitbox(screen, 1, 53.5, 14, 1)
    hitbox6 = Hitbox(screen, 30, 46.5, 42, 1)
    hitbox7 = Hitbox(screen, 86, 46.5, 37, 1)
    hitbox8 = Hitbox(screen, 23, 14.5, 103, 1)
    hitbox81 = Hitbox(screen, 36, 86.5, 23, 1)
    # vertical wall hitboxes
    hitbox9 = Hitbox(screen, 8, 68.5, 6, 15)
    hitbox10 = Hitbox(screen, 26, 62.5, 4, 16)
    hitbox11 = Hitbox(screen, 6, 14.5, 6, 27)
    hitbox12 = Hitbox(screen, 142, 84.5, 6, 20)
    hitbox13 = Hitbox(screen, 123, 67.5, 6, 23)
    hitbox14 = Hitbox(screen, 142, 53.5, 6, 22)
    hitbox15 = Hitbox(screen, 123, 46.5, 6, 12)
    hitbox16 = Hitbox(screen, 142, 29.5, 6, 15)

    # variables that keep track of whether the game is over and who won it
    game_is_over = False
    game_winner = "none"

    # a list of all hitboxes in the game that is referenced later for collision detection
    hitboxes = [hitbox1, hitbox2, hitbox3, hitbox4, hitbox5, hitbox6, hitbox7, hitbox8, hitbox81, hitbox9, hitbox10,
                hitbox11, hitbox12, hitbox13, hitbox14, hitbox15, hitbox16]

    # variables that aid in the implementation of the starting screen
    start_game = 0
    char_move_allow = 0

    # THE MAIN GAME LOOP
    while True:
        clock.tick(60)
        screen.fill((255, 255, 255))

        # the code for the starting screen
        if start_game == 0:
            background = pygame.image.load("Title Screen.png")
            background_image = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
            screen.blit(background_image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start_game = 1
        if start_game == 1:
            background = pygame.image.load("background_ladder.png")
            background_image = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
            screen.blit(background_image, (0, 0))
            char_move_allow = 1

        # the elements that need to be shown on the screen when the game is over
        damage_counter1.draw()
        damage_counter2.draw()
        player_1.draw()
        player_2.draw()

        # a loop that freezes the screen and shows the appropriate ending screen when a character dies
        if game_is_over:
            if game_winner == "Player 1 Wins":
                pygame.mixer.Sound.stop(background_music)
                damage_counter2.health = 0
                damage_counter2.draw()
                game_over = pygame.image.load("Mage-Win.png")
                game_over_image = pygame.transform.scale(game_over, (screen.get_width(), screen.get_height()))
                screen.blit(game_over_image, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            main()
            if game_winner == "Player 2 Wins":
                pygame.mixer.Sound.stop(background_music)
                damage_counter1.health = 0
                damage_counter1.draw()
                game_over = pygame.image.load("Knight-Win.png")
                game_over_image = pygame.transform.scale(game_over, (screen.get_width(), screen.get_height()))
                screen.blit(game_over_image, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            main()
            continue

        # the EVENT loop where key presses that we don't want to happen continuously are located
        pressed_keys = pygame.key.get_pressed()
        if char_move_allow == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # event loops for jumping
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and jump_state_wizard == 1 and player_1.y > 0:
                        jump_state_wizard = 0
                        if player_1.jump_direction == "right":
                            pygame.mixer.Sound.play(wizard_jump)
                            player_1.jump_right()
                        if player_1.jump_direction == "left":
                            pygame.mixer.Sound.play(wizard_jump)
                            player_1.jump_left()
                    if event.key == pygame.K_UP and jump_state_knight == 1 and player_2.y > 0:
                        jump_state_knight = 0
                        if player_2.jump_direction == "right":
                            pygame.mixer.Sound.play(knight_jump)
                            player_2.jump_right()
                        if player_2.jump_direction == "left":
                            pygame.mixer.Sound.play(knight_jump)
                            player_2.jump_left()

                    # event loops for slash attacking
                    if event.key == pygame.K_s:
                        if player_1.jump_direction == "right":
                            wiz_slash.changeX(player_1.getX() + 25)
                            wiz_slash.changeY(player_1.getY() + 10)
                            pygame.mixer.Sound.play(flame_slash)
                            wiz_slash.draw()
                            wiz_slash.hitbox_right.update(player_1.x + 45, player_1.y + 10, 25, 20)
                            if player_2.hit_by(wiz_slash.hitbox_right):
                                damage_counter2.health -= 4
                                player_2.x += 50
                                player_2.y -= 20
                                if damage_counter2.health <= 0:
                                    damage_counter2.health = 0
                        if player_1.jump_direction == "left":
                            wiz_slash.changeX(player_1.getX() - 25)
                            wiz_slash.changeY(player_1.getY() + 10)
                            pygame.mixer.Sound.play(flame_slash)
                            wiz_slash.secondDraw()
                            wiz_slash.hitbox_left.update(player_1.x - 15, player_1.y + 10, 25, 20)
                            if player_2.hit_by(wiz_slash.hitbox_left):
                                damage_counter2.health -= 4
                                player_2.x -= 50
                                player_2.y -= 20
                                if damage_counter2.health <= 0:
                                    damage_counter2.health = 0
                    if event.key == pygame.K_DOWN:
                        if player_2.jump_direction == "right":
                            test_slash.changeX(player_2.getX() + 25)
                            test_slash.changeY(player_2.getY())
                            pygame.mixer.Sound.play(sword_slash)
                            test_slash.draw()
                            test_slash.hitbox_right.update(player_2.x + 45, player_2.y + 10, 25, 20)
                            if player_1.hit_by(test_slash.hitbox_right):
                                damage_counter1.health -= 4
                                player_1.x += 50
                                player_1.y -= 20
                                if damage_counter1.health <= 0:
                                    damage_counter1.health = 0
                        if player_2.jump_direction == "left":
                            test_slash.changeX(player_2.getX() - 25)
                            test_slash.changeY(player_2.getY())
                            pygame.mixer.Sound.play(sword_slash)
                            test_slash.secondDraw()
                            test_slash.hitbox_left.update(player_2.x - 15, player_2.y + 10, 25, 20)
                            if player_1.hit_by(test_slash.hitbox_left):
                                damage_counter1.health -= 4
                                player_1.x -= 50
                                player_1.y -= 20
                                if damage_counter1.health <= 0:
                                    damage_counter1.health = 0

                    # event loops for firing projectiles
                    if event.key == pygame.K_q:
                        if player_1.jump_direction == "left":
                            pygame.mixer.Sound.play(fireball_shoot)
                            player_1.fire_left()
                        if player_1.jump_direction == "right":
                            pygame.mixer.Sound.play(fireball_shoot)
                            player_1.fire_right()
                    if event.key == pygame.K_KP0:
                        if player_2.jump_direction == "left":
                            pygame.mixer.Sound.play(bow_shoot)
                            player_2.fire_left()
                        if player_2.jump_direction == "right":
                            pygame.mixer.Sound.play(bow_shoot)
                            player_2.fire_right()

            # left and right movement syntax for the wizard and knight
            if pressed_keys[pygame.K_a] and player_1.x > 0:
                player_1.move_left()
                player_1.jump_direction = "left"
            if pressed_keys[pygame.K_d] and player_1.x < screen.get_width() - player_1.image.get_width():
                player_1.move_right()
                player_1.jump_direction = "right"
            if pressed_keys[pygame.K_LEFT] and player_2.x > 0:
                player_2.move_left()
                player_2.jump_direction = "left"
            if pressed_keys[pygame.K_RIGHT] and player_2.x < screen.get_width() - player_2.image.get_width():
                player_2.move_right()
                player_2.jump_direction = "right"

            # here is where the gravity function in the PLayer1 & Player2 classes is called
            player_1.gravity()
            player_2.gravity()

            # collision detection: if a player hits one of the platform hitboxes, they stop falling
            for hitbox in hitboxes:
                if hitbox.hit_by(player_1):
                    player_1.anti_gravity()
                    jump_state_wizard = 1
                if hitbox.hit_by(player_2):
                    player_2.anti_gravity()
                    jump_state_knight = 1

            # syntax for the movement and damage of a fireball
            for fireball in player_1.fireballs_left:
                fireball.move_left()
                fireball.draw_left()
                if player_2.hit_by(fireball.hitbox):
                    damage_counter2.health -= 10
                    fireball_hit.play()
                    fireball.has_hit = True
            for fireball in player_1.fireballs_right:
                fireball.move_right()
                fireball.draw_right()
                if player_2.hit_by(fireball.hitbox):
                    damage_counter2.health -= 10
                    fireball_hit.play()
                    fireball.has_hit = True

            # syntax for the movement and damage of an arrow
            for arrow in player_2.arrows_left:
                arrow.move_left()
                arrow.draw_left()
                if player_1.hit_by(arrow.hitbox):
                    damage_counter1.health -= 10
                    bow_hit.play()
                    arrow.has_hit = True
            for arrow in player_2.arrows_right:
                arrow.move_right()
                arrow.draw_right()
                if player_1.hit_by(arrow.hitbox):
                    damage_counter1.health -= 10
                    bow_hit.play()
                    arrow.has_hit = True

            # tells the game that if a player falls off the bottom of the screen, they die
            if player_1.y > 720:
                damage_counter1.health = 0
            if player_2.y > 720:
                damage_counter2.health = 0

            # tells the game if a player has 0 health remaining, the game is over and the other player wins
            if damage_counter1.health <= 0:
                game_is_over = True
                game_winner = "Player 2 Wins"
            if damage_counter2.health <= 0:
                game_is_over = True
                game_winner = "Player 1 Wins"

            # don't forget the update, otherwise nothing will show up!
            player_1.remove_exploded_left()
            player_1.remove_exploded_right()
            player_2.remove_exploded_left()
            player_2.remove_exploded_right()
            pygame.display.update()
        pygame.display.update()


# THE MAIN FUNCTION IS CALLED!!
main()
