import pygame
import sys
import random
import time

white = (63, 138, 66)
class Shadow:
    def __init__(self, screen,x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.shadow_image= pygame.image.load()
        self.speedx = 5
        self.speedy = 5
class Fox:
    def __init__(self, screen, x, y, timeon):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/IMG_0770.PNG")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.draw_image = True
        self.frames = 0
        self.timeon = timeon

    def draw(self):
        if self.draw_image:
            self.screen.blit(self.image, (self.x, self.y))
        self.frames = self.frames + 1
        if self.draw_image:
            if self.frames % self.timeon == 0:
                self.draw_image = False
        else:
            if self.frames % self.timeon == 0:
                self.draw_image = True

    def collide(self, bunny_x, bunny_y):
        if self.draw_image:
            hitbox = pygame.Rect(bunny_x+3, bunny_y, 40, 40)
            foxhitbox = pygame.Rect(self.x, self.y, 40, 40)
            return hitbox.colliderect(foxhitbox)
        return False

class Polygon:
    def __init__(self, screen):
        self.poly3_points = [(50, 200), (250, 200), (250, 250), (500, 250),
                             (500, 300), (200, 300), (200, 250), (150, 250),
                             (150, 300), (100, 300), (100, 250), (50, 250)]
        self.poly2_points = [(0, 0), (100, 0), (100, 50), (50, 50), (50, 100),
                            (100, 100), (100, 150), (50, 150), (50, 350), (0, 350)]

        self.poly1_points = [(0, 350), (150, 350), (150, 400), (50, 400),
                             (50, 450), (250, 450), (250, 550), (0, 550)]
        self.poly4_points = [(150, 100), (350, 100), (350, 150), (500, 150),
                             (500, 200), (300, 200), (300, 150), (150, 150)]
        self.poly5_points = [(150, 0), (550, 0), (550, 50), (500, 50),
                             (500, 100), (400, 100), (400, 50), (250, 50),
                             (250, 100), (200, 100), (200, 50), (150, 50)]
        self.poly6_points = [(400, 500), (450, 500), (450, 450), (500, 450),
                            (500, 500), (550, 500), (550, 0), (600, 0),
                            (600, 550), (400, 550)]
        self.poly7_points = [(200, 350), (500, 350), (500, 400), (400, 400),
                             (400, 550), (300, 550), (300, 400), (200, 400)]
        self.screen = screen

        self.polylines = [self.poly1_points, self.poly2_points,
                          self.poly3_points, self.poly4_points,
                          self.poly5_points, self.poly6_points,
                          self.poly7_points]

    def draw(self):
        pygame.draw.polygon(self.screen, white, self.poly1_points, 0)  # poly1
        pygame.draw.polygon(self.screen, white, self.poly2_points, 0)  # poly2
        pygame.draw.polygon(self.screen, white, self.poly3_points, 0)  # poly3
        pygame.draw.polygon(self.screen, white, self.poly4_points, 0)  # poly4
        pygame.draw.polygon(self.screen, white, self.poly5_points, 0)  # poly5
        pygame.draw.polygon(self.screen, white, self.poly6_points, 0)  # poly6
        pygame.draw.polygon(self.screen, white, self.poly7_points, 0)  # poly7

    def collide(self, bunny_x, bunny_y):
        bunny_rect = pygame.Rect(bunny_x+3, bunny_y, 40, 40)
        for poly_lines in self.polylines:
            for i in range(len(poly_lines)-1):
                if bunny_rect.clipline(poly_lines[i],
                                       poly_lines[i+1]):
                    return True
        return False
        # is_collision1 = bunny_rect.clipline(100, 200, 350, 200)
        # is_collision2 = bunny_rect.clipline(275, 300, 500, 300)
        # is_collision3 = bunny_rect.clipline(150, 400, 400, 400)
        # return is_collision1 != () or is_collision2 != () or is_collision3 != ()


class Lines:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (100, 1), (150, 1), 2)

    def can_collide(self, x, y):
        bunny_rect = pygame.Rect(x + 3, y, 40, 40)
        return bunny_rect.clipline(100, 1, 150, 1)

class Player:
    def __init__(self, screen, x, y, player_left_file, player_right_file, player_down_file, player_up_file):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_left = pygame.image.load(player_left_file)
        self.image_right = pygame.image.load(player_right_file)
        self.image_up = pygame.image.load(player_up_file)
        self.image_down = pygame.image.load(player_down_file)
        self.speedx = 5
        self.speedy = 5

    def draw(self):
        current_image = self.image_down
        self.screen.blit(current_image, (self.x, self.y))
    def collide(self, x, y):
        return False
        return self.collide(x, y)
# def move(self):
#     self.y = self.y + self.speedyss
#     self.x = self.x + self.speedx
#     if self.x <= 0 or self.x >= 550:
#         self.speedx = 0
#     if self.y <= 0 or self.y >= 500:
#         self.speedy = 0


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Garden Escape")

    screen = pygame.display.set_mode((600, 550))

    bunny_x = 250
    bunny_y = 500
    line_x = 100
    line_y = 0

    # let's set the frame rate
    clock = pygame.time.Clock()
    bunny = Player(screen, 300, 400, "assets/left-sm.png", "assets/right-sm.png", "assets/back-sm.png", "assets/front-sm.png")
    line = Lines(screen)
    polygon = Polygon(screen)
    fox1 = Fox(screen, 150, 300, 180)
    fox2 = Fox(screen, 500, 250, 60)
    fox3 = Fox(screen, 350, 100, 300)
    fox4 = Fox(screen, 100, 50, 120)
    start_screen = True

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if start_screen:
            start = pygame.image.load("assets/start_screens.jpg")
            start = pygame.transform.scale(start, (600, 550))
            screen.blit(start, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        start_screen = False
            pygame.display.update()
            continue

        Lose = pygame.image.load("assets/Game_over.png")
        Lose = pygame.transform.scale(Lose, (600, 550))
        if fox1.collide(bunny_x, bunny_y):
            screen.blit(Lose, (0, 0))
            pygame.display.update()
            continue
        if fox2.collide(bunny_x, bunny_y):
            screen.blit(Lose, (0, 0))
            pygame.display.update()
            continue
        if fox3.collide(bunny_x, bunny_y):
            screen.blit(Lose, (0, 0))
            pygame.display.update()
            continue
        if fox4.collide(bunny_x, bunny_y):
            screen.blit(Lose, (0, 0))
            pygame.display.update()
            continue
        winsound= pygame.mixer.Sound("assets/win.mp3")
        Win = pygame.image.load("assets/win_screen.jpg")
        Win = pygame.transform.scale(Win, (600, 550))
        if line.can_collide(bunny_x, bunny_y):
            screen.blit(Win, (0,0))
            winsound.play()
            pygame.display.update()
            continue

        if not line.can_collide(bunny_x, bunny_y):
            pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            if bunny_y > 0:
                if not polygon.collide(bunny_x, bunny_y - bunny.speedy):
                    bunny_y = bunny_y - bunny.speedy
        if pressed_keys[pygame.K_DOWN]:
            if bunny_y < 500:
                if not polygon.collide(bunny_x, bunny_y + bunny.speedy):
                    bunny_y = bunny_y + bunny.speedy
        if pressed_keys[pygame.K_LEFT]:
            if bunny_x > 0:
                if not polygon.collide(bunny_x - bunny.speedx, bunny_y):
                    bunny_x = bunny_x - bunny.speedx
        if pressed_keys[pygame.K_RIGHT]:
            if bunny_x < 550:
                if not polygon.collide(bunny_x + bunny.speedy, bunny_y):
                    bunny_x = bunny_x + bunny.speedx

        screen.fill((212, 191, 123))



        polygon.draw()
        image = pygame.image.load("assets/front-sm.png")
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, (0 + bunny_x, 0 + bunny_y))
        fox1.draw()
        fox2.draw()
        fox3.draw()
        fox4.draw()
        line.draw()
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()
