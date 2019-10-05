
import turtle


class Pen(turtle.Turtle):
    """ Class för pennan som ritar upp klassrummet """
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("black")
        self.speed(0)

    def draw_desk(self):
        """ Metod för att rita ett bord """


