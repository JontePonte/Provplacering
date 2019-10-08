
from Location import Location
import random


class ClassRoom:
    """ Huvudklass för klassrummet. Den tar in information om storlek och platser mha info """
    def __init__(self, info):
        # Ta ut information ur info
        self.x_num = info[0]
        self.y_num = info[1]
        self.room_type = info[2]

        # Skapa tom lista som fylls med skrivplatser
        self.locations = []
        self.create_locations()     # Skapa platser i klassrummet

    def placement(self, students):
        """ Placera ut eleverna i klassrummet """

        num_students = len(students)
        num_locations = len(self.locations)
        students = students + ["Empty"]*(num_locations-num_students)
        random.shuffle(students)
        print(students)

        for i in range(len(students)):
            self.locations[i].student_name = students[i]
            self.locations[i].occupied = True

    def create_locations(self):
        """ Metod som skapar platserna i rummet """
        for x in range(self.x_num):
            for y in range(self.y_num):
                # Skapa en plats med x- & y-koordinat
                info = [x, y]
                location = Location(info)
                self.locations.append(location)    # Spara i "locations"
