from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis,"R")

    def updateLocation(self, newXaxis, newYaxis):
        self.x_axis = newXaxis
        self.y_axis = newYaxis  
        