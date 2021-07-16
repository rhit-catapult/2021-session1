import pygame
import sys
import random
import time
import math

simon_replay_notes = dict()

class Note:
    def __init__(self, screen, color, note, x, y, width, height):
        self.screen = screen
        self.color = color
        self.note = note
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.original_color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)

    def play(self):
        self.note.play()

    def stop(self):
        self.note.stop()

def generate_random_note():
    all_notes = ['A', 'W', 'S', 'E', 'D', 'R', 'F', 'G', 'Y', 'H', 'U', 'J']
    index = random.randint(0, 11)
    return all_notes[index]

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.current_round = 1
        self.current_notes = [generate_random_note()]
        self.current_turn = 0
        self.key_to_note = dict()
        self.key_to_note[pygame.K_a] = 'A'
        self.key_to_note[pygame.K_w] = 'W'
        self.key_to_note[pygame.K_s] = 'S'
        self.key_to_note[pygame.K_e] = 'E'
        self.key_to_note[pygame.K_d] = 'D'
        self.key_to_note[pygame.K_r] = 'R'
        self.key_to_note[pygame.K_f] = 'F'
        self.key_to_note[pygame.K_g] = 'G'
        self.key_to_note[pygame.K_y] = 'Y'
        self.key_to_note[pygame.K_h] = 'H'
        self.key_to_note[pygame.K_u] = 'U'
        self.key_to_note[pygame.K_j] = 'J'
        print(self.current_notes)
        self.is_game_over = False
        self.font = pygame.font.Font(None, 40)
        self.score = 0
        self.start_ticks = pygame.time.get_ticks()
        self.replay_ticks = pygame.time.get_ticks()
        self.played_note = False
        self.note_play_time = 0
        self.current_index = 0
        self.add_delay = False
        self.delay_start = 0
        self.time_limit = 5.0
        self.display_time = False

        self.replay_notes()

    def take_turn(self, event):
        key = event.key
        if key in self.key_to_note:
            correct_note = self.current_notes[self.current_turn]
            if correct_note == self.key_to_note[key]:
                if self.current_turn < len(self.current_notes) - 1:
                    self.current_turn += 1
                    self.start_ticks = pygame.time.get_ticks()
                    # print('You have won a turn')
                else:
                    self.win_round()
                    self.score += 1
                    self.time_limit += 1
                    self.current_index = 0
                    self.replay_ticks = pygame.time.get_ticks()
                    self.add_delay = True
                    self.delay_start = pygame.time.get_ticks()
                    self.display_time = False

                    self.replay_notes()
                    # print('You have won a round')
            else:
                # print('You have lost')
                self.is_game_over = True
                self.lose_game()
        else:
            # print('You have lost')
            self.is_game_over = True
            self.lose_game()

    def win_round(self):
        self.current_turn = 0
        self.current_round += 1
        self.current_notes.append(generate_random_note())
        print(self.current_notes)
        self.start_ticks = pygame.time.get_ticks()

    def lose_game(self):
        for key, value in simon_replay_notes.items():
            value.color = value.original_color
            value.stop()

    def replay_notes(self):
        if self.add_delay:
            delay = (pygame.time.get_ticks() - self.delay_start) / 1000
            if delay >= 0.5:
                self.add_delay = False
                self.replay_ticks = pygame.time.get_ticks()
            else:
                return
        time_difference = (pygame.time.get_ticks() - self.replay_ticks) / 1000
        index = math.floor(time_difference)
        if index <= len(self.current_notes):
            if index != self.current_index:
                simon_replay_notes[self.current_notes[self.current_index]].stop()
                simon_replay_notes[self.current_notes[self.current_index]].color \
                    = simon_replay_notes[self.current_notes[self.current_index]].original_color
                self.played_note = False
                self.current_index = index
                if index == len(self.current_notes):
                    self.start_ticks = pygame.time.get_ticks()
                    self.display_time = True
        if index < len(self.current_notes):
            if not self.played_note:
                simon_replay_notes[self.current_notes[index]].play()
                self.note_play_time = pygame.time.get_ticks()
                simon_replay_notes[self.current_notes[index]].color = (255, 102, 102)
                self.played_note = True
            # else:
            #     local_time_diff = (pygame.time.get_ticks() - self.note_play_time) / 1000
            #     if local_time_diff >= (1 - (1/60)):
            #         simon_replay_notes[self.current_notes[index]].stop()
            #         simon_replay_notes[self.current_notes[index]].color \
            #             = simon_replay_notes[self.current_notes[index]].original_color
            #         self.played_note = False

    def draw(self):
        # message = ''
        # for current in self.current_notes:
        #     message = current + ' '
        # rendered_image = self.font.render(message, True, (0, 0, 0))
        # self.screen.blit(rendered_image, (320 - rendered_image.get_width() // 2, 330))
        score_text = 'Score: {}'.format(self.score)
        score_image = self.font.render(score_text, True, (0, 0, 0))
        self.screen.blit(score_image, (480 - score_image.get_width() // 2, 30))
        ticks = (pygame.time.get_ticks() - self.start_ticks) / 1000
        time_remaining = self.time_limit - ticks
        time_text = 'Time: {:.0f}'.format(time_remaining)
        time_image = self.font.render(time_text, True, (0, 0, 0))
        if self.display_time:
            self.screen.blit(time_image, (160 - time_image.get_width() // 2, 30))
        if time_remaining <= 0:
            self.is_game_over = True
        self.replay_notes()

def main():
    pygame.mixer.init()
    pygame.init()

    pygame.display.set_caption("Synthesizer Simon")
    screen = pygame.display.set_mode((640, 480))

    game_over_sound = pygame.mixer.Sound("game_over.wav")

    w_color = (255, 255, 255)
    blk_color = (0, 0, 0)
    red_color = (255, 0, 0)
    orange_color = (255, 165, 0)
    yellow_color = (255, 255, 0)
    green_color = (0, 128, 0)
    blue_color = (0, 0, 255)
    indigo_color = (75, 0, 130)
    violet_color = (238, 130, 238)

    reor_color = (255, 83, 0)
    orye_color = (255, 210, 0)
    yege_color = (123, 192, 0)
    blin_color = (38, 0, 193)
    invi_color = (157, 65, 184)

    is_game_over = False
    menu_music = True
    starting_splash = True
    credits_screen = False
    simon_mode = False

    biggest_font = pygame.font.Font(None, 60)
    big_font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)
    middle_font = pygame.font.Font(None, 40)
    dr_font = pygame.font.Font(None, 25)

    you_lose_text = big_font.render("Game Over.", True, blk_color)
    restart_text = big_font.render('Press "B" to restart.', True, blk_color)

    freeplay_end_text = big_font.render('Press "=" to end game.', True, blk_color)
    main_menu_text = big_font.render('Press "=" to go back to main menu.', True, blk_color)
    credits_main_text = middle_font.render('Press "-" to go back to main menu.', True, blk_color)
    freeplay_image = pygame.image.load("freeplay.png")
    simon_image = pygame.image.load("simon.png")
    main_simon_text = dr_font.render('Simon Mode', True, blk_color)
    main_freeplay_text = dr_font.render('Free play Mode', True, blk_color)

    # Splash Text ---------------------------------------------------------------------------------

    splash_text = big_font.render('Synthesizer Simon', True, blk_color)
    freeplay_splash_text = small_font.render('Press "1" to play.', True, blk_color)
    credits_splash_text = small_font.render('Press "Backspace" to open credits.', True, blk_color)
    simon_splash_text = small_font.render('Press "2" to play.', True, blk_color)


    # Credits text --------------------------------------------------------------------------------

    main_credits_text = biggest_font.render('Game Developed By:', True, blk_color)
    nick_hinds_text = small_font.render('Nick Hinds - Lino Lakes, Minnesota', True, (0, 128, 255))
    joshua_suggs_text = small_font.render('Joshua Suggs - Cambridge, Maryland', True, (52, 255, 255))
    nima_asadi_text = small_font.render('Nima Asadi - Terre Haute, Indiana', True, (150, 100, 255))
    jonah_marin_text = small_font.render('Jonah Marin - Mesa, Arizona', True, (150, 0, 0))
    dr_noureddine_text = dr_font.render('Special thank you to Dr. Noureddine!', True, blk_color)

    # Key text --------------------------------------------------------------------------------

    a_control_text = big_font.render('A', True, blk_color)
    s_control_text = big_font.render('S', True, blk_color)
    d_control_text = big_font.render('D', True, blk_color)
    f_control_text = big_font.render('F', True, blk_color)
    g_control_text = big_font.render('G', True, blk_color)
    h_control_text = big_font.render('H', True, blk_color)
    j_control_text = big_font.render('J', True, blk_color)

    w_control_text = small_font.render('W', True, w_color)
    e_control_text = small_font.render('E', True, w_color)
    r_control_text = small_font.render('R', True, w_color)
    y_control_text = small_font.render('Y', True, w_color)
    u_control_text = small_font.render('U', True, w_color)

    # ------------------------------------------------------------------------------------------

    clock = pygame.time.Clock()
    f_note = Note(screen, w_color, pygame.mixer.Sound("f_note.wav"), 103, 100, 62, 200)
    simon_replay_notes['A'] = f_note
    f_sharp_note = Note(screen, blk_color, pygame.mixer.Sound("f_sharp_note.wav"), 151, 100, 28, 120)
    simon_replay_notes['W'] = f_sharp_note
    g_note = Note(screen, w_color, pygame.mixer.Sound("g_note.wav"), 165, 100, 62, 200)
    simon_replay_notes['S'] = g_note
    g_sharp_note = Note(screen, blk_color, pygame.mixer.Sound("g_sharp_note.wav"), 213, 100, 28, 120)
    simon_replay_notes['E'] = g_sharp_note
    a_note = Note(screen, w_color, pygame.mixer.Sound("a_note.wav"), 227, 100, 62, 200)
    simon_replay_notes['D'] = a_note
    a_sharp_note = Note(screen, blk_color, pygame.mixer.Sound("a_sharp_note.wav"), 275, 100, 28, 120)
    simon_replay_notes['R'] = a_sharp_note
    b_note = Note(screen, w_color, pygame.mixer.Sound("b_note.wav"), 289, 100, 62, 200)
    simon_replay_notes['F'] = b_note
    c_note = Note(screen, w_color, pygame.mixer.Sound("c_note.wav"), 351, 100, 62, 200)
    simon_replay_notes['G'] = c_note
    c_sharp_note = Note(screen, blk_color, pygame.mixer.Sound("c_sharp_note.wav"), 399, 100, 28, 120)
    simon_replay_notes['Y'] = c_sharp_note
    d_note = Note(screen, w_color, pygame.mixer.Sound("d_note.wav"), 413, 100, 62, 200)
    simon_replay_notes['H'] = d_note
    d_sharp_note = Note(screen, blk_color, pygame.mixer.Sound("d_sharp_note.wav"), 461, 100, 28, 120)
    simon_replay_notes['U'] = d_sharp_note
    e_note = Note(screen, w_color, pygame.mixer.Sound("e_note.wav"), 475, 100, 62, 200)
    simon_replay_notes['J'] = e_note

    game = None
    score_text = 0

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if simon_mode:
                    game.take_turn(event)
                    if game.is_game_over:
                        is_game_over = True
                        simon_mode = False
                        score_text = game.score
                        del game
                        game_over_sound.play()
                        continue

                if event.key == pygame.K_a:
                    f_note.play()
                    f_note.color = red_color

                if event.key == pygame.K_w:
                    f_sharp_note.play()
                    f_sharp_note.color = reor_color

                if event.key == pygame.K_s:
                    g_note.play()
                    g_note.color = orange_color

                if event.key == pygame.K_e:
                    g_sharp_note.play()
                    g_sharp_note.color = orye_color

                if event.key == pygame.K_d:
                    a_note.play()
                    a_note.color = yellow_color

                if event.key == pygame.K_r:
                    a_sharp_note.play()
                    a_sharp_note.color = yege_color

                if event.key == pygame.K_f:
                    b_note.play()
                    b_note.color = green_color

                if event.key == pygame.K_g:
                    c_note.play()
                    c_note.color = blue_color

                if event.key == pygame.K_y:
                    c_sharp_note.play()
                    c_sharp_note.color = blin_color

                if event.key == pygame.K_h:
                    d_note.play()
                    d_note.color = indigo_color

                if event.key == pygame.K_u:
                    d_sharp_note.play()
                    d_sharp_note.color = invi_color

                if event.key == pygame.K_j:
                    e_note.play()
                    e_note.color = violet_color

# -------------- Text Keys -------------- #

                if pressed_keys[pygame.K_1]:
                    starting_splash = False
                    credits_screen = False
                    is_game_over = False
                    simon_mode = False
                    menu_music = False
                    pygame.mixer.music.stop()

                if pressed_keys[pygame.K_b]:
                    is_game_over = False
                    simon_mode = True
                    game = Game(screen)
                    starting_splash = False
                    credits_screen = False

                if pressed_keys[pygame.K_BACKSPACE]:
                    starting_splash = False
                    credits_screen = True
                    is_game_over = False
                    simon_mode = False

                if pressed_keys[pygame.K_EQUALS]:
                    starting_splash = True
                    is_game_over = False
                    credits_screen = False
                    simon_mode = False
                    menu_music = True

                if pressed_keys[pygame.K_MINUS]:
                    starting_splash = True
                    is_game_over = False
                    credits_screen = False
                    simon_mode = False

                if pressed_keys[pygame.K_2]:
                    simon_mode = True
                    starting_splash = False
                    menu_music = False
                    pygame.mixer.music.stop()
                    game = Game(screen)
                    credits_screen = False

# --------------------------------------- #

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    f_note.stop()
                    f_note.color = w_color

                if event.key == pygame.K_w:
                    f_sharp_note.stop()
                    f_sharp_note.color = blk_color

                if event.key == pygame.K_s:
                    g_note.stop()
                    g_note.color = w_color

                if event.key == pygame.K_e:
                    g_sharp_note.stop()
                    g_sharp_note.color = blk_color

                if event.key == pygame.K_d:
                    a_note.stop()
                    a_note.color = w_color

                if event.key == pygame.K_r:
                    a_sharp_note.stop()
                    a_sharp_note.color = blk_color

                if event.key == pygame.K_f:
                    b_note.stop()
                    b_note.color = w_color

                if event.key == pygame.K_g:
                    c_note.stop()
                    c_note.color = w_color

                if event.key == pygame.K_y:
                    c_sharp_note.stop()
                    c_sharp_note.color = blk_color

                if event.key == pygame.K_h:
                    d_note.stop()
                    d_note.color = w_color

                if event.key == pygame.K_u:
                    d_sharp_note.stop()
                    d_sharp_note.color = blk_color

                if event.key == pygame.K_j:
                    e_note.stop()
                    e_note.color = w_color

        screen.fill(w_color)
        c_note.draw()
        d_note.draw()
        e_note.draw()
        f_note.draw()
        g_note.draw()
        a_note.draw()
        b_note.draw()
        c_sharp_note.draw()
        d_sharp_note.draw()
        f_sharp_note.draw()
        g_sharp_note.draw()
        a_sharp_note.draw()
        screen.blit(freeplay_end_text, (320 - freeplay_end_text.get_width() // 2, 400))

        # Key text --------------------------------------------------------------------------------

        screen.blit(a_control_text, (134 - a_control_text.get_width() // 2, 250))
        screen.blit(s_control_text, (196 - s_control_text.get_width() // 2, 250))
        screen.blit(d_control_text, (258 - d_control_text.get_width() // 2, 250))
        screen.blit(f_control_text, (320 - f_control_text.get_width() // 2, 250))
        screen.blit(g_control_text, (382 - g_control_text.get_width() // 2, 250))
        screen.blit(h_control_text, (444 - h_control_text.get_width() // 2, 250))
        screen.blit(j_control_text, (506 - j_control_text.get_width() // 2, 250))

        screen.blit(w_control_text, (165 - w_control_text.get_width() // 2, 190))
        screen.blit(e_control_text, (227 - e_control_text.get_width() // 2, 190))
        screen.blit(r_control_text, (289 - r_control_text.get_width() // 2, 190))
        screen.blit(y_control_text, (413 - y_control_text.get_width() // 2, 190))
        screen.blit(u_control_text, (475 - u_control_text.get_width() // 2, 190))

        # ------------------------------------------------------------------------------------------

        if simon_mode:
            game.draw()
            if game.is_game_over:
                is_game_over = True
                simon_mode = False
                score_text = game.score
                del game

        if is_game_over:
            screen.fill(w_color)
            screen.blit(you_lose_text, (320 - you_lose_text.get_width() // 2, 50))
            screen.blit(restart_text, (320 - restart_text.get_width() // 2, 250))
            screen.blit(main_menu_text, (320 - main_menu_text.get_width() // 2, 400))
            score_font = pygame.font.Font(None, 40)
            score_message = 'Score: {}'.format(score_text)
            score_image = score_font.render(score_message, True, blk_color)
            screen.blit(score_image, (320 - score_image.get_width() // 2, 100))

        if starting_splash:
            screen.fill(w_color)
            screen.blit(splash_text, (320 - splash_text.get_width() // 2, 30))
            screen.blit(credits_splash_text, (320 - credits_splash_text.get_width() // 2,
                                              screen.get_height() - credits_splash_text.get_height() - 30))
            screen.blit(freeplay_image, (140 - freeplay_image.get_width() // 2, 150))
            screen.blit(freeplay_splash_text, (140 - freeplay_splash_text.get_width() // 2, 250))
            screen.blit(simon_image, (500 - simon_image.get_width() // 2, 150))
            screen.blit(simon_splash_text, (500 - simon_splash_text.get_width() // 2, 250))
            screen.blit(main_simon_text, (500 - main_simon_text.get_width() // 2, 285))
            screen.blit(main_freeplay_text, (140 - main_freeplay_text.get_width() // 2, 285))

        if credits_screen:
            screen.fill(w_color)
            screen.blit(main_credits_text, (320 - main_credits_text.get_width() // 2, 25))
            screen.blit(credits_main_text, (320 - credits_main_text.get_width() // 2, 425))
            screen.blit(nick_hinds_text, (320 - nick_hinds_text.get_width() // 2, 125))
            screen.blit(nima_asadi_text, (320 - nima_asadi_text.get_width() // 2, 175))
            screen.blit(joshua_suggs_text, (320 - joshua_suggs_text.get_width() // 2, 225))
            screen.blit(jonah_marin_text, (320 - jonah_marin_text.get_width() // 2, 275))
            screen.blit(dr_noureddine_text, (320 - dr_noureddine_text.get_width() // 2, 350))

        if menu_music:
            # print('Playing')
            pygame.mixer.music.load("menu_music.mp3")
            pygame.mixer.music.play(-1)
            menu_music = False

        pygame.display.update()

main()
