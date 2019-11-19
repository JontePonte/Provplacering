
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

        # Plocka ut eleverna i mf-listan från students-listan
        for student in mf:
            students.remove(student)

        # Fix av längden på students. Fyll upp hålrum med "Empty"
        num_students = len(students)
        num_locations = len(self.locations)
        num_mf = len(mf)
        # Tillsammans blir students & mf är lika lång som locations
        students += ["Empty"] * (num_locations - (num_mf + num_students))

        if self.room_type == "Aula":
            x = 2
            y = 19
            for location in self.locations:
                if location.x_cor == x and location.y_cor == y:
                    location.occupied = True
                    location.student_name = ""

        # Placera ut eleverna i mf först. De hamnar minst två platser ifrån varandra i x- & y-led
        for student in mf:
            placed = False
            test = 0
            while not placed:
                # De ges en slumpposition x, y
                x = random.randint(0, self.x_num-1)
                y = random.randint(0, self.y_num-1)
                # Kolla alla platser runt x & y
                placed = True
                for location in self.locations:
                    if location.x_cor - 1 <= x <= location.x_cor + 1 and location.y_cor - 1 <= y <= location.y_cor + 1:
                        # Om någon är upptagen så starta om
                        if location.occupied:
                            placed = False

                test += 1       # Testa ifall placeringen inte fungerar och stoppa isf
                if test > 200:
                    print("To many students in MF. The students could not be placed.")
                    exit()

            # Placera ut eleven på platsen med koordinaterna x & y
            for location in self.locations:
                if location.x_cor == x and location.y_cor == y:
                    location.student_name = student
                    location.occupied = True

        # Placera ut resten av elever i students
        random.shuffle(students)
        i = 0
        for location in self.locations:
            if location.occupied:
                pass
            else:
                location.student_name = students[i]
                if not location.student_name == "Empty":
                    location.occupied = True
                i += 1

    def create_locations(self):
        """ Metod som skapar platserna i rummet """
        for y in range(self.y_num):
            for x in range(self.x_num):
                # Skapa en plats med x- & y-koordinat
                info = [x, y]
                location = Location(info)
                self.locations.append(location)    # Spara i "locations"
