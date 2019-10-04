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

    def show_room(self):
        """ Anropa show room i room """
        self.room.show_room()

run = PlaceStudents()
run.show_room()
