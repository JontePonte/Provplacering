
import arcade

SCREEN_SIDE = 600
SCREEN_WIDTH = SCREEN_SIDE
SCREEN_HEIGHT = SCREEN_SIDE


class PlacementDraw(arcade.Window):
    """
    Rita upp classrummet och placera eleverna utifrån informationen i "Placement.txt"
    """

    def __init__(self, width, height, information):
        super().__init__(width, height, information[0])

        # Sortera informationen i "information"
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

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):

        if self.room_name == "Aula":
            # Sätt x-koordinater för bänkarna i Aulan
            self.x_bench_positions = [
                int(1 * SCREEN_HEIGHT / 8),
                int(2 * SCREEN_HEIGHT / 8),
                int(3 * SCREEN_HEIGHT / 8),
                int(5 * SCREEN_HEIGHT / 8),
                int(6 * SCREEN_HEIGHT / 8),
            ]
            # Sätt y-koordinater för bänkarna i Aulan
            for i in range(self.y_num):
                self.y_bench_positions.append(int((i + 1) * SCREEN_HEIGHT / (self.y_num + 2)))

            self.bench_height = int(SCREEN_HEIGHT / 30)
            self.bench_width = int(SCREEN_WIDTH / 10)

            print(self.x_positions)
            print(self.y_positions)

    def draw_bench(self, x, y):
        """ Rita ut en skrivplats """
        arcade.draw_lrtb_rectangle_filled(x, x + self.bench_width, y, y - self.bench_height,
                                          arcade.color.LIVER_CHESTNUT)

    def draw_aula_scene(self):
        """ Rita ut en scenen i Aulan """
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT
        x_width = SCREEN_WIDTH / 5
        y_width = SCREEN_HEIGHT / 20
        arcade.draw_lrtb_rectangle_filled(x - x_width, x + x_width, y, y - y_width,
                                          arcade.color.DARK_CHESTNUT)


    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        for x in self.x_bench_positions:
            for y in self.y_bench_positions:
                self.draw_bench(x, y)
        if self.room_name == "Aula":
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


def draw(information):
    """ Main method """
    game = PlacementDraw(SCREEN_WIDTH, SCREEN_HEIGHT, information)
    game.setup()
    arcade.run()
