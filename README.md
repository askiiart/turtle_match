## Memory Game
#### Benjamin Zimmerman

Info for users:
- This is my final project (option 1) for ITSE-1479.
- It is a memory game with a graphical interface.
- You can click on a card to flip it. Match 2 cards correctly and the cards will stay flipped. Match all cards to win.
- Scoring:
  - When you make an incorrect match, you lose 1 point.
  - When you make a correct match, you gain 5 points.

Technical info:
- This program is written in Python 3, using the turtle module for graphics, and the pygame module for sound and music.
- Instead of using the provided cardback.png image, I used a photo of one of my turtles as the card back.
- Notable game behavior: If you make an incorrect match, the cards will flip back over after 1 second. However, if you click on a card while the incorrect match is still face up, nothing will happen.
    - Just wait until the cards flip back over.

Future plans:
- Change the game behavior to a queue of cards to flip over once the incorrect match is flipped back over, instead of just waiting for the cards to flip back over.
- Expand the game to include a stopwatch.
- Expand score to include number of correct and incorrect matches.