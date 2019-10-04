import turtle
from Location import Location


class ClassRoom:
    """ Huvudklass för klassrummet. Den tar in information om storlek och platser mha info """
    def __init__(self, info):
        # Ta ut information ur info
        self.x_num = info[0]
        self.y_num = info[1]
        self.room_type = info[2]

        # Skapa tom lista som fylls med skrivplatser
        self.locations = []
        self.pen = turtle.Turtle()
        self.screen = turtle.Screen()

    def create_loactions(self):
        """ Metod som skapar platserna i rummet """
        for x in range(self.x_num):
            for y in range(self.y_num):
                # Skapa en plats med x- & y-koordinat
                info = [x, y]
                location = Location(info)
                self.locations.append(location)    # Spara i "locations"

    def show_room(self):
        """ Rita upp klassrummet mha turtle grafics """
        self.screen = turtle.Screen()
        self.screen.bgcolor("red")
