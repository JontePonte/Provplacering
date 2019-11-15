
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


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
        self.location_height = 1
        self.location_width = 1

        if self.room_name == "aula":
            self.x_positions = [
                1 * SCREEN_HEIGHT / 7,
                3 * SCREEN_HEIGHT / 7,
                5 * SCREEN_HEIGHT / 7,
                6 * SCREEN_HEIGHT / 7,
            ]
            for i in range(self.y_num):
                self.y_positions = (i+1) * SCREEN_HEIGHT / self.y_num

        # Samla ihop x & y - koordinater
        for i in range(len(self.x_positions)):
            pass #self.positions[i] = []

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def draw_location(self, x, y):
        """ Rita ut en skrivplats """
        arcade.draw_lrtb_rectangle_filled(x, x + 100, y, y - 40,
                                          arcade.color.DARK_BROWN)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.draw_location(400, 400)

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
