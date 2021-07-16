import pygame, sys


class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   has_exploded to False.
        self.screen = screen
        self.x = x
        self.y = 591
        self.has_exploded = False

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        self.y -= 5

    def draw(self):
        # Draw a vertical, 4 pixels thick, 8 pixels long, red (or green) line on the screen,
        # where the line starts at the current position of this Missile.
        pygame.draw.line(self.screen, (0, 255, 0), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey((255, 255, 255))
        self.missiles = []
        self.pew = pygame.mixer.Sound("pew.wav")

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        new_missile = Missile(self.screen, self.x + self.image.get_width() // 2)
        self.missiles.append(new_missile)
        self.pew.play()

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same name.
        # Set   is_dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.original_x = x
        self.y = y
        self.speed = speed
        self.is_dead = False
        self.image = pygame.image.load("badguy.png")

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        self.x += self.speed
        if abs(self.x - self.original_x) > 100:
            self.speed = -self.speed
            self.y += abs(self.speed)

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        self.death = pygame.mixer.Sound("explosion.wav")
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        return len(self.badguys) == 0

    def move(self):
        # Make each badguy in this EnemyFleet move.
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]
                self.death.play()


class Scoreboard:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        score_string = "Score: " + str(self.score)
        score_image = self.font.render(score_string, True, (255, 255, 255))
        self.screen.blit(score_image, (5, 5))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # TODOne 9: Set    enemy_rows    to an initial value of 3.
    # TODOne 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    is_game_over = False
    enemy_rows = 3
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    # TODOne 1: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)
    game_over_image = pygame.image.load("gameover.png")
    scoreboard = Scoreboard(screen)
    win_sound = pygame.mixer.Sound("win.wav")
    lose_sound = pygame.mixer.Sound("lose.wav")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # TODOne 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        enemy_fleet.draw()
        fighter.draw()
        scoreboard.draw()
        if is_game_over:
            screen.blit(game_over_image, (170, 200))
            pygame.display.update()
            continue
        pressed_keys = pygame.key.get_pressed()
        # TODOne 3: If pygame.K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5
        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x -= 5
        # TODOne 4: If pygame.K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < 590:
            fighter.x += 5
        # TODOne 2: Draw the fighter
        # TODOne 11: Move the enemy_fleet
        # TODOne 12: Draw the enemy_fleet
        enemy_fleet.move()

        # TODOne 6: For each missile in the fighter missiles
        #   TODOne 7: Move the missile
        #   TODOne 8: Draw the missile
        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        # TODOne 12: For each badguy in the enemy_fleet.badguys list
        for badguy in enemy_fleet.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    scoreboard.score += 100
                    badguy.is_dead = True
                    missile.has_exploded = True
        #     TODOne 13: For each missile in the fighter missiles
        #         TODOne 14: If the badguy is hit by the missile
        #             TODOne 15: Mark the badguy is_dead = True
        #             TODOne 16: Mark the missile has_exploded = True

        # TODOne 17: Use the fighter to remove exploded missiles
        # TODOne 18: Use the enemy_fleet to remove dead badguys
        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()

        # TODOne 19: If the enemy is_defeated
        #     TODOne 20: Increment the enemy_rows
        #     TODOne 21: Create a new enemy_fleet with the screen and enemy_rows
        if enemy_fleet.is_defeated:
            win_sound.play()
            enemy_rows += 1
            enemy_fleet = EnemyFleet(screen, enemy_rows)

        # TODOne 22: Check for your death.  Figure out what needs to happen.
        for badguy in enemy_fleet.badguys:
            if badguy.y > 545:
                is_game_over = True
                lose_sound.play()
        # Hints: Check if a Badguy gets a y value greater than 545
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)

        # TODOne 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score
        # TODOne 24: Optional extra - Add sound effects!
        pygame.display.update()


main()