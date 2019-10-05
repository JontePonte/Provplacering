""" Main för provplacering """

# Imports
import tkinter
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

        # Ladda in klasslista
        self.students = self.load_text("test_list.txt")
        for i in range(len(self.students)):
            print(self.students[i])

        # Placera ut eleverna
        self.room.placement(self.students)
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
tkinter.mainloop()
