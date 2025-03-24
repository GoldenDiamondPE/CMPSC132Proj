# CMPSC132
# Brandon and Gabe
# 3/24/2025
# This program has the class Date to gather information regarding dates from birthdays to acceptance date.

class Date():
    def __init__(self, mm, dd, yyyy):
        self.__mm = mm
        self.__dd = dd
        self.__yyyy = yyyy

    def set_mm(self, mm):
        self.__mm = mm

    def set_dd(self, dd):
        self.__dd = dd

    def set_yyyy(self, yyyy):
        self.__yyyy = yyyy

    def get_mm(self):
        return self.__mm

    def get_dd(self):
        return self.__dd

    def get_yyyy(self):
        return self.__yyyy

    def __str__(self):
        return f"{self.__mm}-{self.__dd}-{self.__yyyy}"