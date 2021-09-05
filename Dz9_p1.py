from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.color = (('Red', 5), ('Yellow', 2), ('Green', 4), ('Yellow', 2))

    def running(self):
        for color, sec in cycle(self.color):
            print(color, '(До переключения {} сек.)'.format(sec))
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()

