# Author : Sreram Vasudev
# Date : 12/5/2023
# Description : This program that takes in the value for the text symbol and assigns
# the value to the new member variables.

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        """A function to get the name and symbol of the vegetable and a value representing the number of points the vegetable is worth
        :param name: Name of the vegetable
        :type name: string
        :param symbol: The symbol of the vegetable
        :type symbol: string
        :param points: Number of points the vegetable is worth
        :type points: integer"""
        super().__init__(symbol)
        self._name = name
        self._points = points

    def __str__(self):
        return f"{self._symbol} {self._name} {self._points}"

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

    def get_points(self):
        return self._points
    
    def set_points(self, new_points):
        self._points = new_points
