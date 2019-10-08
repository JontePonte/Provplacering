""" Main för provplacering """

# Imports
from ClassRoom import ClassRoom


class PlaceStudents:
    """ Mainklass för att skapa klassrummet, placera ut eleverna och rita ut """
    def __init__(self):
        """ Variabler som styr provsalens utseende """

        self.x_num = 5       # Antal platser x-led
        self.y_num = 5       # Antal platser y-led

        # Möjliga varianter för provsal är "Aula", "Hörsal", "zigzag", "normal"
        self.room_type = "normal"
        info = [self.x_num, self.y_num, self.room_type]       # Samla info i info

        self.room = ClassRoom(info)      # Skapa klassrumet

        # Ladda in klasslista
        self.students = self.load_text("test_list.txt")
        for i in range(len(self.students)):
            print(self.students[i])

        # Placera ut eleverna
        self.room.placement(self.students)

        # Skapa listan
        self.export_list()

    def load_text(self, text):
        """ Importera klasslista från textfil """
        with open(text) as f:
            list2 = []
            f = f.read().split(',')                 # Dela upp hela texten vid ","
            for item in f:
                item = item.replace(" ", "").replace("\n", "")
                list2.append(item)
        return list2

    def export_list(self):
        """ Exportera en .txt fil med all relevant information """
        file = open("Placement.txt", "w")

        # Spara informaion om rummet
        file.write("[")
        file.write(self.room_type)
        file.write(",")
        file.write(str(self.x_num))
        file.write(",")
        file.write(str(self.y_num))
        file.write("],")

        # Spara information om alla platser
        for location in self.room.locations:
            file.write("[")
            file.write(location.student_name)
            file.write(",")
            file.write(str(location.x_cor))
            file.write(",")
            file.write(str(location.y_cor))
            file.write("],")

        file.close()


run = PlaceStudents()
