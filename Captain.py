from Creature import Creature

class Captain(Creature):
    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis,"V")
        self._collected_veggie = []

    def addVeggie(self, veggie):
        self._collected_veggie.append(veggie)

    def get_collected_veggie(self):
        return self._collected_veggie
    
    def set_collected_veggie(self, veggie):
        self._collected_veggie = veggie

    def updateLocation(self, newXaxis, newYaxis):
        self.x_axis = newXaxis
        self.y_axis = newYaxis 