import pygame


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height):
        """
        Initializes Card object.
        :param image_path: Path of
        :param screen_width:
        :param screen_height:
        """
        super().__init__()
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.rect.move(screen_width / 2, screen_height / 2)

    def is_clicked(self):
        """
        Tests if the sprite is clicked
        :return: Returns True if clicked, False otherwise
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def move(self, x, y):
        """
        Moves to the given x and y coordinates
        :param x: x coordinate
        :param y: y coordinate
        :return: None
        """
        self.rect.move(x, y)

