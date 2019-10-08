
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

    def placement(self, students, mf):
        """ Placera ut eleverna i klassrummet """

        # Plocka ut eleverna i mf listan från students
        for student in students:
            if "mf" in students:
                students.remove(student)

        # Sätt variabler för längden på alla listor
        num_students = len(students)
        num_locations = len(self.locations)
        num_mf = len(mf)
        # Fyll upp students med "Empty" tills students + mf är lika lång som locations
        students += ["Empty"] * (num_locations - num_mf - num_students)

        # Placera ut elever i mf
        not_placed = len(mf)
        for i in range(len(mf)):
            while not_placed > 1:
                if not self.locations[i].occupied:
                    try:
                        left = self.locations[i-1].occupied
                    except "Exception":
                        left = False
                    try:
                        right = self.locations[i + 1].occupied
                    except "Exception":
                        right = False


        # Placera ut elever i students
        for i in range(len(students)):
            if not self.locations[i].occupied:
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
