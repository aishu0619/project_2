from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x_axis, y_axis):
        """A function to get x and y coordinates of the rabbit
        :param x_axis: x coordinate of the rabbit
        :type x_axis: integer
        :param x_axis: x coordinate of the rabbit
        :type x_axis: integer"""
        super().__init__(x_axis, y_axis,"R")

    def updateLocation(self, newXaxis, newYaxis):
        self.x_axis = newXaxis
        self.y_axis = newYaxis  
