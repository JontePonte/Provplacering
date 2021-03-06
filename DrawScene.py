
import arcade
import tkinter
import random

# Importera information för helskärm
screen = tkinter.Tk()
screen.withdraw()
SCREEN_WIDTH = screen.winfo_screenwidth()       # SCREEN_WIDTH = antal pixlar i x-led
SCREEN_HEIGHT = screen.winfo_screenheight()     # SCREEN_HEIGHT = antal pixlar i y-led


class PlacementDraw(arcade.Window):
    """
    Rita upp classrummet och placera eleverna utifrån informationen från Main
    """

    def __init__(self, width, height, information):
        super().__init__(width, height, information[0], fullscreen=True)

        # Sortera informationen i "information" från Main
        self.room_name = information[0]
        self.x_num = information[1]
        self.y_num = information[2]
        self.locations = information[3]

        # Variabler som styrs av rummet
        self.x_positions = []               # x-koordinater längst till vänster
        self.y_positions = []               # y-koordinater högst upp
        self.positions = []                 # x, y-koordinater för alla platser

        self.x_bench_positions = []         # Bänkarnas x-position
        self.y_bench_positions = []         # Bänkarnas y-position
        self.bench_height = 1
        self.bench_width = 1

        # Lista med elevernas namn
        self.name_positions = []

        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)

    def setup(self):

        # Denna if fixar allt för "Aula"
        if self.room_name == "Aula" or self.room_name == "Aula_Halvfull":
            self.bench_height = int(SCREEN_HEIGHT / 30)     # Storlek för bänkar i Aulan
            self.bench_width = int(SCREEN_WIDTH / 10)

            self.x_bench_positions = [                      # Sätt x-koordinater för bänkarna i Aulan
                int(1 * SCREEN_WIDTH / 8),
                int(2 * SCREEN_WIDTH / 8),
                int(3 * SCREEN_WIDTH / 8),
                int(5 * SCREEN_WIDTH / 8),
                int(6 * SCREEN_WIDTH / 8),
            ]

            if self.room_name == "Aula_Halvfull":           # Sätt x-koorsinater för skrivplatser i Aulan
                self.x_positions = [                        # Aula_Halvfull beter sig lite annorlunda
                    int(1 * SCREEN_WIDTH / 8),
                    int(3 * SCREEN_WIDTH / 8),
                    int(5 * SCREEN_WIDTH / 8),
                    int(6 * SCREEN_WIDTH / 8),
                ]
            else:
                self.x_positions = self.x_bench_positions   # Normal Aula

            # Sätt y-koordinater för bänkarna i Aulan
            for i in range(20):
                self.y_bench_positions.append(int((i + 1) * SCREEN_HEIGHT / (20 + 2)))

            # Sätt y-koordinater för skrivplatser i Aulan
            if self.room_name == "Aula_Halvfull":
                self.y_positions = self.y_bench_positions[1::2]
            else:
                self.y_positions = self.y_bench_positions

        # Detta fixar allt för normala klassrum
        else:
            for x in range(self.x_num):
                self.x_bench_positions.append(int((x + 1) * SCREEN_HEIGHT / self.x_num))
            for y in range(self.y_num):
                self.y_bench_positions.append(int((y + 1) * SCREEN_HEIGHT / self.y_num))

            self.x_positions = self.x_bench_positions       # Eleverna sitter vid alla bänkar
            self.y_positions = self.y_bench_positions

            self.bench_width = 10
            self.bench_height = 10

        # y = 0 är i botten på klassrummet så y_positions måste köras baklänges
        self.y_positions.reverse()
        if self.room_name == "Aula_Halvfull":
            self.y_bench_positions.reverse()

        # Placera ut alla elevers namn på locations
        for location in self.locations:
            if location.occupied and not (location.x_cor == 2 and location.y_cor == 19):    # Mixerbordet måste bort
                # Skapa en namnposition
                name_position = NamePosition(location.student_name, self.bench_height)
                if self.room_name == "Aula" or self.room_name == "Aula_Halvfull":
                    name_position.x_pos = 4 * SCREEN_WIDTH / 8 + 80 * (0.8 - random.random())
                    name_position.y_pos = 0 - 100 * random.random()
                    name_position.x_start = name_position.x_pos
                    name_position.y_start = name_position.y_pos
                else:
                    name_position.x_pos = 0
                    name_position.y_pos = 0

                # Målpositionen är skrivplatserna
                name_position.x_goal = self.x_positions[location.x_cor]
                name_position.y_goal = self.y_positions[location.y_cor]

                # Sätt in den i name_positions
                self.name_positions.append(name_position)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        # Rita ut bänkarna utifrån x- & y-koordinater
        for x in self.x_bench_positions:
            for y in self.y_bench_positions:
                self.draw_bench(x, y)

        # Rita ut texten med elevernas namn
        for name in self.name_positions:
            name.draw()

        # Rita ut bänknummer
        self.draw_bench_numbers()

        # Rita ut scenen ifall provet är i Aulan
        if self.room_name == "Aula" or self.room_name == "Aula_Halvfull":
            self.draw_aula()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for name in self.name_positions:
            name.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        # if key == arcade.key.Q or arcade.key.ESCAPE:  # Avsluta med "ESC" eller "Q"
        #     exit()
        # Does not work in newer versions of arcade???
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def draw_bench(self, x, y):
        """ Rita ut en skrivplats utifrån x- och y-koordinater """
        arcade.draw_lrtb_rectangle_filled(x, x + self.bench_width, y, y - self.bench_height,
                                          arcade.color.LIGHT_TAUPE)

    def draw_aula(self):
        """ Rita ut en scenen i Aulan """
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT
        x_width = SCREEN_WIDTH / 5
        y_width = SCREEN_HEIGHT / 20
        arcade.draw_lrtb_rectangle_filled(x - x_width, x + x_width, y, y - y_width,
                                          arcade.color.TAUPE_GRAY)
        arcade.draw_text("Scen", x - int(y_width * 0.50), y - int(y_width * 0.95),
                         arcade.color.BLACK, int(y_width * 0.5))

        # Rita ut mixerbordet
        x = self.x_bench_positions[2]           # Tredje kolumnen
        y = self.y_bench_positions[19]          # Sista raden
        arcade.draw_lrtb_rectangle_filled(x, x + self.bench_width, y, y - self.bench_height * 1.2,
                                          arcade.color.BLACK)
        arcade.draw_text("Mixerbord", x + 1, y + 1 - self.bench_height, arcade.color.ANTIQUE_WHITE,
                         int(self.bench_height * 0.7))

    def draw_bench_numbers(self):
        """ Rita ut numrering av bänkarna """
        x = 1
        y = 1
        # Rita ut x numrering
        for position in self.x_bench_positions:
            arcade.draw_text(str(x), position + int(self.bench_width / 2),
                             self.y_bench_positions[0] + int(self.bench_height * .5), arcade.color.BLACK,
                             int(self.bench_height / 2))
            x += 1

        # Rita ut y-numrering
        for position in self.y_bench_positions:
            arcade.draw_text(str(y), self.x_bench_positions[0] - int(self.bench_width / 2),
                             position + 1 - self.bench_height, arcade.color.BLACK,
                             int(self.bench_height / 2))
            y += 1


class NamePosition:
    """ Klass för animering och utritning av elevernas namn """
    def __init__(self, name, bench_height):
        # Variabler koplade till position
        self.x_pos = 0
        self.y_pos = 0
        self.x_goal = 0
        self.y_goal = 0
        self.x_start = 0
        self.y_start = 0

        # Vatiabler kopplade till rörelse
        self.x_vel = 0
        self.y_vel = 0
        self.x_acc = 0.15 + 0.12 * (0.5 - random.random())
        self.y_acc = 0.18 + 0.12 * (0.5 - random.random())

        self.x_vel_max = 1.5 + 1 * (0.5 - random.random())
        self.y_vel_max = 2 + 1 * (0.5 - random.random())

        # Variabler som gör eleverna mer mänskliga
        self.rand_chance = 0.2
        self.x_rand = 0.2
        self.y_rand = 0.2

        # Variabler för skrivandet av namnenq
        self.name = name
        self.bench_height = bench_height

    def draw(self):
        """ Rita ut elevernas namn """
        arcade.draw_text(self.name, self.x_pos + 1, self.y_pos + 1 - self.bench_height, arcade.color.BLACK,
                         int(self.bench_height * 0.5))

    def update(self):
        """ Förflytta namnen till rätt position """

        # Ställ in rätt y-hastighet
        if self.y_pos < self.y_goal:
            self.y_vel = min(self.y_vel + self.y_acc, self.y_vel_max)
        elif self.y_pos > self.y_goal:
            self.y_vel = max(self.y_vel - self.y_vel_max, -self.y_vel_max)

        # Se till at de stannar i y-led innan de börjar gå till sin plats
        right_row = False
        if self.y_goal - 10 < self.y_pos < self.y_goal + 10:
            right_row = True

        # Börja gå in mot raden
        if right_row and self.x_pos < self.x_goal:
            self.x_vel = min(self.x_vel + self.x_acc, self.x_vel_max)
        elif right_row and self. x_pos > self.x_goal:
            self.x_vel = max(self.x_vel - self.x_vel_max, -self.x_vel_max)

        # Slumpa lite rörelse
        if random.random() < self.rand_chance:
            if not right_row and self.x_pos > self.x_start:
                self.x_vel = self.x_vel - self.x_rand * random.random()
            elif not right_row and self.x_pos <= self.x_start:
                self.x_vel = self.x_vel + self.x_rand * random.random()
            self.y_vel = self.y_vel + self.y_rand * (0.5 - random.random())

        # Bromsa in när de närmar sig
        if abs(self.x_pos - self.x_goal) < 2:
            self.x_vel /= 10
            if abs(self.y_pos - self.y_goal) < 2:
                self.y_vel /= 10
        if abs(self.y_pos - self.y_goal) < 2:
            self.y_vel /= 4

        # Förflyttning i x- & y-led
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel


def draw(information):
    """ Main method. Denna funktion anropar hela denna fil """
    game = PlacementDraw(SCREEN_WIDTH, SCREEN_HEIGHT, information)
    game.setup()
    arcade.run()
