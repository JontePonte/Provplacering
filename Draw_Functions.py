
def get_room_name():
    """ Läs rummets namn från Placement """
    file2 = open("Placement.txt")
    f = file2.read().split(",")
    f = f[0].replace("[", "")
    return f
