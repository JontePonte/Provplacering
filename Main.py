""" Main för provplacering """

# Imports
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
        self.show_room()

        def show_room(self):
            """ Rita upp klassrummet mha turtle grafics """