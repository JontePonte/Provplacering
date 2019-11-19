
import arcade
import tkinter

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

            for i in range(20):                             # Sätt y-koordinater för bänkarna i Aulan
                self.y_bench_positions.append(int((i + 1) * SCREEN_HEIGHT / (20 + 2)))

            if self.room_name == "Aula_Halvfull":           # Sätt y-koordinater för skrivplatser i Aulan
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

    def draw_bench(self, x, y):
        """ Rita ut en skrivplats utifrån x- och y-koordinater """
        arcade.draw_lrtb_rectangle_filled(x, x + self.bench_width, y, y - self.bench_height,
                                          arcade.color.LIGHT_TAUPE)

    def draw_aula_scene(self):
        """ Rita ut en scenen i Aulan """
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT
        x_width = SCREEN_WIDTH / 5
        y_width = SCREEN_HEIGHT / 20
        arcade.draw_lrtb_rectangle_filled(x - x_width, x + x_width, y, y - y_width,
                                          arcade.color.TAUPE_GRAY)
        arcade.draw_text("Scen", x - int(y_width * 0.50), y - int(y_width * 0.95),
                         arcade.color.BLACK, int(y_width * 0.5))

    def draw_student_names(self):
        """ Rita ut elevernas namn på de platserna som slumpats fram """

        for location in self.locations:
            if location.occupied:
                arcade.draw_text(location.student_name, self.x_positions[location.x_cor] + 1,
                                 self.y_positions[location.y_cor] + 1 - self.bench_height, arcade.color.BLACK,
                                 int(self.bench_height * 0.7))

    def draw_bench_numbers(self):
        """ Rita ut numrering av bänkarna """
        # Aulan har lite speciell numrering. (Gäller egentligen bara "Aula_Halvfull")
        if self.room_name == "Aula" or "Aula_Halvfull":
            x = 1
            y = 20
        # Annars räkna upp x och räkna ner y då 0,0 är vänster nere
        else:
            x = 1
            y = self.y_num

        # Rita ut x numrering
        for position in self.x_bench_positions:
            arcade.draw_text(str(x), position + int(self.bench_width / 2),
                             self.y_bench_positions[-1] + int(self.bench_height * .5), arcade.color.BLACK,
                             int(self.bench_height / 2))
            x += 1

        # Rita ut y-numrering
        for position in self.y_bench_positions:
            arcade.draw_text(str(y), self.x_positions[0] - int(self.bench_width / 2),
                             position + 1 - self.bench_height, arcade.color.BLACK,
                             int(self.bench_height / 2))
            y -= 1

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        # Rita ut bänkarna utifrån x- & y-koordinater
        for x in self.x_bench_positions:
            for y in self.y_bench_positions:
                self.draw_bench(x, y)

        # Rita ut texten på elevernas namn
        self.draw_student_names()

        # Rita ut bänknummer
        self.draw_bench_numbers()

        # Rita ut scenen ifall provet är i Aulan
        if self.room_name == "Aula" or self.room_name == "Aula_Halvfull":
            self.draw_aula_scene()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

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
        if key == arcade.key.Q or arcade.key.ESCAPE:  # Avsluta med "ESC" eller "Q"
            exit()

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


def draw(information):
    """ Main method. Denna funktion anropar hela denna fil """
    game = PlacementDraw(SCREEN_WIDTH, SCREEN_HEIGHT, information)
    game.setup()
    arcade.run()
