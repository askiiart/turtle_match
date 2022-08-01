from audio import Audio

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
    screen.title('Turtle Match - Benjamin Zimmerman')

    Audio.start_audio()
    Audio.play_background_music()

    # Scoreboard
    score_text = turtle.Turtle()
    score_text.hideturtle()
    score_text.penup()
    score_text.goto((WIDTH - HEIGHT) // 2, HEIGHT * .25)
    score_text.write('Score: 0', font=('Arial', 24, 'bold'))


    def coord_translation(x, y):
        """
        Translates coordinates from the screen to turtle.
        :param x: x coordinate
        :param y: y coordinate
        :return: Translated coordinates
        """
        return x - (WIDTH / 2), y - (HEIGHT / 2)


    image_files = os.listdir('images')

    # Creates list of images, doubles it, and shuffles it
    image_files.remove('turtle.png')
    image_files.extend(image_files)
    random.shuffle(image_files)

    cards = []
    for file in image_files:
        path = f'images/{file}'
        cards.append(Card(path))

    # Move sprites
    for i in range(16):
        # Note: Coordinates start from (0, 0) at top left of screen.
        # Arrange cards in a grid, 4x4, with a margin of 20 pixels between each card.
        # Array from left to right, then top to bottom.
        x, y = coord_translation((210 * (i % 4)) + 105, (210 * int(i / 4)) + 105)
        cards[i].goto(x, y)

    score = 0
    game_is_running = True
    clicked_cards = []

    def clicked_card(x, y):
        """
        :return: The card which was clicked
        """
        Audio.click()
        global clicked_cards
        for card in cards:
            if card.is_mouse_over(x, y):
                if len(clicked_cards) == 2:
                    clicked_cards = []
                card.to_front()
                clicked_cards.append(card)


    def update_score():
        score_text.clear()
        score_text.write(f'Score: {score}', font=('Arial', 24, 'bold'))


    screen.onclick(fun=clicked_card)

    while game_is_running:
        time.sleep(0.1)
        if len(clicked_cards) == 2:
            if clicked_cards[0] != clicked_cards[1]:
                time.sleep(1)
                clicked_cards[0].to_back()
                clicked_cards[1].to_back()
                score -= 1
                update_score()
                Audio.no_match()
            else:
                score += 5
                update_score()
                Audio.match_made()
            clicked_cards = []
        screen.update()

    screen.mainloop()
except turtle.Terminator:
    exit(0)
