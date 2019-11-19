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

        # Möjliga varianter för provsal är "Aula", "Normal", "Zigzag",
        self.room_type = "Aula"

        # Ladda in klasslista
        self.students = self.load_text("Elevlista.txt")
        for i in range(len(self.students)):
            print(self.students[i])
        self.mf = self.load_text("MF.txt")  # mf = Misstänkt Fusk. Dessa hamnar inte nära varandra

        if self.room_type == "Aula":    # Specialinställningar för Aula
            self.aula_settings()

        self.fix_list_problems()        # Fixa eventuella problem som kan lösas

        if self.is_problems():          # Avbryt programmet ifall några problem dyker upp och berätta varför
            exit()

        info = [self.x_num, self.y_num, self.room_type]       # Samla info i info

        self.room = ClassRoom(info)      # Skapa klassrumet

        # Placera ut eleverna
        self.room.placement(self.students, self.mf)

        # Skapa listan
        self.export_list()

        # Samla ihop input till draw
        info_to_draw = [
            self.room_type,
            self.x_num,
            self.y_num,
            self.room.locations
            ]
        draw(info_to_draw)  # Anropa funktionen "draw" i "DrawScene" som kör all arcade-kod

    def load_text(self, text):
        """ Importera klasslista från textfil """
        with open(text) as f:
            list2 = []
            f = f.read().split("\n")                 # Dela upp hela texten vid ","
            for item in f:
                item = item.replace(",", "").replace("\n", "")
                list2.append(item)
        return list2

    def aula_settings(self):
        """ Fixa all specialinformation för Aulan """
        self.x_num = 5
        self.y_num = 20
        # Placera eleverna endast på varannan rad ifall det finns plats
        if len(self.students) <= 40:
            self.x_num = 4
            self.y_num = 10
            self.room_type = "Aula_Halvfull"

    def is_problems(self):
        """ Sök upp eventuella problem så att programmet kan avslutas innan """
        problem = False
        # Kolla ifall eleverna får plats
        max_students = self.x_num * self.y_num
        if self.room_type == "Aula":
            max_students -= 1                   # Mixerbordet tar en plats också
        if len(self.students) > max_students:
            print("Impossible! There are more students than places to put them")
            problem = True

        # Kolla att namnen i Elevlista inte är för långa
        for student in self.students:
            if len(student) > 20:
                print("There are to long names in Elevlista (", student, ")")
                problem = True

        # Kolla att eleverna i MF finns med i Elevlista
        for mf_student in self.mf:
            if mf_student not in self.students:
                if len(mf_student) == 0:
                    name = "Empty Row"
                else:
                    name = mf_student
                print("There is a student (", name, ") in MF that is not in Elevlista")
                problem = True

        return problem

    def fix_list_problems(self):
        """ Fixa eventuella problem med listorna som kan lösas """
        # Plocka bort tomma rader i elevlista och låt användaren höra det
        elevlista_empty = 0
        for student in self.students:
            if len(student) == 0:
                elevlista_empty += 1
        if elevlista_empty > 0:
            self.students.remove("")
            print("There are", str(elevlista_empty), "empty rows in Elevlista")

        # Plocka bort tomma rader i MF och låt användaren höra det
        mf_empty = 0
        for student in self.mf:
            if len(student) == 0:
                mf_empty += 1
        if mf_empty > 0:
            self.mf.remove("")
            print("There are", str(mf_empty), "empty rows in MF")

        # Skryt lite
        if mf_empty or elevlista_empty > 0:
            print("Do not worry. The empty rows did not take up any space in the classroom")

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
