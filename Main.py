""" Main för provplacering """

# Imports
import turtle
from ClassRoom import ClassRoom


class PlaceStudents:
    """ Mainklass för att skapa klassrummet, placera ut eleverna och rita ut """
    def __init__(self):
        """ Variabler som styr provsalens utseende """

        x_num = 5       # Antal platser x-led
        y_num = 5       # Antal platser y-led

        # Möjliga varianter för provsal är "Aula", "Hörsal", "zigzag", "normal"
        room_type = "normal"

        info = [x_num, y_num, room_type]       # Samla info i info

        self.room = ClassRoom(info)      # Skapa klassrumet
        self.room.create_loactions()     # Skapa platser i klassrummet

        # Ladda in klasslista
        self.students = self.load_text("test_list.txt")
        for i in range(len(self.students)):
            print(self.students[i])

        # Placera ut eleverna
        self.placement()

    def placement(self):
        """ Placera ut eleverna i klassrummet """
        for i in range(len(self.students)):
            self.room.locations[i].student_name = self.students[i]
            self.room.locations[i].occupied = True

        for location in self.room.locations:
            print(location.student_name)
            print(location.occupied)
            print(location.x_cor)
            print(location.x_cor)

    def show_room(self):
        """ Anropa show room i room """
        self.room.show_room()

    def load_text(self, text):
        """ Importera klasslista från textfil """
        with open(text) as f:
            list2 = []
            f = f.read().split(',')                 # Dela upp hela texten vid ","
            for item in f:
                item = item.replace(" ", "")        # Ta bort mellanslag
                list2.append(item)
        return list2


run = PlaceStudents()
run.show_room()
