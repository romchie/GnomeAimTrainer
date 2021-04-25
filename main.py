import os
import sys
import time
import random
import argparse
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def randomPos():
    x = random.randrange(0, 1231)
    y = random.randrange(0, 691)
    return (x, y)

def randomColor():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return (r, g, b)

def calculateScore(h, c):
    try:
        mult = (h / c) + 1
    except ZeroDivisionError:
        sys.exit()
    score = round((h * mult), 4)
    print("\n\t<< Kills:", str(h) + " >>")
    print("\t<< Accuracy:", str(round(((h / c) * 100), 2)) + "% >>")
    print("\t<< Score:", str(score) + " >>\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ct", "--customtime", help="manually enter the amount of game time in seconds (defaults to 60)")

    args = parser.parse_args()
    try:
        total_time = int(args.customtime)
    except TypeError:
        total_time = 60

    pygame.init()

    colors = randomColor()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    button = pygame.image.load('assets/gnome.png').convert_alpha()
    button = pygame.transform.scale(button, (50, 75))
    button_pos = randomPos()
    mask = pygame.mask.from_surface(button)

    pygame.mixer.music.load("assets/targets.mp3")
    pygame.mixer.music.play(loops=-1)
    hit_sound = pygame.mixer.Sound("assets/gnome.wav")

    clicks = 0
    hits = 0
    main_loop = True
    start_time = time.time()
    while main_loop:
        if time.time() - start_time > total_time:
            main_loop = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                print("\n*** NOTE: game stopped prematurely ***")
                main_loop = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                clicks += 1
                try:
                    if mask.get_at((e.pos[0]-button_pos[0], e.pos[1]-button_pos[1])):
                        hit_sound.play()
                        hits += 1
                        button_pos = randomPos()
                except IndexError:
                    pass

        screen.fill(colors)
        screen.blit(button, button_pos)
        pygame.display.flip()

    calculateScore(hits, clicks)
    pygame.mixer.music.stop()

main()
