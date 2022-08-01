import turtle
from tkinter import PhotoImage


class Card(turtle.Turtle):
    def __init__(self, image_path):
        """
        Initializes Card object.
        :param image_path: Path to image
        """
        super().__init__()

        # self.size = 150  # desired image height and width (in pixels)
        self.penup()
        self.speed(8)
        self.smaller_back = PhotoImage(file='images/turtle.png').subsample(4, 4)
        turtle.addshape('card_back', turtle.Shape('image', self.smaller_back))
        self.smaller_front = PhotoImage(file=image_path).subsample(4, 4)
        turtle.addshape('card_front', turtle.Shape('image', self.smaller_front))
        self.shape('card_back')

    def to_front(self):
        self.shape('card_front')

    def to_back(self):
        self.shape('card_back')

    def is_mouse_over(self, x, y):
        # Collision code reused from D. Atkinson's Turtle Crossing program, with some minor modifications.
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
