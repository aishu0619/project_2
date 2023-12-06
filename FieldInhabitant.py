# Author : Sreram Vasudev
# Date : 12/5/2023
# Description : This program that takes in the value for the text symbol and assigns
# the value to the new member variables.

class FieldInhabitant:
    def __init__(self,symbol):
        """A function to get the text symbol representing the field inhabitant
        :param symbol: The text symbol representing field inhabitant
        :type symbol: string"""
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, new_symbol):
        self._symbol = new_symbol

   
