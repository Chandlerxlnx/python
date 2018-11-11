import pygame, sys
from pygame.locals import *

import random
from random import choice

RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (100, 0, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 255, 0)


def draw_gallows(screen):
    '''
    function draw a gallow in the screen
    :param screen:
    :return:
    '''
    pygame.draw.rect(screen, PURPLE, (450, 350, 100, 10))  # bottom
    pygame.draw.rect(screen, PURPLE, (450, 250, 10, 100))  # support
    pygame.draw.rect(screen, PURPLE, (450, 250, 50, 10))  # crossbar
    pygame.draw.rect(screen, PURPLE, (450, 350, 10, 25))  # noose


def draw_man(screen, body_part):
    if body_part == "head":
        pygame.draw.circle(screen, RED, (455, 270), 10)  # head
    if body_part == "body":
        pygame.draw.line(screen, RED, (455, 280), (455, 320), 3)  # Body
    if body_part == "l_arm":
        pygame.draw.line(screen, RED, (455, 300), (445, 285), 3)  # arm
    if body_part == "r_arm":
        pygame.draw.line(screen, RED, (455, 300), (465, 285), 3)  # arm
    if body_part == "l_leg":
        pygame.draw.line(screen, RED, (455, 320), (445, 330), 3)  # leg
    if body_part == "r_leg":
        pygame.draw.line(screen, RED, (455, 320), (465, 330), 3)  # leg


def draw_word(screen, spaces):
    x = 10
    for i in range(spaces):
        pygame.draw.line(screen, YELLOW, (x, 350), (x + 20, 350), 3)
        x += 30


def draw_letter(screen, font, word, guess):
    x = 10
    for letter in word:
        letter = font.render(letter, 3, (255, 255, 255))
        screen.blit(letter, (x, 300))
        x += 30


def get_words():
    '''
    get words from words.txt
    :return: words list
    '''
    f = open("words.txt")
    temp = f.readlines()
    words = []
    for word in temp:
        words.append(word.strip())
    return (words)


def main():
    """
      Pygame example
    """
    pygame.init()

    screen = pygame.display.set_mode((600, 400))
    font = pygame.font.SysFont("monospace", 30)
    draw_gallows(screen)
    draw_man(screen, body_part="head")
    # pygame.draw.circle(screen,RED,(20,20),10)

    words = get_words()
    word = choice(words)
    print("the word is ${}, length is ${}".format(word, len(word)))
    print("")

    draw_word(screen, len(word))
    pygame.display.update()

    body = ['r_leg', 'l_leg', 'r_arm', 'l_arm', 'body', 'head']

    while body:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    guess = event.unicode
                    if guess in word:
                        draw_letter(screen, font, word, guess)
                        pygame.display.update()
                    else:
                        body_part = body.pop()
                        draw_man(screen, body_part)
                        pygame.display.update()


if __name__ == '__main__':
    main()
