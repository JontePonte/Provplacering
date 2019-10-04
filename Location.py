
class Location:
    """ Egenskap för skrivplats """
    def __init__(self, info):
        self.occupied = False
        self.x_cor = info[0]
        self.y_cor = info[1]

