from PhoneInfoNode import PhoneNode

class PhoneLinkedList:
    def __init__(self):
        self.head = None

    def addPhone(self, info):
        newNode = PhoneNode(info)
        newNode.next = self.head
        self.head = newNode

    def removePhone(self, info):
        prev = None
        current = self.head
        while current:
            if current.phone.getStudentPhone() == info:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # successfully removed
            prev = current
            current = current.next
        return False  # course not found

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.getStudentPhone()) + "\n"
            current = current.next
        return result.strip()
