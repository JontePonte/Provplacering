""" Main för provplacering """

# Imports
from ClassRoom import ClassRoom
from DrawScene import draw


class PlaceStudents:
    """ Mainklass för att skapa klassrummet, placera ut eleverna och rita ut """
    def __init__(self):
        """ Variabler som styr provsalens utseende """

        self.x_num = 6       # Antal platser x-led
        self.y_num = 6       # Antal platser y-led

        # Möjliga varianter för provsal är "Aula", "Hörsal", "zigzag", "normal"
        self.room_type = "Aula_Halvfull"
        if self.room_type == "Aula" or "Aula_Full":
            self.x_num = 5
            self.y_num = 20
        if self.room_type == "Aula_Halvfull":
            self.x_num = 4
            self.y_num = 10
        info = [self.x_num, self.y_num, self.room_type]       # Samla info i info

        self.room = ClassRoom(info)      # Skapa klassrumet

        # Ladda in klasslista
        self.students = self.load_text("Elevlista.txt")
        for i in range(len(self.students)):
            print(self.students[i])
        self.mf = self.load_text("MF.txt")      # mf = Misstänkt Fusk. Dessa hamnar inte nära varandra

        # Placera ut eleverna
        self.room.placement(self.students, self.mf)

        # Skapa listan
        self.export_list()

        """ Rita rummet """
        # Samla ihop input till draw
        info_to_draw = [
            self.room_type,
            self.x_num,
            self.y_num,
            self.room.locations
            ]
        draw(info_to_draw)

    def load_text(self, text):
        """ Importera klasslista från textfil """
        with open(text) as f:
            list2 = []
            f = f.read().split("\n")                 # Dela upp hela texten vid ","
            for item in f:
                item = item.replace(",", "").replace("\n", "")
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
        file.write("\n")

        # Spara information om alla platser
        loc = self.room.locations
        i = 0
        for y in range(self.y_num):
            for x in range(self.x_num):
                file.write("[")
                file.write(loc[i].student_name)
                file.write(",")
                file.write(str(loc[i].x_cor))
                file.write(",")
                file.write(str(loc[i].y_cor))
                file.write("],")
                i += 1
            file.write("\n")            # Byt rad då y ökar

        file.close()


""" Kör programmet """
run = PlaceStudents()
