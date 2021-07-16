import pygame
import sys


class Spaceship:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('hero.png')
        self.lifelost = False
        self.has_died = False
        self.scaled_image = pygame.transform.scale(self.image, (100, 100))
        self.scaled_image.set_colorkey((255, 255, 255))
        self.bullets = []
        self.shot = pygame.mixer.Sound("shot.mp3")

    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    def shoot(self):
        new_bullet = Bullet(self.screen, self.x + self.scaled_image.get_width() // 2 - 25,
                            self.y + self.scaled_image.get_height() - 100)
        self.bullets.append(new_bullet)
        self.shot.play(maxtime=400)

    def remove_hit_bullets(self):
        for k in range(len(self.bullets) - 1, -1, -1):
            if self.bullets[k].has_hit or self.bullets[k].y < 0:
                del self.bullets[k]

    def remove_reverse_bullets(self, reverse_bullets):
        for k in range(len(reverse_bullets) - 1, -1, -1):
            if reverse_bullets[k].has_hit or reverse_bullets[k].y > 700:
                del reverse_bullets[k]

    def hit_by(self, reverse_bullet):
        hitbox = pygame.Rect(self.x, self.y, self.scaled_image.get_width(), self.scaled_image.get_height())
        return hitbox.collidepoint(reverse_bullet.x, reverse_bullet.y)


class Bullet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('bullet.png')
        self.has_hit = False
        self.scaled_image = pygame.transform.scale(self.image, (50, 10))
        self.speed = -10

    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    def move(self):
        self.y += self.speed


class ReverseBullet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('bullet.png')
        self.has_hit = False
        self.scaled_image = pygame.transform.scale(self.image, (50, 10))
        self.speed = +10

    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    def move(self):
        self.y += self.speed


class EnemySpaceship:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.original_x = x
        self.y = y
        self.c = 0
        self.speed_x = 4
        self.is_dead = False
        self.image = pygame.image.load('enemy2.png')
        self.scaled_image = pygame.transform.scale(self.image, (50, 50))
        self.explosion_image = pygame.image.load("explosion.png")
        self.scaled_explosion_image = pygame.transform.scale(self.explosion_image, (50, 50))
        self.pictures = [self.scaled_image, self.scaled_explosion_image]

    def onSpace(self):
        self.c = (self.c + 1) % len(self.pictures)

    def get_image(self):
        return self.pictures[self.c]

    def draw(self):
        self.screen.blit(self.pictures.__getitem__(self.c), (self.x, self.y))

    def move(self):
        self.x += self.speed_x
        if self.x > 900:
            self.speed_x = -self.speed_x
        if self.x < 0:
            self.speed_x = -self.speed_x

    def hit_by(self, bullet):
        hitbox = pygame.Rect(self.x, self.y, self.scaled_image.get_width(), self.scaled_image.get_height())
        return hitbox.collidepoint(bullet.x, bullet.y)


class GalagaArmy:
    def __init__(self, screen, army_lines):
        self.enemyspaceships = []
        self.explosion = pygame.mixer.Sound("explosion.wav")
        for j in range(army_lines):
            for k in range(16):
                self.enemyspaceships.append(EnemySpaceship(screen, 55 * k, 55 * j + 20))

    @property
    def is_destroyed(self):
        return len(self.enemyspaceships) == 0

    def move(self):
        for enemyspaceship in self.enemyspaceships:
            enemyspaceship.move()

    def draw(self):
        for enemyspaceship in self.enemyspaceships:
            enemyspaceship.draw()

    def remove_dead(self):
        for k in range(len(self.enemyspaceships) - 1, -1, -1):
            if self.enemyspaceships[k].is_dead:
                del self.enemyspaceships[k]
                self.explosion.play(maxtime=399)


class Scoreboard(object):

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        score_string = "Score:" + str(self.score)
        score_image = self.font.render(score_string, True, (255, 255, 255))
        self.screen.blit(score_image, (5, 5))


class LostHeart(object):

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.image = pygame.image.load('lostheart.png')
        self.scaled_image = pygame.transform.scale(self.image, (25, 25))
        self.lives = self.scaled_image
        self.number_of_lives = 3
        self.lostheart_image = pygame.image.load('lostheart.png')
        self.lostheart_scaled_image = pygame.transform.scale(self.lostheart_image, (25, 25))

    def draw(self):
        self.scaled_image.blit(self.scaled_image, (500, 5))


class LivesCounter(object):

    def __init__(self, screen):
        self.Lives = []
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.image = pygame.image.load('heart.png')
        self.scaled_image = pygame.transform.scale(self.image, (25, 25))
        self.lives = self.scaled_image
        self.number_of_lives = 3

    def draw(self):
        lives_string = "Lives:"
        lives_image = self.font.render(lives_string, True, (255, 255, 255))
        self.screen.blit(lives_image, (800, 0))
        for i in range(0, self.number_of_lives):
            x_coordinate = 805 + lives_image.get_width() + i * self.lives.get_width()
            self.screen.blit(self.lives, (x_coordinate, 0))


def main():
    # turn on pygame
    pygame.init()
    background_sound = pygame.mixer.Sound("needforspeed.mp3")
    background_sound.play(loops=-1)
    # create a screen
    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((1000, 700))
    spaceship1 = Spaceship(screen, screen.get_width() // 2 - 50, screen.get_height() - 100)
    enemyspaceship = EnemySpaceship(screen, 500, 0)
    army_lines = 2
    galaga_army = GalagaArmy(screen, army_lines)
    scoreboard = Scoreboard(screen)
    win_sound = pygame.mixer.Sound("win.wav")
    lose_sound = pygame.mixer.Sound("lose.wav")
    reverse_bullets = []
    livescounter = LivesCounter(screen)
    lostheart = LostHeart(screen)
    game_over_image = pygame.image.load("gameover.png")
    is_game_over = False
    stopped = False
    clock = pygame.time.Clock()
    number_of_frames = 0
    while True:
        clock.tick(60)
        number_of_frames += 1
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                spaceship1.shoot()
            if event.type == pygame.QUIT:
                sys.exit()

        if is_game_over:
            screen.blit(game_over_image, (200, 100))
            background_sound.stop()
            pygame.display.update()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_r]:
                is_game_over = False
                livescounter.number_of_lives = 3
                spaceship1 = Spaceship(screen, screen.get_width() // 2 - 50, screen.get_height() - 100)
                enemyspaceship = EnemySpaceship(screen, 500, 0)
                army_lines = 2
                galaga_army = GalagaArmy(screen, army_lines)
                scoreboard = Scoreboard(screen)
                reverse_bullets = []
                background_sound.play(loops=-1)
            continue

        screen.fill((0, 0, 0))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and spaceship1.x > 0:
            spaceship1.x -= 5
        if pressed_keys[pygame.K_RIGHT] and spaceship1.x < 900:
            spaceship1.x += 5
        if pressed_keys[pygame.K_UP] and spaceship1.y > 500:
            spaceship1.y -= 5
        if pressed_keys[pygame.K_DOWN] and spaceship1.y < 600:
            spaceship1.y += 5

        spaceship1.remove_hit_bullets()
        spaceship1.remove_reverse_bullets(reverse_bullets)
        if number_of_frames % 30 == 0:
            galaga_army.remove_dead()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_r]:
            livescounter.number_of_lives = 3

        for enemyspaceship in galaga_army.enemyspaceships:
            for bullet in spaceship1.bullets:
                if enemyspaceship.hit_by(bullet):
                    scoreboard.score += 100
                    enemyspaceship.is_dead = True
                    bullet.has_hit = True
                    reverse_bullet = ReverseBullet(screen, enemyspaceship.x, enemyspaceship.y)
                    reverse_bullets.append(reverse_bullet)
                    enemyspaceship.onSpace()

        for rb in reverse_bullets:
            if spaceship1.hit_by(rb):
                livescounter.number_of_lives -= 1
                rb.has_hit = True

        if livescounter.number_of_lives == 0:
            is_game_over = True
            lose_sound.play()

        if galaga_army.is_destroyed:
            win_sound.play()
            army_lines += 1
            galaga_army = GalagaArmy(screen, army_lines)

        scoreboard.draw()
        livescounter.draw()
        lostheart.draw()
        galaga_army.draw()
        galaga_army.move()
        spaceship1.draw()
        for bullet in spaceship1.bullets:
            bullet.move()
            bullet.draw()

        for rb in reverse_bullets:
            rb.move()
            rb.draw()

        pygame.display.update()


main()
