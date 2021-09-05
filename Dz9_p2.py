class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass):
        self.mass = mass

    def thickness(self, thickness):
        self.thickness = thickness


    def sum_road (self):
        print (f"{self._length * self._width * self.mass * self.thickness / 1000}.т" )



road_1 = Road(50000, 10)
road_1.mass(25)
road_1.thickness(3)
print(road_1.sum_road())


road_2 = Road(50000, 10)
road_2.mass(30)
road_2.thickness(5)
print(road_2.sum_road())
