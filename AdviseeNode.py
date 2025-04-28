# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 4/24/2025
# Sets and gets info related to Advisees

class AdviseeNode:
    def __init__(self, AdviseeNode):
        self.__AdviseeNode = AdviseeNode
        self.next = None

    def setAdviseeNode(self, AdviseeNode):
        self.__studentID = AdviseeNode

    def getAdviseeNode(self):
        return self.__AdviseeNode

    def __str__(self):
        return f"Node Data: {self.__AdviseeNode}\n"
