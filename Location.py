
class Location:
    """ Egenskap för skrivplats """
    def __init__(self, info):
        self.occupied = False
        self.student_name = "None"
        self.x_cor, self.y_cor = info
