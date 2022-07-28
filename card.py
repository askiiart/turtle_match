import pygame
from image_sprite import ImageSprite


class Card(ImageSprite):
    def __init__(self, image_path, screen_width, screen_height):
        """
        Initializes Card object.
        :param image_path: Path to image
        :param screen_width: Width of screen
        :param screen_height: Height of screen
        """
        super().__init__(image_path, screen_width, screen_height)

        self.size = 150  # image height and width (in pixels)
        self.card_back = pygame.transform.scale(pygame.image.load('images/turtle.jpg'), (self.size, self.size))
        self.card_front = pygame.transform.scale(pygame.image.load(image_path), (self.size, self.size))
        self.image = self.card_back

        self.temp_count = 0

    def flip_card(self):
        if self.image == self.card_back:
            self.image = self.card_front
        else:
            self.image = self.card_back
