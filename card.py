import turtle
from tkinter import PhotoImage


class Card(turtle.Turtle):
    card_count = 0

    def __init__(self, image_path):
        """
        Initializes Card object.
        :param image_path: Path to image for card_front
        """
        super().__init__()

        self.image_path = image_path
        self.card_id = Card.card_count
        Card.card_count += 1
        self.penup()
        self.speed(8)
        self.back = PhotoImage(file='images/turtle.png').subsample(4, 4)
        turtle.addshape('card_back', turtle.Shape('image', self.back))
        self.front = PhotoImage(file=image_path).subsample(4, 4)
        turtle.addshape(f'card_front{self.card_id}', turtle.Shape('image', self.front))
        self.shape('card_back')

    def __eq__(self, other):
        """
        Checks if two cards have the same front image.
        :param other: Another Card object
        :return: True if cards have the same front image, False otherwise.
        """
        if type(other) is not Card:
            raise TypeError('Can only compare Card objects to other Card objects.')
        else:
            return self.image_path == other.image_path

    def to_front(self):
        self.shape(f'card_front{self.card_id}')

    def to_back(self):
        self.shape('card_back')

    def is_mouse_over(self, x, y):
        # Collision code reused from D. Atkinson's Turtle Crossing program, with some minor modifications.
        # http://tiny.cc/ShortCodeLink
        top_edge = self.ycor() + 103
        bottom_edge = self.ycor() - 103
        car_left_edge = self.xcor() - 103
        car_right_edge = self.xcor() + 103
        if (
                (
                        (y - bottom_edge > 0 and top_edge - y > 0)
                        or
                        (top_edge - y > 0 and y - bottom_edge > 0)
                )
                and
                (
                        (x - car_left_edge > 0 and car_right_edge - x > 0)
                        or
                        (x - car_left_edge > 0 and car_right_edge - x > 0)
                )
        ):
            return True
        return False
