## Memory Game

Info for users:
- This is my final project (option 1) for ITSE-1479.
- It is a memory game with a graphical interface.

Technical info:
- This program is written in Python 3, using the turtle module for graphics, and the pygame module for sound and music.
- Instead of using the provided cardback.png image, I used a photo of one of my turtles as the card back.
- Game behavior: If you make an incorrect match, the cards will flip back over after 1 second. However, if you click on a card while the incorrect match is still face up, nothing will happen.
    - Just wait until the cards flip back over.
    - This is not a bug, and the program will not crash, but it is not the ideal way I'd like the program to function.
        - I'm working on changing this to function how I'd like (a queue of cards to flip over after the incorrect match is flipped back over), but it is not completed yet.

One last note: Sorry if this README file looks weird. I can't see what I'm writing, because the preview in PyCharm isn't working.
