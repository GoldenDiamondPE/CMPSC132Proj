# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 4/24/2025
# Course Nodes for the linked list

class CourseNode:
    def __init__(self, course):
        self.__course = course
        self.next = None

    def setCourse(self, course):
        self.__course = course

    def getCourse(self):
        return self.__course

    def __str__(self):
        return f"Node Data: {self.__course}\n"
