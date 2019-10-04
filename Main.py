""" Main för provplacering """

# Imports
import turtle
from ClassRoom import ClassRoom


class PlaceStudents():
    def __init__(selfs):
        """ Variabler som styr provsalens utseende """

        x_num = 5       # Antal platser x-led
        y_num = 5       # Antal platser y-led

        info = [x_num, y_num]       # Samla info i info

        # Skapa klassrumet
        room = ClassRoom(info)

