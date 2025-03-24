# CMPSC132
# Brandon and Gabe
# 3/24/2025
# This contains the ID of the student which is unique for each student

class studentIDNum:
    def __init__(self, studentID):
        self.__studentID = studentID

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def getStudentID(self):
        return self.__studentID

    def __str__(self):
        return str(self.__studentID)