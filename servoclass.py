"""
math model for servo-motor
"""


class Servo():
    __angle = 0
    __min_angle = 0
    __max_angle = 360

    def __init__(self):
        nothing = 0

    def set_min_angle(self, angle):
        if 0 <= angle < self.__max_angle:
            self.__min_angle = angle
        else:
            print("angle is out of limits")

    def get_min_angle(self):
        return self.__min_angle

    def set_max_angle(self, angle):
        if 360 >= angle > self.__min_angle:
            self.__max_angle = angle
        else:
            print("angle is out of limits")

    def get_max_angle(self):
        return self.__max_angle

    def set_limits(self, min, max):
        if 360 >= max > min >= 0:
            self.__min_angle = min
            self.__max_angle = max

    def set_angle(self, angle):
        if self.__min_angle <= angle <= self.__max_angle:
            self.__angle = angle
        else:
            print("angle is out of limits")

    def get_angle(self):
        return self.__angle
