try:
    import os
    import random
    import time
    import turtle

    from card import Card

    # CONSTANTS
    WIDTH = 1600
    HEIGHT = 840
    BACKGROUND_COLOR = (66, 135, 245)

    screen = turtle.Screen()
    turtle.bgcolor('#46a38d')
    screen.setup(WIDTH, HEIGHT)


    def coord_translation(x, y):
        """
        Translates coordinates from the screen to turtle.
        :param x: x coordinate
        :param y: y coordinate
        :return: Translated coordinates
        """
        return x - (WIDTH / 2), y - (HEIGHT / 2)


    # Creates list of images, doubles it, and shuffles it
    image_files = os.listdir('images')
    image_files.remove('turtle.png')
    image_files.extend(image_files)
    random.shuffle(image_files)

    cards = [Card(f'images/{file}') for file in image_files]

    # Move sprites
    for i in range(16):
        # Note: Coordinates start from (0, 0) at top left of screen.
        # Arrange cards in a grid, 4x4, with a margin of 20 pixels between each card.
        # Array from left to right, then top to bottom.
        x, y = coord_translation((210 * (i % 4)) + 105, (210 * int(i / 4)) + 105)
        cards[i].goto(x, y)


    def clicked_card(x, y):
        """
        :return: The card which was clicked
        """
        for card in cards:
            if card.is_mouse_over(x, y):
                print(cards.index(card))
                card.to_front()
                clicked_cards.append(card)


    screen.onclick(fun=clicked_card)

    game_is_running = True
    clicked_cards = []
    score = 0

    while game_is_running:
        time.sleep(0.1)
        if len(clicked_cards) == 2:
            if clicked_cards[0].shape() != clicked_cards[1].shape():
                time.sleep(2)
                clicked_cards[0].to_back()
                clicked_cards[1].to_back()
                print('Wrong!')
                score -= 1
            else:
                print('Correct!')
                score += 5
            clicked_cards = []
        screen.update()

    screen.mainloop()
except turtle.Terminator:
    exit(0)
