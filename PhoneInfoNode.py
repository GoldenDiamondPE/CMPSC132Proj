class PhoneNode:
    def __init__(self, phone):
        self.__phone = phone
        self.next = None

    def setStudentPhone(self, phone):
        self.__phone = phone

    def getStudentPhone(self):
        return self.__phone

    def __str__(self):
        return f"Node Data: {self.__phone}\n"
