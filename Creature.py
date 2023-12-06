# Author : Sreram Vasudev
# Date : 12/5/2023
# Description : This program gets the x and y coordinates of the creature and
# a symbol for the creature

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x_axis, y_axis, symbol):
        """A function to get the x and y coordinates and the symbol
        :param x_axis: x coordinate of the creature
        :type x_axis: int
        :param y_axis: y coordinate of the creature
        :type y_axis: int
        :param symbol: The text symbol representing field inhabitant
        :type symbol: string"""
        super().__init__(symbol)
        self._x = x_axis
        self._y = y_axis

    def get_x_axis(self):
        return self._x
    
    def set_x_axis(self, new_xaxis):
        self._x = new_xaxis

    def get_points(self):
        return self._y
    
    def set_points(self, new_yaxis):
        self._y = new_yaxis
