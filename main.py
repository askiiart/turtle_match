import os
import random
import pygame

from card import Card

# CONSTANTS
WIDTH = 1600
HEIGHT = 900
BACKGROUND_COLOR = (66, 135, 245)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Turtle Cards')

# Creates list of images, doubles it, and shuffles it
image_files = os.listdir('images')
image_files.remove('turtle.jpg')
image_files.extend(image_files)
random.shuffle(image_files)

# Create sprites
cards = [Card(f'images/{file}', WIDTH, HEIGHT) for file in image_files]
for card in cards:
    screen.blit(card.image, card.rect)
pygame.display.flip()

# Move sprites
# TODO: Fix initial movement of sprites
for i in range(16):
    # Note: Coordinates start from (0, 0) at top left of screen.
    # Arrange cards in a grid, 4x4, with a margin of 20 pixels between each card.
    # Array from left to right, then top to bottom.
    cards[i].move((150 * (i % 4)) + 85, (150 * int(i / 4)) + 85)
    print(str((150 * (i % 4)) + 85), str((150 * int(i / 4)) + 85))
    print(cards[i].rect)

game_is_running = True

while game_is_running:
    # Draw things
    screen.fill(BACKGROUND_COLOR)
    for card in cards:
        screen.blit(card.image, card.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        clicked_cards = []
        for card in cards:
            if card.is_clicked():
                clicked_cards.append(card)
                card.on_click()
                card.flip_card()
    cards[0].move(1, 0)
    pygame.display.flip()
