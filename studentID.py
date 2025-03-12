class studentIDNum:
    def __init__(self, studentID):
        self.__studentID = studentID

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def getStudentID(self):
        return self.__studentID

    def __str__(self):
        return str(self.__studentID)